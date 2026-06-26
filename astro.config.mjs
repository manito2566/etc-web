// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// ตั้งค่า i18n: รองรับสองภาษา ไทย (ค่าตั้งต้น) / อังกฤษ
// เส้นทางจะเป็น /th/... และ /en/...  (prefixDefaultLocale: true => ทุกภาษามี prefix)
export default defineConfig({
  // เปลี่ยน site ให้ตรงกับโดเมนจริงตอน deploy (เช่น https://etc.example.ac.th)
  site: "https://example.com",
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
