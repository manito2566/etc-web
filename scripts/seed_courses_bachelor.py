# -*- coding: utf-8 -*-
"""
Seed ป.ตรี courses (เฉพาะวิชาเอก/วิชาหลักของภาควิชา) จาก มคอ.2
กศ.บ. เทคโนโลยีการศึกษาและคอมพิวเตอร์ศึกษา (หลักสูตรปรับปรุง พ.ศ. 2567)
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "content" / "courses"
OUT.mkdir(parents=True, exist_ok=True)

# (code, name_th, name_en, credits, category_th, category_en, order)
COURSES = [
    # วิชาบังคับเอกเทคโนโลยีการศึกษา
    ("0537 113", "หลักการและทฤษฎีเทคโนโลยีและสื่อสารการศึกษา", "Principles and Theories of Educational Communication and Technology", "3(3-0-6)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 1),
    ("0537 114", "การผลิตสื่อกราฟิกเพื่อการศึกษา", "Graphic Media Production for Education", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 2),
    ("0537 116", "การปฏิบัติการควบคุมและการใช้อุปกรณ์การเรียนการสอน", "Operation of Instructional Equipment", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 3),
    ("0537 117", "กิจกรรมทางเทคโนโลยีการศึกษา", "Activities in Educational Technology", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 4),
    ("0537 211", "นวัตกรรมทางเทคโนโลยีและสื่อสารการศึกษา", "Innovation in Educational Technology and Communications", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 5),
    ("0537 212", "การถ่ายภาพดิจิทัลเพื่อการสื่อความหมายทางการศึกษา", "Photography for Educational Communications", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 6),
    ("0537 213", "การออกแบบระบบการเรียนการสอนเพื่อการผลิตสื่อการศึกษา", "Instructional System Design for Instructional Media Production", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 7),
    ("0537 214", "การผลิตสื่อมัลติมีเดียเพื่อการเรียนการสอนและการนำเสนอ", "Multimedia Production for Instruction and Presentation", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 8),
    ("0537 318", "การผลิตสื่อวิดีทัศน์ดิจิทัลเพื่อเผยแพร่ในเครือข่าย", "Video Digital Media Production to Streaming", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 9),
    ("0537 319", "การออกแบบและผลิตแอนิเมชันเพื่อการเรียนการสอนและการนำเสนอ", "Design and Production of Animations for Instruction and Presentations", "3(2-2-5)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 10),
    ("0537 332", "การจัดการเทคโนโลยีและสื่อสารการศึกษา", "Management of Educational Technology and Communication", "3(3-0-6)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 11),
    ("0537 333", "ประเด็นและแนวโน้มทางเทคโนโลยีการศึกษา", "Issues and Trends in Educational Technology", "2(1-2-3)", "วิชาบังคับเอกเทคโนโลยีการศึกษา", "Required — Educational Technology", 12),

    # วิชาบังคับเอกคอมพิวเตอร์ศึกษา
    ("0537 112", "ความรู้เบื้องต้นเกี่ยวกับคอมพิวเตอร์", "Fundamentals of Computer", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 1),
    ("0537 115", "การออกแบบคอมพิวเตอร์กราฟิกเพื่อผลิตสื่อการศึกษา", "Designing Computer Graphic for Instructional Media Production", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 2),
    ("0537 334", "วิทยาการคำนวณและการออกแบบเทคโนโลยี", "Computation and Design Technology", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 3),
    ("0537 335", "การพัฒนาโปรแกรมประยุกต์บนอุปกรณ์เคลื่อนที่สำหรับการศึกษา", "Mobile Application Development for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 4),
    ("0537 336", "วิทยาการหุ่นยนต์เบื้องต้นเพื่อการศึกษา", "Introduction to Robotics for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 5),
    ("0537 337", "ประเด็นและแนวโน้มด้านคอมพิวเตอร์เพื่อการศึกษา", "Issues and Trends in Computer Education", "2(1-2-3)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 6),
    ("0537 344", "ปัญญาประดิษฐ์เบื้องต้นสำหรับการศึกษา", "Introduction of Artificial Intelligence for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 7),
    ("1204 437", "การแก้ปัญหาทางวิทยาการคอมพิวเตอร์สำหรับศึกษาศาสตร์", "Problem Solving of Computer Science for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 8),
    ("1204 440", "หลักการโปรแกรมคอมพิวเตอร์สำหรับศึกษาศาสตร์", "Principles of Computer Programming for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 9),
    ("1204 441", "ระบบสื่อสารข้อมูลและเครือข่ายคอมพิวเตอร์สำหรับศึกษาศาสตร์", "Communication Systems and Computer Network for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 10),
    ("1204 442", "การออกแบบและการจัดการฐานข้อมูลสำหรับศึกษาศาสตร์", "Database Design and Management for Education", "3(2-2-5)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 11),
    ("1204 443", "การวิเคราะห์และออกแบบระบบสำหรับศึกษาศาสตร์", "System Analysis and Design for Education", "3(3-0-6)", "วิชาบังคับเอกคอมพิวเตอร์ศึกษา", "Required — Computer Education", 12),

    # วิชาการสอนเอก
    ("0537 342", "การฝึกปฏิบัติการเทคโนโลยีการศึกษา", "Practicum in Educational Technology", "3(2-2-5)", "วิชาการสอนเอก", "Teaching Methodology", 1),
    ("0537 343", "วิธีวิทยาการสอนคอมพิวเตอร์", "Methodology in Teaching Computer", "3(2-2-5)", "วิชาการสอนเอก", "Teaching Methodology", 2),

    # วิชาเลือกเอกเทคโนโลยีการศึกษา
    ("0537 215", "อินเทอร์เน็ตสำหรับสรรพสิ่งการเรียนรู้", "Internet of Things for Education", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 1),
    ("0537 216", "การออกแบบและพัฒนาบอร์ดเกมเพื่อการศึกษา", "Design and Development of Educational Board Game", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 2),
    ("0537 322", "การผลิตสื่อสิ่งพิมพ์เพื่อการศึกษา", "Print Media Production for Education", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 3),
    ("0537 323", "เทคโนโลยีสิ่งอำนวยความสะดวกสำหรับเด็กบกพร่องทางการเรียนรู้", "Educational Assistive Technology for the Learning Disabilities", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 4),
    ("0537 325", "แหล่งเรียนรู้และการศึกษานอกสถานที่", "Learning Resources and Educational Field Trip", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 5),
    ("0537 327", "การฝึกอบรมเพื่อพัฒนาบุคลากรทางการศึกษา", "Training for Educational Human Resource Development", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 6),
    ("0537 341", "การออกแบบสภาพแวดล้อมการเรียนรู้ดิจิทัล", "Digital Learning Environment Design", "3(2-2-5)", "วิชาเลือกเอกเทคโนโลยีการศึกษา", "Elective — Educational Technology", 7),

    # วิชาเลือกเอกคอมพิวเตอร์ศึกษา
    ("0537 217", "อิเล็กทรอนิกส์และเทคโนโลยีสมองกลฝังตัว", "Electronic and Embedded Technology", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 1),
    ("0537 218", "คณิตศาสตร์พื้นฐานสำหรับคอมพิวเตอร์ทางการศึกษา", "Fundamental Mathematics for Computer Education", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 2),
    ("0537 338", "การออกแบบส่วนต่อประสานกับผู้ใช้", "Interface Design with User", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 3),
    ("0537 339", "การบูรณาการโปรแกรมประยุกต์เพื่อการสอน", "Application Program Integration for Instruction", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 4),
    ("0537 340", "การพัฒนาเกมคอมพิวเตอร์เพื่อการศึกษา", "Development of Computer Games for Education", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 5),
    ("0537 345", "ระบบฐานความรู้", "Knowledge Based Systems", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 6),
    ("0537 346", "เหมืองข้อมูลทางการศึกษา", "Educational Data Mining", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 7),
    ("0537 347", "วิทยาการข้อมูลเบื้องต้นเพื่อการศึกษา", "Introduction of Data Science for Education", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 8),
    ("1201 353", "การจัดการอีสปอร์ต", "E-sports Management", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 9),
    ("1204 413", "การบริหารเครือข่ายคอมพิวเตอร์", "Computer Network Administration", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 10),
    ("1204 444", "กฎหมายและจริยธรรมทางเทคโนโลยีสารสนเทศสำหรับศึกษาศาสตร์", "Legal and Ethical Issues in Information Technology for Education", "2(2-0-4)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 11),
    ("1204 445", "การโปรแกรมจินตภาพสำหรับศึกษาศาสตร์", "Visual Programming for Education", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 12),
    ("1204 446", "การพัฒนาและการจัดการเว็บสำหรับศึกษาศาสตร์", "Web Development and Management for Education", "3(2-2-5)", "วิชาเลือกเอกคอมพิวเตอร์ศึกษา", "Elective — Computer Education", 13),
]

def esc(s: str) -> str:
    return s.replace('"', '\\"')

# กลุ่มสำหรับลำดับ global (ให้แต่ละหมวดเรียงต่อกันในตาราง)
group_order = {
    "วิชาบังคับเอกเทคโนโลยีการศึกษา": 100,
    "วิชาบังคับเอกคอมพิวเตอร์ศึกษา": 200,
    "วิชาการสอนเอก": 300,
    "วิชาเลือกเอกเทคโนโลยีการศึกษา": 400,
    "วิชาเลือกเอกคอมพิวเตอร์ศึกษา": 500,
}

for code, name_th, name_en, credits, cat_th, cat_en, local_order in COURSES:
    slug = code.replace(" ", "")
    p = OUT / f"b-{slug}.md"
    global_order = group_order[cat_th] + local_order
    p.write_text(
        f'---\n'
        f'code: "{code}"\n'
        f'name_th: "{esc(name_th)}"\n'
        f'name_en: "{esc(name_en)}"\n'
        f'program: "bachelor"\n'
        f'category_th: "{esc(cat_th)}"\n'
        f'category_en: "{esc(cat_en)}"\n'
        f'credits: "{credits}"\n'
        f'order: {global_order}\n'
        f'---\n',
        encoding="utf-8",
    )

print(f"created {len(COURSES)} bachelor course files")
