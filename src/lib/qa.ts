import { getCollection, type CollectionEntry } from "astro:content";

export type Criterion = CollectionEntry<"criteria">;
export type SubCriterion = CollectionEntry<"subcriteria">;

// โหลดเกณฑ์ทั้งหมด เรียงตาม code
export async function getCriteria(): Promise<Criterion[]> {
  const items = await getCollection("criteria");
  return items.sort((a, b) => a.data.code - b.data.code);
}

// โหลดตัวบ่งชี้ทั้งหมด เรียงตาม code (เช่น 1.1, 1.2, ..., 7.9)
export async function getSubcriteria(): Promise<SubCriterion[]> {
  const items = await getCollection("subcriteria");
  return items.sort((a, b) => cmpCode(a.data.code, b.data.code));
}

export function cmpCode(a: string, b: string): number {
  const [a1, a2] = a.split(".").map(Number);
  const [b1, b2] = b.split(".").map(Number);
  return a1 - b1 || a2 - b2;
}

// ตัวบ่งชี้ของเกณฑ์หนึ่ง (id ของ criterion entry เช่น "c1")
export function subsOfCriterion(subs: SubCriterion[], criterionId: string) {
  return subs.filter((s) => s.data.criterion.id === criterionId);
}

export interface CriterionStats {
  total: number;
  avgRating: number; // เฉลี่ยเฉพาะตัวที่ประเมินแล้ว (rating>0); 0 ถ้ายังไม่ประเมิน
  rated: number; // จำนวนที่ประเมินแล้ว
  withEvidence: number; // จำนวนที่มีหลักฐาน >= 1
  completeness: number; // % ตัวบ่งชี้ที่มีหลักฐาน
}

export function statsFor(subs: SubCriterion[]): CriterionStats {
  const total = subs.length;
  const rated = subs.filter((s) => s.data.rating > 0);
  const withEvidence = subs.filter((s) => (s.data.evidence?.length ?? 0) > 0);
  const avgRating =
    rated.length === 0
      ? 0
      : rated.reduce((sum, s) => sum + s.data.rating, 0) / rated.length;
  return {
    total,
    rated: rated.length,
    avgRating: Math.round(avgRating * 100) / 100,
    withEvidence: withEvidence.length,
    completeness: total === 0 ? 0 : Math.round((withEvidence.length / total) * 100),
  };
}

// สี/ป้ายตามสถานะ PDCA
export const pdcaStyles: Record<string, { bg: string; text: string; key: string }> = {
  none: { bg: "bg-slate-200", text: "text-slate-600", key: "qa.pdca.none" },
  plan: { bg: "bg-amber-100", text: "text-amber-800", key: "qa.pdca.plan" },
  do: { bg: "bg-blue-100", text: "text-blue-800", key: "qa.pdca.do" },
  check: { bg: "bg-violet-100", text: "text-violet-800", key: "qa.pdca.check" },
  act: { bg: "bg-emerald-100", text: "text-emerald-800", key: "qa.pdca.act" },
};

// สีตามระดับคะแนน AUN-QA (1-7); 0 = ยังไม่ประเมิน
export function ratingColor(r: number): string {
  if (r <= 0) return "bg-slate-300";
  if (r <= 3) return "bg-rose-400"; // ต่ำกว่า adequate
  if (r === 4) return "bg-amber-400"; // adequate as expected
  if (r <= 6) return "bg-emerald-400"; // better than adequate
  return "bg-emerald-600"; // excellent
}

// hex สำหรับใช้ใน SVG (เทียบเท่า ratingColor)
export function ratingHex(r: number): string {
  if (r <= 0) return "#cbd5e1";
  if (r <= 3) return "#fb7185";
  if (r === 4) return "#fbbf24";
  if (r <= 6) return "#34d399";
  return "#059669";
}

// ---------- ผลประเมินรายปี (กราฟแนวโน้ม) ----------
export type Assessment = CollectionEntry<"assessments">;

export async function getAssessments(): Promise<Assessment[]> {
  const items = await getCollection("assessments");
  return items.sort((a, b) => a.data.year - b.data.year);
}

// คะแนนรวมของปีหนึ่ง: ใช้ค่า overall ถ้ามี ไม่งั้นเฉลี่ยจาก scores
export function overallOf(a: Assessment): number {
  if (typeof a.data.overall === "number") return round2(a.data.overall);
  const s = a.data.scores;
  if (s.length === 0) return 0;
  return round2(s.reduce((sum, x) => sum + x.score, 0) / s.length);
}

