import { defineCollection, reference, z } from "astro:content";
import { glob } from "astro/loaders";

// ---------- ค่าคงที่ใช้ร่วม ----------
const pdcaValues = ["none", "plan", "do", "check", "act"] as const;

// รายการหลักฐาน 1 ชิ้น
const evidenceItem = z.object({
  title_th: z.string(),
  title_en: z.string().optional().default(""),
  // ลิงก์ภายนอกหรือพาธไฟล์ที่อัปโหลดผ่าน CMS (เก็บใน /public/evidence)
  link: z.string(),
  date: z.coerce.date().optional(),
});

// ========================================================
//  กลุ่ม AUN-QA — หัวใจของระบบ (single source of truth)
// ========================================================

// 8 เกณฑ์ของ AUN-QA v4.0
const criteria = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/criteria" }),
  schema: z.object({
    code: z.number().int().min(1).max(8), // เกณฑ์ที่ 1-8
    title_th: z.string(),
    title_en: z.string(),
    intro_th: z.string().optional().default(""),
    intro_en: z.string().optional().default(""),
    order: z.number().optional(),
  }),
});

// 53 ตัวบ่งชี้ย่อย (C1=3, C2=7, C3=7, C4=7, C5=8, C6=7, C7=9, C8=5)
const subcriteria = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/subcriteria" }),
  schema: z.object({
    code: z.string(), // เช่น "1.1", "7.9"
    criterion: reference("criteria"), // อ้างถึงเกณฑ์แม่
    requirement_th: z.string(),
    requirement_en: z.string(),
    narrative_th: z.string().optional().default(""),
    narrative_en: z.string().optional().default(""),
    pdca: z.enum(pdcaValues).default("none"),
    responsible: z.string().optional().default(""),
    rating: z.number().int().min(0).max(7).default(0), // 0 = ยังไม่ประเมิน, 1-7 ตาม AUN-QA
    target: z.number().int().min(1).max(7).default(4),
    evidence: z.array(evidenceItem).default([]),
  }),
});

// ผลการประเมินรายปี (หนึ่งไฟล์ = หนึ่งปีการศึกษา) ใช้ทำกราฟแนวโน้มคะแนน
const assessments = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/assessments" }),
  schema: z.object({
    year: z.number().int(), // ปี พ.ศ. เช่น 2567
    label: z.string().optional().default(""), // ป้ายแสดงผล เช่น "2567"
    note_th: z.string().optional().default(""),
    note_en: z.string().optional().default(""),
    // คะแนนรายเกณฑ์ 1-8 (ระดับ 1-7 ตาม AUN-QA); ใส่เท่าที่ประเมินแล้ว
    scores: z
      .array(
        z.object({
          criterion: z.number().int().min(1).max(8),
          score: z.number().min(1).max(7),
        })
      )
      .default([]),
    // คะแนนรวม (ถ้าเว้นว่างจะคำนวณเฉลี่ยจาก scores)
    overall: z.number().min(1).max(7).optional(),
  }),
});

// ========================================================
//  กลุ่มเว็บประชาสัมพันธ์
// ========================================================

// หน้าเนื้อหาทั่วไป (about, วิสัยทัศน์, PLO/CLO)
const pages = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/pages" }),
  schema: z.object({
    title_th: z.string(),
    title_en: z.string(),
    body_th: z.string().optional().default(""),
    body_en: z.string().optional().default(""),
    order: z.number().optional().default(0),
  }),
});

// รายวิชา
const courses = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/courses" }),
  schema: z.object({
    code: z.string(), // รหัสวิชา
    name_th: z.string(),
    name_en: z.string(),
    credits: z.number().optional(),
    year: z.number().optional(), // ชั้นปีที่เรียน
    desc_th: z.string().optional().default(""),
    desc_en: z.string().optional().default(""),
  }),
});

// อาจารย์ประจำหลักสูตร
const staff = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/staff" }),
  schema: z.object({
    name_th: z.string(),
    name_en: z.string(),
    position_th: z.string().optional().default(""),
    position_en: z.string().optional().default(""),
    email: z.string().optional().default(""),
    expertise_th: z.string().optional().default(""),
    expertise_en: z.string().optional().default(""),
    photo: z.string().optional().default(""),
    order: z.number().optional().default(0),
  }),
});

// ข่าว/กิจกรรม
const news = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/news" }),
  schema: z.object({
    title_th: z.string(),
    title_en: z.string().optional().default(""),
    date: z.coerce.date(),
    summary_th: z.string().optional().default(""),
    summary_en: z.string().optional().default(""),
    cover: z.string().optional().default(""),
    body_th: z.string().optional().default(""),
    body_en: z.string().optional().default(""),
  }),
});

export const collections = { criteria, subcriteria, assessments, pages, courses, staff, news };
