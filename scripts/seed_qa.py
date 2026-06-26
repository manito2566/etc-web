# -*- coding: utf-8 -*-
"""
Seed AUN-QA v4.0 content files (8 criteria + 53 sub-criteria).
English requirement texts are VERBATIM from the official "Guide to AUN-QA
Assessment at Programme Level Version 4.0", Appendix A (Self-rating checklist).
Thai texts are working translations to be verified/refined by the programme chair.

Run:  python scripts/seed_qa.py
"""
import os, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CRIT_DIR = ROOT / "src" / "content" / "criteria"
SUB_DIR = ROOT / "src" / "content" / "subcriteria"
CRIT_DIR.mkdir(parents=True, exist_ok=True)
SUB_DIR.mkdir(parents=True, exist_ok=True)

CRITERIA = [
    (1, "Expected Learning Outcomes", "ผลการเรียนรู้ที่คาดหวัง"),
    (2, "Programme Structure and Content", "โครงสร้างและเนื้อหาของหลักสูตร"),
    (3, "Teaching and Learning Approach", "แนวทางการจัดการเรียนการสอน"),
    (4, "Student Assessment", "การประเมินผู้เรียน"),
    (5, "Academic Staff", "บุคลากรสายวิชาการ"),
    (6, "Student Support Services", "การบริการและช่วยเหลือผู้เรียน"),
    (7, "Facilities and Infrastructure", "สิ่งสนับสนุนการเรียนรู้และโครงสร้างพื้นฐาน"),
    (8, "Output and Outcomes", "ผลผลิตและผลลัพธ์"),
]

