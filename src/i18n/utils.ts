import { ui, defaultLang, type Lang, type UIKey } from "./ui";

// ดึงภาษาจาก URL (เช่น /th/about => "th")
export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split("/");
  if (lang in ui) return lang as Lang;
  return defaultLang;
}

// สร้างฟังก์ชันแปลข้อความ UI ตามภาษา
export function useTranslations(lang: Lang) {
  return function t(key: UIKey): string {
    return ui[lang][key] ?? ui[defaultLang][key];
  };
}

// เลือกค่าฟิลด์คู่ _th/_en ตามภาษา (มี fallback)
export function pick<T>(lang: Lang, th: T, en: T): T {
  const value = lang === "en" ? en : th;
  // ถ้าภาษาอังกฤษว่าง ให้ fallback เป็นไทย (และกลับกัน)
  return value || (lang === "en" ? th : en);
}

// สร้างลิงก์ที่ผูกกับภาษาปัจจุบัน เช่น localizePath("th", "/about") => "/th/about"
export function localizePath(lang: Lang, path: string): string {
  const clean = path.startsWith("/") ? path : `/${path}`;
  return `/${lang}${clean === "/" ? "" : clean}`;
}

// สลับภาษาบนเส้นทางปัจจุบัน คงพาธเดิมไว้
export function switchLangPath(url: URL, target: Lang): string {
  const parts = url.pathname.split("/");
  parts[1] = target; // ตำแหน่งแรกหลัง / คือ locale
  return parts.join("/") || `/${target}`;
}
