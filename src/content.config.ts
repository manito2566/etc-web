import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// ========================================================
//  เนื้อหาเว็บไซต์สาขา (งานประกันคุณภาพย้ายไปอยู่ระบบทวนสอบ)
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

// ผลงานนิสิต (showcase)
const projects = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: z.object({
    title_th: z.string(),
    title_en: z.string().optional().default(""),
    category_th: z.string().optional().default(""),
    category_en: z.string().optional().default(""),
    year: z.number().optional(),
    award_th: z.string().optional().default(""),
    award_en: z.string().optional().default(""),
    student: z.string().optional().default(""),
    icon: z.string().optional().default("star"),
    cover: z.string().optional().default(""),
    link: z.string().optional().default(""),
    desc_th: z.string().optional().default(""),
    desc_en: z.string().optional().default(""),
    order: z.number().optional().default(0),
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
    website: z.string().optional().default(""),
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

export const collections = { pages, courses, projects, staff, news };
