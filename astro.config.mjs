// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";

// ตั้งค่า i18n: รองรับสองภาษา ไทย (ค่าตั้งต้น) / อังกฤษ
// เส้นทางจะเป็น /th/... และ /en/...  (prefixDefaultLocale: true => ทุกภาษามี prefix)
export default defineConfig({
  // โดเมนจริงบน Cloudflare Pages (เปลี่ยนได้ถ้าตั้ง custom domain ภายหลัง)
  site: "https://etc-msu.pages.dev",
  i18n: {
    locales: ["th", "en"],
    defaultLocale: "th",
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: true,
    },
  },
  integrations: [
    sitemap({
      i18n: { defaultLocale: "th", locales: { th: "th-TH", en: "en-US" } },
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
