// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// ตั้งค่า i18n: รองรับสองภาษา ไทย (ค่าตั้งต้น) / อังกฤษ
// เส้นทางจะเป็น /th/... และ /en/...  (prefixDefaultLocale: true => ทุกภาษามี prefix)
export default defineConfig({
  // โดเมนจริงบน Netlify (เปลี่ยนได้ถ้าตั้ง custom domain ภายหลัง)
  site: "https://deft-jelly-682bd9.netlify.app",
  i18n: {
    locales: ["th", "en"],
    defaultLocale: "th",
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: true,
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
