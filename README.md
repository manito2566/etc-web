# เว็บไซต์สาขาเทคโนโลยีการศึกษาและคอมพิวเตอร์ศึกษา (ETC)

เว็บหน้าบ้านของสาขา **กศ.บ. เทคโนโลยีการศึกษาและคอมพิวเตอร์ศึกษา คณะศึกษาศาสตร์ มหาวิทยาลัยมหาสารคาม**
ทำหน้าที่นำเสนอหลักสูตร ผลงานนิสิต อาจารย์ ศิษย์เก่า ข่าวสาร และเป็น **ศูนย์รวม (hub)**
เชื่อมระบบต่าง ๆ ของสาขาไว้ที่เดียว สองภาษา ไทย/อังกฤษ

🌐 **Live:** https://etc-msu.netlify.app

## สถาปัตยกรรม

| ชั้น | เครื่องมือ |
|------|-----------|
| Static site | Astro 5 (i18n /th, /en) |
| สไตล์ | Tailwind CSS v4 · ธีมน้ำตาล taupe + ทอง (เข้าชุดเว็บศิษย์เก่า) |
| ไอคอน | Tabler icons (webfont) |
| CMS แก้ผ่านหน้าจอ | Sveltia CMS (`/admin`) — commit เข้า Git อัตโนมัติ |
| โฮสติง | Netlify (auto-deploy จาก GitHub) |
| SEO | sitemap, Open Graph/Twitter card, canonical, robots.txt |

## โครงสร้างหน้า (IA)

หน้าแรก (hub) · เกี่ยวกับสาขา · หลักสูตร · อาจารย์ · ผลงานนิสิต · ศิษย์เก่า · ข่าว/กิจกรรม · ติดต่อ

หน้าแรกรวม: hero, ตัวเลขสำคัญ, ไฮไลต์คุณภาพ (ลิงก์ออกระบบทวนสอบ), ผลงานนิสิต,
การ์ดระบบนิเวศ, ข่าว, ศูนย์ติดต่อแยกตามกลุ่ม

## ระบบนิเวศที่เชื่อมโยง (แก้ลิงก์ที่ `src/lib/site.ts`)

- **เครือข่ายศิษย์เก่า** — https://etc-alumni-webappv1.web.app/
- **ระบบทวนสอบ / ประกันคุณภาพ** (มคอ., PLO/CLO, AUN-QA) — https://verification-msu.web.app/dashboard/
- **เว็บผลงานอาจารย์** — https://manito2566.github.io/manit-asanok.github.io/

> งานประกันคุณภาพ AUN-QA ทั้งหมดอยู่ที่ **ระบบทวนสอบ** เว็บนี้เพียงลิงก์ไปและแสดงไฮไลต์ความก้าวหน้า

## ข้อมูล (content collections)

`src/content/` → `pages` (about), `courses`, `projects` (ผลงานนิสิต), `staff`, `news`
ทุก collection มีฟิลด์คู่ `_th`/`_en` และแก้ผ่าน `/admin` ได้

## คำสั่งพัฒนา

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # สร้างไฟล์สแตติกใน dist/
```

## Deploy

push เข้า `main` → Netlify build (`npm run build` → `dist/`) และเผยแพร่อัตโนมัติ
ตั้งค่า: `astro.config.mjs` (`site`), `public/admin/config.yml` (`repo`), `netlify.toml`

## เก็บตก / พัฒนาต่อ

- ตั้ง GitHub OAuth ให้ `/admin` ล็อกอินได้ (เช่น Sveltia authenticator บน Cloudflare Workers)
- ใส่ข้อมูลจริง: ผลงานนิสิต/ภาพ, ข้อมูลติดต่อ (อีเมล/โทร), โปรไฟล์อาจารย์
- โดเมนของคณะ (custom domain) ผ่าน Netlify
