// ค่าตั้งค่าระดับเว็บ + ลิงก์ระบบภายนอกที่เชื่อมกับพอร์ทัล ETC

const BASE = "https://verification-msu.web.app";

export const site = {
  // หน้าแรกของระบบทวนสอบผลสัมฤทธิ์ (CLO/PLO) — แอปแยกที่มีอยู่เดิม
  verificationUrl: `${BASE}/dashboard/`,

  // โมดูลย่อยของระบบทวนสอบ ใช้ทำดีปลิงก์รายเกณฑ์ AUN-QA
  verification: {
    plo: { url: `${BASE}/reports/plo-achievement/`, th: "รายงานการบรรลุ PLO", en: "PLO achievement report" },
    clo: { url: `${BASE}/reports/clo-achievement/`, th: "รายงานการบรรลุ CLO", en: "CLO achievement report" },
    map: { url: `${BASE}/reports/curriculum-mapping/`, th: "Curriculum Map", en: "Curriculum mapping" },
    plan: { url: `${BASE}/verifications/plan/`, th: "แผน/ผลการทวนสอบ", en: "Verification plan & results" },
  },
} as const;

export type VerificationKey = keyof typeof site.verification;

// แมปตัวบ่งชี้ AUN-QA → โมดูลระบบทวนสอบที่ใช้เป็นหลักฐานสนับสนุน
export const verificationBySubcriterion: Record<string, VerificationKey[]> = {
  "1.1": ["plo"], // การกำหนด PLO
  "1.2": ["plo", "clo"], // PLO/CLO รายวิชาสอดคล้องกับ PLO หลักสูตร
  "1.5": ["plo", "plan"], // การบรรลุ PLO เมื่อสำเร็จการศึกษา
  "2.2": ["map"], // constructive alignment
  "2.4": ["map"], // การมีส่วนช่วยของรายวิชาต่อ ELO
  "4.5": ["clo"], // วิธีประเมินวัดการบรรลุ ELO
  "4.7": ["plan"], // ทบทวน/ปรับปรุงการประเมิน
  "8.4": ["plo"], // ข้อมูลแสดงการบรรลุ PLO โดยตรง
};

// คืนรายการลิงก์ระบบทวนสอบของตัวบ่งชี้หนึ่ง
export function verificationLinksFor(code: string) {
  return (verificationBySubcriterion[code] ?? []).map((k) => site.verification[k]);
}
