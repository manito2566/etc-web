# -*- coding: utf-8 -*-
"""
Seed ป.เอก courses (เฉพาะวิชาหลัก/วิชาเอกของภาควิชา) จาก มคอ.2
ปร.ด. เทคโนโลยีและสื่อสารการศึกษา (หลักสูตรปรับปรุง พ.ศ. 2566)
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "content" / "courses"
OUT.mkdir(parents=True, exist_ok=True)

COURSES = [
    # วิชาบังคับ (12 หน่วยกิต)
    ("0503 901", "วิทยาระเบียบวิธีวิจัยขั้นสูง", "Advanced Research Methodology", "3(3-0-6)", "วิชาบังคับ", "Required", 1),
    ("0503 920", "การออกแบบและการพัฒนาระบบเทคโนโลยีการเรียนการสอน", "Design and Development of Instructional System Technology", "3(1-4-4)", "วิชาบังคับ", "Required", 2),
    ("0503 970", "การพัฒนาและการจัดการระบบงานเทคโนโลยีและสื่อสารการศึกษา", "Development and Management of Educational Technology and Communications Systems", "3(1-4-4)", "วิชาบังคับ", "Required", 3),
    ("0503 980", "สัมมนาการวิจัยและประเด็นปัญหาปัจจุบันทางเทคโนโลยีและสื่อสารการศึกษา", "Seminar on Research and Current Issues in Educational Technology and Communications", "3(3-0-6)", "วิชาบังคับ", "Required", 4),

    # วิชาเลือก (ไม่น้อยกว่า 6 หน่วยกิต)
    ("0503 910", "เทคโนโลยีระบบและการพัฒนาการศึกษา", "Systems Technology and Educational Development", "3(1-4-4)", "วิชาเลือก", "Elective", 1),
    ("0503 950", "สัมมนาเทคโนโลยีและสื่อสารการศึกษาร่วมสมัย", "Seminar on Contemporary Educational Technology and Communications", "3(3-0-6)", "วิชาเลือก", "Elective", 2),
    ("0503 962", "การบูรณาการและการจัดการคอมพิวเตอร์เพื่อการศึกษา", "Integration and Management of Computers in Education", "3(1-4-4)", "วิชาเลือก", "Elective", 3),
    ("0503 972", "การจัดการแหล่งเรียนรู้", "Management of Learning Resources", "3(3-0-6)", "วิชาเลือก", "Elective", 4),
    ("0503 974", "นวัตกรรมและเทคโนโลยีพลิกผันทางการศึกษาดิจิทัล", "Innovation and Disruptive Technologies for Digital Education", "3(3-0-6)", "วิชาเลือก", "Elective", 5),
    ("0503 991", "สัมมนาเค้าโครงวิทยานิพนธ์ดุษฎีบัณฑิตเทคโนโลยีและสื่อสารการศึกษา", "Seminar in Doctoral Dissertation Topics and Proposals in Educational Technology and Communications", "3(3-0-6)", "วิชาเลือก", "Elective", 6),
]

def esc(s: str) -> str:
    return s.replace('"', '\\"')

group_order = {"วิชาบังคับ": 100, "วิชาเลือก": 200}

for code, name_th, name_en, credits, cat_th, cat_en, local_order in COURSES:
    slug = code.replace(" ", "")
    p = OUT / f"d-{slug}.md"
    global_order = group_order[cat_th] + local_order
    p.write_text(
        f'---\n'
        f'code: "{code}"\n'
        f'name_th: "{esc(name_th)}"\n'
        f'name_en: "{esc(name_en)}"\n'
        f'program: "doctoral"\n'
        f'category_th: "{esc(cat_th)}"\n'
        f'category_en: "{esc(cat_en)}"\n'
        f'credits: "{credits}"\n'
        f'order: {global_order}\n'
        f'---\n',
        encoding="utf-8",
    )

print(f"created {len(COURSES)} doctoral course files")
