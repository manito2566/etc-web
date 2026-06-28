# -*- coding: utf-8 -*-
"""
Seed ป.โท courses (เฉพาะวิชาหลัก/วิชาเอกของภาควิชา) จาก มคอ.2
กศ.ม. เทคโนโลยีและสื่อสารการศึกษา (หลักสูตรปรับปรุง พ.ศ. 2569)
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "content" / "courses"
OUT.mkdir(parents=True, exist_ok=True)

COURSES = [
    # วิชาบังคับ (แผน 1 ก2, ไม่น้อยกว่า 12 หน่วยกิต)
    ("0503 750", "เทคโนโลยีและสื่อสารการศึกษาด้วยปัญญาประดิษฐ์", "Educational Technology and Communications with Artificial Intelligence", "2(2-0-4)", "วิชาบังคับ", "Required", 1),
    ("0503 751", "การวิจัยทางเทคโนโลยีและสื่อสารการศึกษา", "Research in Educational Technology and Communications", "2(1-2-4)", "วิชาบังคับ", "Required", 2),
    ("0503 752", "การออกแบบและพัฒนาระบบการเรียนการสอน", "Design and Development of Instructional Systems", "2(2-0-4)", "วิชาบังคับ", "Required", 3),
    ("0503 753", "การศึกษาทางไกลแบบดิจิทัล", "Digital Distance Education", "2(2-0-4)", "วิชาบังคับ", "Required", 4),
    ("0503 810", "การบริหารและการจัดการงานเทคโนโลยีและสื่อสารการศึกษา", "Administration and Management of Educational Technology and Communications", "2(2-0-4)", "วิชาบังคับ", "Required", 5),
    ("0503 811", "สัมมนาการวิจัยทางเทคโนโลยีและสื่อสารการศึกษา", "Research Seminar in Educational Technology and Communications", "2(1-2-3)", "วิชาบังคับ", "Required", 6),

    # วิชาเลือก (แผน 1 ก2, ไม่น้อยกว่า 8 หน่วยกิต)
    ("0503 730", "การผลิตวีดิทัศน์และการตัดต่อด้วยระบบดิจิทัล", "Video Production and Video Editing using Digital Systems", "3(3-0-6)", "วิชาเลือก", "Elective", 1),
    ("0503 731", "การออกแบบสื่อเทคโนโลยีดิจิทัลเพื่อการเรียนการสอน", "Digital Technology Media Design for Instruction", "2(1-2-3)", "วิชาเลือก", "Elective", 2),
    ("0503 732", "การออกแบบและพัฒนาสื่อกราฟิกและการพิมพ์เพื่อการศึกษา", "Design and Development of Graphic and Printing Media for Education", "3(2-2-5)", "วิชาเลือก", "Elective", 3),
    ("0503 733", "ระบบการเรียนรู้ผ่านการจำลองสถานการณ์และเกมส์การเรียนการสอน", "Learning Systems through Simulation and Instructional Games", "3(3-0-6)", "วิชาเลือก", "Elective", 4),
    ("0503 734", "การออกแบบและพัฒนาเกมส์ดิจิทัล", "Digital Game Design and Development", "3(3-0-6)", "วิชาเลือก", "Elective", 5),
    ("0503 757", "การออกแบบกลยุทธ์การเรียนการสอนด้วยเทคโนโลยี", "Instructional Strategy Design with Technology", "2(2-0-4)", "วิชาเลือก", "Elective", 6),
    ("0503 758", "การออกแบบและพัฒนานวัตกรรมการศึกษา", "Design and Development of Educational Innovations", "3(3-0-6)", "วิชาเลือก", "Elective", 7),
    ("0503 759", "การออกแบบและพัฒนาแหล่งทรัพยากรการเรียนรู้", "Design and Development of Learning Resources", "2(1-2-3)", "วิชาเลือก", "Elective", 8),
    ("0503 760", "การฝึกอบรมและการพัฒนาทรัพยากรมนุษย์", "Training and Human Resource Development", "2(1-2-3)", "วิชาเลือก", "Elective", 9),
    ("0503 761", "การประเมินทางเทคโนโลยีและสื่อสารการศึกษา", "Evaluation in Educational Technology and Communications", "3(3-0-6)", "วิชาเลือก", "Elective", 10),
    ("0503 814", "การออกแบบและพัฒนาระบบการเรียนรู้ผ่านเครื่องมือการสื่อสารแบบเคลื่อนที่", "Design and Development of Mobile Learning Systems", "2(1-2-3)", "วิชาเลือก", "Elective", 11),
]

def esc(s: str) -> str:
    return s.replace('"', '\\"')

group_order = {"วิชาบังคับ": 100, "วิชาเลือก": 200}

for code, name_th, name_en, credits, cat_th, cat_en, local_order in COURSES:
    slug = code.replace(" ", "")
    p = OUT / f"m-{slug}.md"
    global_order = group_order[cat_th] + local_order
    p.write_text(
        f'---\n'
        f'code: "{code}"\n'
        f'name_th: "{esc(name_th)}"\n'
        f'name_en: "{esc(name_en)}"\n'
        f'program: "master"\n'
        f'category_th: "{esc(cat_th)}"\n'
        f'category_en: "{esc(cat_en)}"\n'
        f'credits: "{credits}"\n'
        f'order: {global_order}\n'
        f'---\n',
        encoding="utf-8",
    )

print(f"created {len(COURSES)} master course files")
