# -*- coding: utf-8 -*-
"""
Parse คำอธิบายรายวิชา (วิชาเอก ป.ตรี) จาก มคอ.2 ที่แปลงเป็น mko2_clean.txt
แล้วเติม desc_th / desc_en ลงในไฟล์ src/content/courses/b-*.md
จับคู่ด้วยรหัสวิชา (ไม่แตะชื่อวิชา)
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLEAN = ROOT / "scripts" / "mko2_clean.txt"
OUT = ROOT / "src" / "content" / "courses"

lines = CLEAN.read_text(encoding="utf-8").splitlines()
# section วิชาเอก ป.ตรี
START, END = 2028 - 1, 2427  # 0-indexed slice
section = lines[START:END]

THAI = re.compile(r"[฀-๿]")
LATIN = re.compile(r"[A-Za-z]")
CODE = re.compile(r"^\d{4} \d{3}$")
CREDIT = re.compile(r"^\d+\(\d+-\d+-\d+\)")
# section headers / structural lines that must not be treated as description
HEADER = re.compile(r"^\d+(\.\d+)*\s*\)|ไม่น้อยกว่า|^หมวดวิชา|^\d+\)\s*หมวด")


def is_thai(s):
    # classify by ratio so a stray Thai char in an English line doesn't flip it
    return len(THAI.findall(s)) >= len(LATIN.findall(s))


def is_header(s):
    return bool(HEADER.search(s))


# split section into blocks by code line
blocks = []
cur = None
for ln in section:
    s = ln.strip()
    if CODE.match(s):
        if cur:
            blocks.append(cur)
        cur = {"code": s, "rest": []}
    elif cur is not None:
        cur["rest"].append(s)
if cur:
    blocks.append(cur)

result = {}  # code -> (desc_th, desc_en)
for b in blocks:
    rest = b["rest"]
    # find credits line index
    ci = next((i for i, x in enumerate(rest) if CREDIT.match(x)), None)
    if ci is None:
        continue
    post = [x for x in rest[ci + 1:] if x and not is_header(x)]  # drop blanks + headers
    # group into alternating language runs
    runs = []  # (lang, [lines])
    for x in post:
        lang = "th" if is_thai(x) else "en"
        if runs and runs[-1][0] == lang:
            runs[-1][1].append(x)
        else:
            runs.append((lang, [x]))
    th_runs = [r[1] for r in runs if r[0] == "th"]
    en_runs = [r[1] for r in runs if r[0] == "en"]
    desc_th = " ".join(th_runs[-1]) if th_runs else ""
    desc_en = " ".join(en_runs[-1]) if en_runs else ""
    # normalize whitespace
    desc_th = re.sub(r"\s+", " ", desc_th).strip()
    desc_en = re.sub(r"\s+", " ", desc_en).strip()
    result[b["code"]] = (desc_th, desc_en)

print(f"parsed {len(result)} course descriptions from มคอ.2")

# update b-*.md files
updated, missing = [], []
files = sorted(OUT.glob("b-*.md"))
for f in files:
    text = f.read_text(encoding="utf-8")
    m = re.search(r'^code:\s*"([^"]+)"', text, re.M)
    if not m:
        continue
    code = m.group(1).strip()
    if code not in result:
        missing.append((f.name, code))
        continue
    desc_th, desc_en = result[code]

    def esc(s):
        return s.replace("\\", "\\\\").replace('"', '\\"')

    # remove existing desc lines then re-insert before closing ---
    body = text
    body = re.sub(r'^desc_th:.*\n', '', body, flags=re.M)
    body = re.sub(r'^desc_en:.*\n', '', body, flags=re.M)
    parts = body.split('---\n')
    # frontmatter is parts[1]
    fm = parts[1].rstrip('\n')
    fm += f'\ndesc_th: "{esc(desc_th)}"\n'
    if desc_en:
        fm += f'desc_en: "{esc(desc_en)}"\n'
    rest = '---\n'.join(parts[2:])
    new = '---\n' + fm + '---\n' + (rest if rest else '')
    f.write_text(new, encoding="utf-8")
    updated.append(code)

print(f"\nupdated {len(updated)} files")
if missing:
    print(f"\n!! {len(missing)} files have code NOT found in มคอ.2 section:")
    for name, code in missing:
        print(f"   {name}  code={code}")