// คะแนนของเกณฑ์หนึ่งในปีหนึ่ง (0 ถ้าไม่มี)
export function scoreOf(a: Assessment, criterion: number): number {
  return a.data.scores.find((x) => x.criterion === criterion)?.score ?? 0;
}

function round2(n: number): number {
  return Math.round(n * 100) / 100;
}

// ----- เกณฑ์คะแนน AUN-QA 7 ระดับ (ข้อมูลอ้างอิง) -----
export interface RatingLevel {
  level: number;
  name_th: string;
  name_en: string;
  desc_th: string;
  desc_en: string;
}

// คำอธิบายภาษาไทยตามถ้อยคำทางการในเอกสาร มคอ.7 (AUN-QA v4.0)
export const ratingScale: RatingLevel[] = [
  {
    level: 1,
    name_th: "คุณภาพไม่เพียงพออย่างชัดเจน",
    name_en: "Absolutely Inadequate",
    desc_th: "ไม่ปรากฏผลการดำเนินการ ไม่มีเอกสาร ไม่มีแผน หรือไม่มีหลักฐานสนับสนุน จำเป็นต้องปรับปรุง แก้ไข หรือพัฒนาอย่างเร่งด่วน",
    desc_en: "The QA practice is not implemented; no plans, documents, evidence or results. Immediate improvement must be made.",
  },
  {
    level: 2,
    name_th: "คุณภาพไม่เพียงพอ จำเป็นต้องมีการปรับปรุง",
    name_en: "Inadequate and Improvement is Necessary",
    desc_th: "มีการวางแผนแต่ยังไม่ได้เริ่มดำเนินการ เอกสารและหลักฐานไม่เพียงพอหรือมีเพียงเล็กน้อย ยังไม่เห็นผลลัพธ์ จำเป็นต้องปรับปรุง",
    desc_en: "The QA practice is at planning stage or inadequate; little document or evidence, poor results. Improvement is necessary.",
  },
  {
    level: 3,
    name_th: "คุณภาพไม่เพียงพอ แต่ปรับปรุงเล็กน้อยจะทำให้เพียงพอได้",
    name_en: "Inadequate but Minor Improvement Will Make It Adequate",
    desc_th: "มีการดำเนินการตามเกณฑ์และมีเอกสารบ้าง แต่ยังขาดความชัดเจนและการเชื่อมโยงสู่การปฏิบัติ ผลการดำเนินงานยังไม่สมบูรณ์ในบางผลลัพธ์",
    desc_en: "Defined and implemented but minor improvement needed; documents available but inconsistent results.",
  },
  {
    level: 4,
    name_th: "มีคุณภาพการดำเนินการตามเกณฑ์ (เพียงพอตามที่คาดหวัง)",
    name_en: "Adequate as Expected",
    desc_th: "มีเอกสารและหลักฐานการดำเนินการตามเกณฑ์ ผลลัพธ์เกิดขึ้นตามที่คาดหวังอย่างสม่ำเสมอ",
    desc_en: "Adequate and fully implemented; consistent results as expected.",
  },
  {
    level: 5,
    name_th: "มีคุณภาพการดำเนินการดีกว่าเกณฑ์",
    name_en: "Better Than Adequate",
    desc_th: "มีเอกสารและหลักฐานชัดเจนที่แสดงการดำเนินการอย่างมีประสิทธิภาพดีกว่าเกณฑ์ ส่งผลให้เกิดผลดีและมีแนวโน้มการพัฒนาเชิงบวก",
    desc_en: "Better than adequate; efficiently implemented with good results and positive trend.",
  },
  {
    level: 6,
    name_th: "เป็นตัวอย่างของแนวปฏิบัติที่ดี",
    name_en: "Example of Best Practices",
    desc_th: "มีหลักฐานสนับสนุนการดำเนินการตามเกณฑ์อย่างมีประสิทธิภาพ ผลลัพธ์การดำเนินการที่ดีและมีแนวโน้มเชิงบวก เป็นแบบอย่างของแนวปฏิบัติที่ดี",
    desc_en: "An example of best practices; effectively implemented with very good results and positive trend.",
  },
  {
    level: 7,
    name_th: "ระดับดีเยี่ยม เป็นแนวปฏิบัติระดับโลกหรือชั้นนำ",
    name_en: "Excellent (Example of World-class or Leading Practices)",
    desc_th: "ดำเนินการตามเกณฑ์อย่างมีนวัตกรรม มีผลลัพธ์โดดเด่นในระดับโลก มีแนวโน้มเชิงบวกชัดเจน สามารถนำไปเป็นแนวปฏิบัติชั้นนำได้",
    desc_en: "Excellent, an example of world-class or leading practices; innovatively implemented with outstanding results.",
  },
];