# (code, requirement_en, requirement_th)
SUBS = [
    ("1.1",
     "The programme to show that the expected learning outcomes are appropriately formulated in accordance with an established learning taxonomy, are aligned to the vision and mission of the university, and are known to all stakeholders.",
     "หลักสูตรแสดงให้เห็นว่าผลการเรียนรู้ที่คาดหวังถูกกำหนดอย่างเหมาะสมตามอนุกรมวิธานการเรียนรู้ที่เป็นที่ยอมรับ สอดคล้องกับวิสัยทัศน์และพันธกิจของมหาวิทยาลัย และเป็นที่รับรู้ของผู้มีส่วนได้ส่วนเสียทุกฝ่าย"),
    ("1.2",
     "The programme to show that the expected learning outcomes for all courses are appropriately formulated and are aligned to the expected learning outcomes of the programme.",
     "หลักสูตรแสดงให้เห็นว่าผลการเรียนรู้ที่คาดหวังของทุกรายวิชาถูกกำหนดอย่างเหมาะสมและสอดคล้องกับผลการเรียนรู้ที่คาดหวังของหลักสูตร"),
    ("1.3",
     "The programme to show that the expected learning outcomes consist of both generic outcomes (related to written and oral communication, problem-solving, information technology, teambuilding skills, etc.) and subject specific outcomes (related to knowledge and skills of the study discipline).",
     "หลักสูตรแสดงให้เห็นว่าผลการเรียนรู้ที่คาดหวังประกอบด้วยทั้งผลการเรียนรู้ทั่วไป (การสื่อสารด้วยการเขียนและการพูด การแก้ปัญหา เทคโนโลยีสารสนเทศ ทักษะการทำงานเป็นทีม ฯลฯ) และผลการเรียนรู้เฉพาะสาขา (ความรู้และทักษะของศาสตร์ที่ศึกษา)"),
    ("1.4",
     "The programme to show that the requirements of the stakeholders, especially the external stakeholders, are gathered, and that these are reflected in the expected learning outcomes.",
     "หลักสูตรแสดงให้เห็นว่ามีการรวบรวมความต้องการของผู้มีส่วนได้ส่วนเสีย โดยเฉพาะผู้มีส่วนได้ส่วนเสียภายนอก และนำมาสะท้อนไว้ในผลการเรียนรู้ที่คาดหวัง"),
    ("1.5",
     "The programme to show that the expected learning outcomes are achieved by the students by the time they graduate.",
     "หลักสูตรแสดงให้เห็นว่าผู้เรียนบรรลุผลการเรียนรู้ที่คาดหวังเมื่อสำเร็จการศึกษา"),

    ("2.1",
     "The specifications of the programme and all its courses are shown to be comprehensive, up-to-date, and made available and communicated to all stakeholders.",
     "รายละเอียดของหลักสูตรและทุกรายวิชาแสดงให้เห็นว่ามีความครบถ้วน ทันสมัย และเผยแพร่สื่อสารให้ผู้มีส่วนได้ส่วนเสียทุกฝ่ายรับทราบ"),
    ("2.2",
     "The design of the curriculum is shown to be constructively aligned with achieving the expected learning outcomes.",
     "การออกแบบหลักสูตรแสดงให้เห็นว่าสอดคล้องเชิงสร้างสรรค์ (constructive alignment) กับการบรรลุผลการเรียนรู้ที่คาดหวัง"),
    ("2.3",
     "The design of the curriculum is shown to include feedback from stakeholders, especially external stakeholders.",
     "การออกแบบหลักสูตรแสดงให้เห็นว่าได้นำข้อมูลป้อนกลับจากผู้มีส่วนได้ส่วนเสีย โดยเฉพาะภายนอก มาประกอบการพิจารณา"),
    ("2.4",
     "The contribution made by each course in achieving the expected learning outcomes is shown to be clear.",
     "การมีส่วนช่วยของแต่ละรายวิชาต่อการบรรลุผลการเรียนรู้ที่คาดหวังแสดงให้เห็นอย่างชัดเจน"),
    ("2.5",
     "The curriculum to show that all its courses are logically structured, properly sequenced (progression from basic to intermediate to specialised courses), and are integrated.",
     "หลักสูตรแสดงให้เห็นว่าทุกรายวิชามีโครงสร้างเชิงตรรกะ เรียงลำดับอย่างเหมาะสม (จากพื้นฐานสู่ระดับกลางสู่รายวิชาเฉพาะทาง) และมีการบูรณาการ"),
    ("2.6",
     "The curriculum to have option(s) for students to pursue major and/or minor specialisations.",
     "หลักสูตรมีทางเลือกให้ผู้เรียนศึกษาวิชาเอกและ/หรือวิชาโทเฉพาะทาง"),
    ("2.7",
     "The programme to show that its curriculum is reviewed periodically following an established procedure and that it remains up-to-date and relevant to industry.",
     "หลักสูตรแสดงให้เห็นว่ามีการทบทวนหลักสูตรเป็นระยะตามกระบวนการที่กำหนด และยังคงทันสมัยและสอดคล้องกับภาคอุตสาหกรรม"),

    ("3.1",
     "The educational philosophy is shown to be articulated and communicated to all stakeholders. It is also shown to be reflected in the teaching and learning activities.",
     "ปรัชญาการศึกษาแสดงให้เห็นว่าได้รับการกำหนดและสื่อสารแก่ผู้มีส่วนได้ส่วนเสียทุกฝ่าย และสะท้อนอยู่ในกิจกรรมการเรียนการสอน"),
    ("3.2",
     "The teaching and learning activities are shown to allow students to participate responsibly in the learning process.",
     "กิจกรรมการเรียนการสอนแสดงให้เห็นว่าเปิดโอกาสให้ผู้เรียนมีส่วนร่วมอย่างรับผิดชอบในกระบวนการเรียนรู้"),
    ("3.3",
     "The teaching and learning activities are shown to involve active learning by the students.",
     "กิจกรรมการเรียนการสอนแสดงให้เห็นว่ามีการเรียนรู้เชิงรุก (active learning) ของผู้เรียน"),
    ("3.4",
     "The teaching and learning activities are shown to promote learning, learning how to learn, and instilling in students a commitment for life-long learning (e.g., commitment to critical inquiry, information-processing skills, and a willingness to experiment with new ideas and practices).",
     "กิจกรรมการเรียนการสอนแสดงให้เห็นว่าส่งเสริมการเรียนรู้ การเรียนรู้วิธีการเรียนรู้ และปลูกฝังความมุ่งมั่นในการเรียนรู้ตลอดชีวิต (เช่น การสืบเสาะเชิงวิพากษ์ ทักษะการประมวลผลสารสนเทศ และความเต็มใจทดลองแนวคิดและวิธีปฏิบัติใหม่)"),
    ("3.5",
     "The teaching and learning activities are shown to inculcate in students, new ideas, creative thought, innovation, and an entrepreneurial mindset.",
     "กิจกรรมการเรียนการสอนแสดงให้เห็นว่าปลูกฝังแนวคิดใหม่ ความคิดสร้างสรรค์ นวัตกรรม และความเป็นผู้ประกอบการแก่ผู้เรียน"),
    ("3.6",
     "The teaching and learning processes are shown to be continuously improved to ensure their relevance to the needs of industry and are aligned to the expected learning outcomes.",
     "กระบวนการเรียนการสอนแสดงให้เห็นว่าได้รับการปรับปรุงอย่างต่อเนื่องเพื่อให้สอดคล้องกับความต้องการของภาคอุตสาหกรรมและผลการเรียนรู้ที่คาดหวัง"),

    ("4.1",
     "A variety of assessment methods are shown to be used and are shown to be constructively aligned to achieving the expected learning outcomes and the teaching and learning objectives.",
     "มีการใช้วิธีการประเมินที่หลากหลาย และแสดงให้เห็นว่าสอดคล้องเชิงสร้างสรรค์กับการบรรลุผลการเรียนรู้ที่คาดหวังและวัตถุประสงค์การเรียนการสอน"),
    ("4.2",
     "The assessment and assessment-appeal policies are shown to be explicit, communicated to students, and applied consistently.",
     "นโยบายการประเมินและการอุทธรณ์ผลการประเมินแสดงให้เห็นว่าชัดเจน สื่อสารแก่ผู้เรียน และใช้อย่างสม่ำเสมอ"),
    ("4.3",
     "The assessment standards and procedures for student progression and degree completion, are shown to be explicit, communicated to students, and applied consistently.",
     "มาตรฐานและกระบวนการประเมินสำหรับการเลื่อนชั้นและการสำเร็จการศึกษาแสดงให้เห็นว่าชัดเจน สื่อสารแก่ผู้เรียน และใช้อย่างสม่ำเสมอ"),
    ("4.4",
     "The assessment methods are shown to include rubrics, marking schemes, timelines, and regulations, and these are shown to ensure validity, reliability, and fairness in assessment.",
     "วิธีการประเมินแสดงให้เห็นว่ามีเกณฑ์การให้คะแนน (rubric) แนวการให้คะแนน กรอบเวลา และระเบียบปฏิบัติ ซึ่งช่วยประกันความตรง ความเชื่อมั่น และความเป็นธรรมในการประเมิน"),
    ("4.5",
     "The assessment methods are shown to measure the achievement of the expected learning outcomes of the programme and its courses.",
     "วิธีการประเมินแสดงให้เห็นว่าวัดการบรรลุผลการเรียนรู้ที่คาดหวังของหลักสูตรและรายวิชา"),
    ("4.6",
     "Feedback of student assessment is shown to be provided in a timely manner.",
     "การให้ข้อมูลป้อนกลับผลการประเมินแก่ผู้เรียนแสดงให้เห็นว่าดำเนินการอย่างทันท่วงที"),
    ("4.7",
     "The student assessment and its processes are shown to be continuously reviewed and improved to ensure their relevance to the needs of industry and alignment to the expected learning outcomes.",
     "การประเมินผู้เรียนและกระบวนการแสดงให้เห็นว่าได้รับการทบทวนและปรับปรุงอย่างต่อเนื่อง เพื่อความสอดคล้องกับความต้องการของภาคอุตสาหกรรมและผลการเรียนรู้ที่คาดหวัง"),

    ("5.1",
     "The programme to show that academic staff planning (including succession, promotion, re-deployment, termination, and retirement plans) is carried out to ensure that the quality and quantity of the academic staff fulfil the needs for education, research, and service.",
     "หลักสูตรแสดงให้เห็นว่ามีการวางแผนอัตรากำลังบุคลากรสายวิชาการ (รวมถึงการสืบทอดตำแหน่ง การเลื่อนตำแหน่ง การปรับย้าย การเลิกจ้าง และการเกษียณ) เพื่อให้คุณภาพและปริมาณบุคลากรเพียงพอต่อความต้องการด้านการศึกษา การวิจัย และการบริการ"),
    ("5.2",
     "The programme to show that staff workload is measured and monitored to improve the quality of education, research, and service.",
     "หลักสูตรแสดงให้เห็นว่ามีการวัดและติดตามภาระงานของบุคลากรเพื่อยกระดับคุณภาพการศึกษา การวิจัย และการบริการ"),
    ("5.3",
     "The programme to show that the competences of the academic staff are determined, evaluated, and communicated.",
     "หลักสูตรแสดงให้เห็นว่ามีการกำหนด ประเมิน และสื่อสารสมรรถนะของบุคลากรสายวิชาการ"),
    ("5.4",
     "The programme to show that the duties allocated to the academic staff are appropriate to qualifications, experience, and aptitude.",
     "หลักสูตรแสดงให้เห็นว่าการมอบหมายภาระหน้าที่แก่บุคลากรสายวิชาการเหมาะสมกับคุณวุฒิ ประสบการณ์ และความถนัด"),
    ("5.5",
     "The programme to show that promotion of the academic staff is based on a merit system which accounts for teaching, research, and service.",
     "หลักสูตรแสดงให้เห็นว่าการเลื่อนตำแหน่งของบุคลากรสายวิชาการเป็นไปตามระบบคุณธรรมที่คำนึงถึงการสอน การวิจัย และการบริการ"),
    ("5.6",
     "The programme to show that the rights and privileges, benefits, roles and relationships, and accountability of the academic staff, taking into account professional ethics and their academic freedom, are well defined and understood.",
     "หลักสูตรแสดงให้เห็นว่าสิทธิและสิทธิประโยชน์ สวัสดิการ บทบาทและความสัมพันธ์ และความรับผิดชอบของบุคลากรสายวิชาการ โดยคำนึงถึงจรรยาบรรณวิชาชีพและเสรีภาพทางวิชาการ ได้รับการกำหนดและเข้าใจอย่างชัดเจน"),
    ("5.7",
     "The programme to show that the training and developmental needs of the academic staff are systematically identified, and that appropriate training and development activities are implemented to fulfil the identified needs.",
     "หลักสูตรแสดงให้เห็นว่ามีการระบุความต้องการฝึกอบรมและพัฒนาบุคลากรสายวิชาการอย่างเป็นระบบ และจัดกิจกรรมฝึกอบรมและพัฒนาที่เหมาะสมเพื่อตอบสนองความต้องการนั้น"),
    ("5.8",
     "The programme to show that performance management including reward and recognition is implemented to assess academic staff teaching and research quality.",
     "หลักสูตรแสดงให้เห็นว่ามีการบริหารผลการปฏิบัติงาน รวมถึงการให้รางวัลและการยกย่อง เพื่อประเมินคุณภาพการสอนและการวิจัยของบุคลากรสายวิชาการ"),

    ("6.1",
     "The student intake policy, admission criteria, and admission procedures to the programme are shown to be clearly defined, communicated, published, and up-to-date.",
     "นโยบายการรับเข้า เกณฑ์ และกระบวนการรับเข้าศึกษาในหลักสูตรแสดงให้เห็นว่ามีการกำหนดอย่างชัดเจน สื่อสาร เผยแพร่ และทันสมัย"),
    ("6.2",
     "Both short-term and long-term planning of academic and non-academic support services are shown to be carried out to ensure sufficiency and quality of support services for teaching, research, and community service.",
     "มีการวางแผนทั้งระยะสั้นและระยะยาวสำหรับบริการสนับสนุนทั้งด้านวิชาการและไม่ใช่วิชาการ เพื่อประกันความเพียงพอและคุณภาพของบริการสนับสนุนการสอน การวิจัย และการบริการชุมชน"),
    ("6.3",
     "An adequate system is shown to exist for student progress, academic performance, and workload monitoring. Student progress, academic performance, and workload are shown to be systematically recorded and monitored. Feedback to students and corrective actions are made where necessary.",
     "มีระบบที่เพียงพอสำหรับติดตามความก้าวหน้า ผลการเรียน และภาระงานของผู้เรียน โดยมีการบันทึกและติดตามอย่างเป็นระบบ พร้อมให้ข้อมูลป้อนกลับและดำเนินการแก้ไขเมื่อจำเป็น"),
    ("6.4",
     "Co-curricular activities, student competition, and other student support services are shown to be available to improve learning experience and employability.",
     "มีกิจกรรมเสริมหลักสูตร การแข่งขันของผู้เรียน และบริการสนับสนุนอื่น ๆ เพื่อยกระดับประสบการณ์การเรียนรู้และความสามารถในการได้งานทำ"),
    ("6.5",
     "The competences of the support staff rendering student services are shown to be identified for recruitment and deployment. These competences are shown to be evaluated to ensure their continued relevance to stakeholders needs. Roles and relationships are shown to be well-defined to ensure smooth delivery of the services.",
     "มีการระบุสมรรถนะของบุคลากรสายสนับสนุนที่ให้บริการผู้เรียนเพื่อการสรรหาและจัดวางกำลังคน และประเมินสมรรถนะเพื่อให้สอดคล้องกับความต้องการของผู้มีส่วนได้ส่วนเสียอย่างต่อเนื่อง รวมทั้งกำหนดบทบาทและความสัมพันธ์อย่างชัดเจนเพื่อการให้บริการที่ราบรื่น"),
    ("6.6",
     "Student support services are shown to be subjected to evaluation, benchmarking, and enhancement.",
     "บริการสนับสนุนผู้เรียนแสดงให้เห็นว่าได้รับการประเมิน เทียบเคียงสมรรถนะ และพัฒนาให้ดีขึ้น"),

    ("7.1",
     "The physical resources to deliver the curriculum, including equipment, material, and information technology, are shown to be sufficient.",
     "ทรัพยากรกายภาพสำหรับจัดการเรียนการสอน รวมถึงอุปกรณ์ วัสดุ และเทคโนโลยีสารสนเทศ แสดงให้เห็นว่าเพียงพอ"),
    ("7.2",
     "The laboratories and equipment are shown to be up-to-date, readily available, and effectively deployed.",
     "ห้องปฏิบัติการและอุปกรณ์แสดงให้เห็นว่าทันสมัย พร้อมใช้งาน และนำไปใช้อย่างมีประสิทธิภาพ"),
    ("7.3",
     "A digital library is shown to be set-up, in keeping with progress in information and communication technology.",
     "มีการจัดตั้งห้องสมุดดิจิทัลที่สอดคล้องกับความก้าวหน้าของเทคโนโลยีสารสนเทศและการสื่อสาร"),
    ("7.4",
     "The information technology systems are shown to be set up to meet the needs of staff and students.",
     "ระบบเทคโนโลยีสารสนเทศแสดงให้เห็นว่าจัดตั้งขึ้นเพื่อตอบสนองความต้องการของบุคลากรและผู้เรียน"),
    ("7.5",
     "The university is shown to provide a highly accessible computer and network infrastructure that enables the campus community to fully exploit information technology for teaching, research, service, and administration.",
     "มหาวิทยาลัยแสดงให้เห็นว่าจัดให้มีโครงสร้างพื้นฐานคอมพิวเตอร์และเครือข่ายที่เข้าถึงได้สูง เพื่อให้ประชาคมใช้ประโยชน์จากเทคโนโลยีสารสนเทศอย่างเต็มที่ในการสอน การวิจัย การบริการ และการบริหาร"),
    ("7.6",
     "The environmental, health, and safety standards and access for people with special needs are shown to be defined and implemented.",
     "มาตรฐานด้านสิ่งแวดล้อม สุขภาพ และความปลอดภัย รวมถึงการเข้าถึงสำหรับผู้มีความต้องการพิเศษ แสดงให้เห็นว่าได้รับการกำหนดและนำไปปฏิบัติ"),
    ("7.7",
     "The university is shown to provide a physical, social, and psychological environment that is conducive for education, research, and personal well-being.",
     "มหาวิทยาลัยแสดงให้เห็นว่าจัดสภาพแวดล้อมทางกายภาพ สังคม และจิตใจที่เอื้อต่อการศึกษา การวิจัย และความเป็นอยู่ที่ดีของบุคคล"),
    ("7.8",
     "The competences of the support staff rendering services related to facilities are shown to be identified and evaluated to ensure that their skills remain relevant to stakeholder needs.",
     "สมรรถนะของบุคลากรสายสนับสนุนที่ให้บริการด้านสิ่งอำนวยความสะดวกแสดงให้เห็นว่าได้รับการระบุและประเมิน เพื่อให้ทักษะสอดคล้องกับความต้องการของผู้มีส่วนได้ส่วนเสีย"),
    ("7.9",
     "The quality of the facilities (library, laboratory, IT, and student services) are shown to be subjected to evaluation and enhancement.",
     "คุณภาพของสิ่งอำนวยความสะดวก (ห้องสมุด ห้องปฏิบัติการ ไอที และบริการผู้เรียน) แสดงให้เห็นว่าได้รับการประเมินและพัฒนาให้ดีขึ้น"),

    ("8.1",
     "The pass rate, dropout rate, and average time to graduate are shown to be established, monitored, and benchmarked for improvement.",
     "อัตราการสำเร็จการศึกษา อัตราการออกกลางคัน และระยะเวลาเฉลี่ยในการสำเร็จการศึกษา แสดงให้เห็นว่ามีการกำหนด ติดตาม และเทียบเคียงเพื่อการพัฒนา"),
    ("8.2",
     "Employability as well as self-employment, entrepreneurship, and advancement to further studies, are shown to be established, monitored, and benchmarked for improvement.",
     "การได้งานทำ การประกอบอาชีพอิสระ การเป็นผู้ประกอบการ และการศึกษาต่อ แสดงให้เห็นว่ามีการกำหนด ติดตาม และเทียบเคียงเพื่อการพัฒนา"),
    ("8.3",
     "Research and creative work output and activities carried out by the academic staff and students, are shown to be established, monitored, and benchmarked for improvement.",
     "ผลงานวิจัยและงานสร้างสรรค์ รวมถึงกิจกรรมที่ดำเนินการโดยบุคลากรสายวิชาการและผู้เรียน แสดงให้เห็นว่ามีการกำหนด ติดตาม และเทียบเคียงเพื่อการพัฒนา"),
    ("8.4",
     "Data are provided to show directly the achievement of the programme outcomes, which are established and monitored.",
     "มีการจัดเตรียมข้อมูลเพื่อแสดงการบรรลุผลลัพธ์ของหลักสูตรโดยตรง ซึ่งได้รับการกำหนดและติดตาม"),
    ("8.5",
     "Satisfaction level of the various stakeholders are shown to be established, monitored, and benchmarked for improvement.",
     "ระดับความพึงพอใจของผู้มีส่วนได้ส่วนเสียกลุ่มต่าง ๆ แสดงให้เห็นว่ามีการกำหนด ติดตาม และเทียบเคียงเพื่อการพัฒนา"),
]


