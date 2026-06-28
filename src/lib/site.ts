// ค่าตั้งค่าระดับเว็บ + ลิงก์ระบบในเครือข่ายของสาขา (ecosystem)

export const site = {
  name_th: "ภาควิชาเทคโนโลยีและสื่อสารการศึกษา",
  name_en: "Department of Educational Technology and Communications",
  shortName: "ETC",
  faculty_th: "คณะศึกษาศาสตร์ มหาวิทยาลัยมหาสารคาม",
  faculty_en: "Faculty of Education, Mahasarakham University",
  address_th: "คณะศึกษาศาสตร์ มหาวิทยาลัยมหาสารคาม ถนนนครสวรรค์ ตำบลตลาด อำเภอเมือง จังหวัดมหาสารคาม 44000",
  address_en: "Faculty of Education, Mahasarakham University, Nakhon Sawan Rd., Talat, Mueang, Maha Sarakham 44000",
  phone: "043-719852 ต่อ 6235",
  fax: "043-721764",
};

// ระบบในเครือข่ายของสาขา — แสดงเป็นการ์ดศูนย์รวมบนหน้าแรก
export const ecosystem = [
  {
    key: "alumni",
    url: "https://etc-alumni-webappv1.web.app/",
    icon: "ti-users",
    title_th: "เครือข่ายศิษย์เก่า",
    title_en: "Alumni network",
    desc_th: "ทำเนียบ · กิจกรรม · ข่าวศิษย์เก่า",
    desc_en: "Directory, events and alumni news",
  },
  {
    key: "verification",
    url: "https://verification-msu.web.app/dashboard/",
    icon: "ti-shield-check",
    title_th: "ระบบทวนสอบ / ประกันคุณภาพ",
    title_en: "Verification & QA system",
    desc_th: "มคอ. · PLO/CLO · AUN-QA",
    desc_en: "TQF, PLO/CLO and AUN-QA",
  },
  {
    key: "journal",
    url: "https://so02.tci-thaijo.org/index.php/etcedumsujournal",
    icon: "ti-book",
    title_th: "วารสารภาควิชา",
    title_en: "Department Journal",
    desc_th: "บทความวิจัย · TCI · ThaiJO",
    desc_en: "Research articles · TCI · ThaiJO",
  },
] as const;

// ลิงก์ระบบทวนสอบ (ใช้สำหรับไฮไลต์ความก้าวหน้าคุณภาพบนหน้าแรก)
export const verificationUrl = ecosystem.find((e) => e.key === "verification")!.url;
export const journalUrl = ecosystem.find((e) => e.key === "journal")!.url;
