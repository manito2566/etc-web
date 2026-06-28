# -*- coding: utf-8 -*-
"""
Parse คำอธิบายรายวิชา (ป.โท) จาก มคอ.2 PDF (ปร.ด. เทคโนโลยีและสื่อสารการศึกษา)
ฟอนต์ THSarabunPSK ใช้ Private Use Area สำหรับวรรณยุกต์ -> remap กลับเป็น Unicode
เติม desc_th / desc_en ลงในไฟล์ src/content/courses/d-*.md (จับคู่ด้วยรหัสวิชา)
"""
import re, pathlib, pdfplumber

ROOT = pathlib.Path(__file__).resolve().parents[1]
PDF = ROOT / "scripts" / "phd.pdf"
OUT = ROOT / "src" / "content" / "courses"
PAGES = range(40, 46)  # หมวด 3.1.5 คำอธิบายรายวิชา

PUA = {0xf700:'่',0xf701:'่',0xf702:'้',0xf703:'๊',0xf704:'๋',0xf705:'์',
       0xf706:'็',0xf707:'็',0xf708:'๊',0xf709:'๋',0xf70a:'่',0xf70b:'้',
       0xf70c:'๊',0xf70d:'๋',0xf70e:'์',0xf70f:'็',0xf710:'ั',0xf711:'ิ',
       0xf712:'ี',0xf713:'ึ',0xf714:'ื'}

def fix(s):
    return ''.join(PUA.get(ord(c), c) for c in s)

THAI = re.compile(r"[฀-๿]")
LATIN = re.compile(r"[A-Za-z]")
CODE = re.compile(r"^\d{4} \d{3}\b")
CREDIT = re.compile(r"\d+\(\d+-\d+-\d+\)")
HEADER = re.compile(r"^\d+(\.\d+)*\s*\)|ไม่น้อยกว่า|^หมวดวิชา")

def is_thai(s):
    return len(THAI.findall(s)) >= len(LATIN.findall(s))

def is_skip(s):
    if not s: return True
    if s.isdigit(): return True            # page number
    if s.startswith("====="): return True  # page marker
    if HEADER.search(s): return True
    if "คำอธิบายรายวิชา" in s: return True
    return False

# extract & clean lines
lines = []
with pdfplumber.open(PDF) as pdf:
    for i in PAGES:
        t = fix(pdf.pages[i].extract_text(use_text_flow=True) or "")
        for ln in t.split("\n"):
            lines.append(ln.strip())
lines = [l for l in lines if not is_skip(l)]

# split into blocks at course-code lines
blocks, cur = [], None
for l in lines:
    if CODE.match(l):
        if cur: blocks.append(cur)
        cur = {"code": l[:8], "lines": [l]}
    elif cur is not None:
        cur["lines"].append(l)
if cur: blocks.append(cur)

result = {}
for b in blocks:
    body = b["lines"]
    ci = next((i for i, x in enumerate(body) if CREDIT.search(x)), None)
    if ci is None:
        continue
    post = body[ci + 1:]
    runs = []
    for x in post:
        lang = "th" if is_thai(x) else "en"
        if runs and runs[-1][0] == lang:
            runs[-1][1].append(x)
        else:
            runs.append((lang, [x]))
    th = [r[1] for r in runs if r[0] == "th"]
    en = [r[1] for r in runs if r[0] == "en"]
    desc_th = re.sub(r"\s+", " ", " ".join(th[-1])).strip() if th else ""
    desc_en = re.sub(r"\s+", " ", " ".join(en[-1])).strip() if en else ""
    result[b["code"]] = (desc_th, desc_en)

print(f"parsed {len(result)} descriptions")

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

updated, missing = [], []
for f in sorted(OUT.glob("d-*.md")):
    text = f.read_text(encoding="utf-8")
    m = re.search(r'^code:\s*"([^"]+)"', text, re.M)
    code = m.group(1).strip()
    if code not in result:
        missing.append((f.name, code)); continue
    desc_th, desc_en = result[code]
    body = re.sub(r'^desc_th:.*\n', '', text, flags=re.M)
    body = re.sub(r'^desc_en:.*\n', '', body, flags=re.M)
    parts = body.split('---\n')
    fm = parts[1].rstrip('\n') + f'\ndesc_th: "{esc(desc_th)}"\n'
    if desc_en:
        fm += f'desc_en: "{esc(desc_en)}"\n'
    rest = '---\n'.join(parts[2:])
    f.write_text('---\n' + fm + '---\n' + rest, encoding="utf-8")
    updated.append(code)

print(f"updated {len(updated)} files")
if missing:
    print(f"!! {len(missing)} not found in section:")
    for n, c in missing: print("  ", n, c)