def esc(s: str) -> str:
    return s.replace('"', '\\"')


# --- write criteria files ---
for code, en, th in CRITERIA:
    p = CRIT_DIR / f"c{code}.md"
    p.write_text(
        f'---\n'
        f'code: {code}\n'
        f'title_en: "{esc(en)}"\n'
        f'title_th: "{esc(th)}"\n'
        f'intro_en: ""\n'
        f'intro_th: ""\n'
        f'order: {code}\n'
        f'---\n',
        encoding="utf-8",
    )

# --- write sub-criteria files ---
for code, en, th in SUBS:
    crit = int(code.split(".")[0])
    p = SUB_DIR / f"s{code.replace('.', '-')}.md"
    p.write_text(
        f'---\n'
        f'code: "{code}"\n'
        f'criterion: c{crit}\n'
        f'requirement_en: "{esc(en)}"\n'
        f'requirement_th: "{esc(th)}"\n'
        f'narrative_th: ""\n'
        f'narrative_en: ""\n'
        f'pdca: none\n'
        f'responsible: ""\n'
        f'rating: 0\n'
        f'target: 4\n'
        f'evidence: []\n'
        f'---\n',
        encoding="utf-8",
    )

# distribution check
from collections import Counter
dist = Counter(int(c.split(".")[0]) for c, _, _ in SUBS)
print("criteria files:", len(CRITERIA))
print("subcriteria files:", len(SUBS))
print("distribution:", dict(sorted(dist.items())))
assert len(SUBS) == 53, "expected 53 sub-criteria"
assert dict(sorted(dist.items())) == {1: 5, 2: 7, 3: 6, 4: 7, 5: 8, 6: 6, 7: 9, 8: 5}
print("OK: 53 sub-criteria across 8 criteria")
