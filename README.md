# เว็บไซต์สาขา ETC + ระบบสารสนเทศ AUN-QA v4.0

เว็บไซต์เดียวที่ทำงาน 2 ชั้น: **ประชาสัมพันธ์สาขา** + **ระบบจัดการข้อมูล AUN-QA v4.0**
(8 เกณฑ์ 53 ตัวบ่งชี้) สองภาษา ไทย/อังกฤษ — เป็นเว็บสแตติก โฮสต์ฟรีได้
และให้ประธาน/อาจารย์แก้เนื้อหาเองผ่านหน้าจอ `/admin`

## สถาปัตยกรรม

| ชั้น | เครื่องมือ |
|------|-----------|
| Static site | Astro 5 (content collections + i18n) |
| สไตล์ | Tailwind CSS v4 |
| CMS แก้ผ่านหน้าจอ | Sveltia CMS (`/admin`) — commit เข้า Git อัตโนมัติ |
| โฮสติง | Netlify / Vercel / GitHub Pages (ฟรี) |

ข้อมูลทั้งหมดเก็บเป็นไฟล์ Markdown ใน `src/content/` → เป็น **แหล่งข้อมูลเดียว**
ที่ป้อนทั้งหน้าเว็บ Dashboard และมุมมอง SAR

## โครงสร้างข้อมูล AUN-QA

- `src/content/criteria/` — 8 เกณฑ์ (c1–c8)
- `src/content/subcriteria/` — 53 ตัวบ่งชี้
  - การกระจาย: **C1=5, C2=7, C3=6, C4=7, C5=8, C6=6, C7=9, C8=5 = 53**
  - แต่ละตัวมี: ข้อกำหนด (ไทย/อังกฤษ), narrative, PDCA, ผู้รับผิดชอบ, คะแนน 0–7, เป้าหมาย, รายการหลักฐาน
- `src/content/assessments/` — ผลการประเมินรายปี (หนึ่งไฟล์ = หนึ่งปี พ.ศ.)
  ใช้สร้าง **กราฟแนวโน้มคะแนนรายปี** บน Dashboard — เริ่มข้อมูลจริงที่ปี 2567
  (เพิ่มปีถัดไปผ่าน `/admin` แล้วเส้นแนวโน้มจะปรากฏเอง)
- `src/content/{pages,courses,staff,news}/` — เนื้อหาประชาสัมพันธ์

ตารางอ้างอิง **เกณฑ์คะแนน AUN-QA 7 ระดับ** แสดงบน Dashboard (ข้อมูลอยู่ใน `src/lib/qa.ts`)

**ระบบทวนสอบผลสัมฤทธิ์ (CLO/PLO)** เชื่อมเป็นโมดูลภายนอก (เกณฑ์ที่ 1 และ 4) —
แก้ URL ได้ที่ `src/lib/site.ts` (`verificationUrl`) ลิงก์ปรากฏที่เมนูและการ์ดบนหน้า `/qa`

> ⚠️ **การตรวจสอบข้อความข้อกำหนด:** ข้อความภาษาอังกฤษคัดลอกแบบ verbatim จาก
> *Guide to AUN-QA Assessment at Programme Level v4.0, Appendix A*
> ส่วนภาษาไทยเป็นคำแปลใช้งานที่ควรปรับให้ตรงสำนวนทางการของหน่วยงานก่อนใช้จริง

## คำสั่งพัฒนา

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # สร้างไฟล์สแตติกใน dist/
npm run preview  # ดู dist/ ก่อน deploy
```

สร้าง/รีเซ็ตข้อมูล AUN-QA ทั้ง 53 ตัว: `python scripts/seed_qa.py`

## หน้าหลักของระบบ

- `/th` `/en` — หน้าแรก + การ์ด 8 เกณฑ์
- `/th/qa` — Dashboard (ตัวเลขสรุป + เรดาร์คะแนน + ตาราง 8 เกณฑ์)
- `/th/qa/1` … `/th/qa/8` — รายเกณฑ์ พร้อมตัวบ่งชี้ย่อย/PDCA/หลักฐาน
- `/th/qa/evidence` — คลังหลักฐาน (ค้นหาได้)
- `/th/qa/sar` — มุมมองรายงานประเมินตนเอง (พิมพ์/บันทึก PDF ได้)
- `/admin` — หน้าจอจัดการเนื้อหา (Sveltia CMS)

## การแก้เนื้อหาผ่านหน้าจอ (สำหรับอาจารย์)

**ทดลองในเครื่อง (ไม่ต้องมี GitHub):**
```bash
npx @sveltia/cms-proxy-server   # เทอร์มินัลที่ 1
npm run dev                      # เทอร์มินัลที่ 2
```
เปิด `http://localhost:4321/admin/` แล้วเลือก "Work with Local Repository"

**ใช้งานจริง:** ดูหัวข้อ Deploy ด้านล่าง แล้วเข้า `https<โดเมน>/admin/` ล็อกอินด้วย GitHub

## Deploy (Netlify — แนะนำ)

1. push โค้ดขึ้น GitHub repo เช่น `etc-faculty/etc-web`
2. แก้ `public/admin/config.yml` → `repo: etc-faculty/etc-web`, `branch: main`
3. ที่ Netlify: **Add new site → Import from GitHub** เลือก repo
   - Build command: `npm run build` · Publish directory: `dist`
4. เปิดสิทธิ์ให้ CMS เขียน Git (ทางใดทางหนึ่ง):
   - ใช้ **Netlify Identity + Git Gateway** (ง่ายสุด ไม่ต้องตั้ง OAuth) หรือ
   - ตั้ง **GitHub OAuth App** แล้วใส่ client id/secret ใน Netlify (Sveltia รองรับ)
5. แก้ `site:` ใน `astro.config.mjs` ให้เป็นโดเมนจริง
6. เมื่ออาจารย์บันทึกใน `/admin` → commit เข้า Git → Netlify build เว็บใหม่อัตโนมัติ

> GitHub Pages ก็ใช้ได้ (ฟรี) แต่ต้องตั้ง GitHub OAuth เองสำหรับ `/admin`

## อ้างอิง

- Guide to AUN-QA Assessment at Programme Level v4.0 — ASEAN University Network
