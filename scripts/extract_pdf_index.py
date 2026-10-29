from pathlib import Path
import json, re, fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "PDF_KNOWLEDGE"
OUT = ROOT / "extraction-output"
OUT.mkdir(exist_ok=True)

BOOKS = [
    ("03-sgk-toan-3-tap-mot.pdf", "Toán 3 - Tập 1"),
    ("03-sgk-toan-3-tap-hai.pdf", "Toán 3 - Tập 2"),
    ("03-sgk-tieng-viet-3-tap-mot.pdf", "Tiếng Việt 3 - Tập 1"),
    ("03-sgk-tieng-viet-3-tap-hai.pdf", "Tiếng Việt 3 - Tập 2"),
    ("03-sgk-tieng-anh-3-tap-1-global-success.pdf", "Tiếng Anh 3 Global Success - Tập 1"),
    ("03-sgk-tieng-anh-3-tap-2-global-success.pdf", "Tiếng Anh 3 Global Success - Tập 2"),
]
manifest = []
heading_re = re.compile(r"(?i)^(?:bài\s+\d+|tuần\s+\d+|unit\s+\d+|review\s+\d+|starter|chủ đề\s+\d+|\d+\.\s+\S.{2,})")

for filename, label in BOOKS:
    path = SOURCE / filename
    if not path.exists():
        raise FileNotFoundError(f"Thiếu tệp nguồn: {path}")
    doc = fitz.open(path)
    blocks = []
    index = []
    empty_pages = []
    for i, page in enumerate(doc):
        text = page.get_text("text", sort=True)
        text = text.replace("\x00", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if len(text) < 30:
            empty_pages.append(i + 1)
        lines = [x.strip() for x in text.splitlines() if x.strip()]
        candidates = [x for x in lines if heading_re.match(x)]
        index.append({
            "pdf_page": i + 1,
            "chars": len(text),
            "heading_candidates": candidates[:12],
            "preview": " | ".join(lines[:8])[:900]
        })
        blocks.append(f"\n\n===== PDF PAGE {i + 1} =====\n{text}")
    stem = path.stem
    (OUT / f"{stem}.txt").write_text("\n".join(blocks), encoding="utf-8")
    (OUT / f"{stem}.page-index.json").write_text(
        json.dumps({"book": label, "file": filename, "pages": index}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    manifest.append({
        "book": label,
        "file": filename,
        "pdf_pages": len(doc),
        "extracted_characters": sum(x["chars"] for x in index),
        "pages_with_little_or_no_text": empty_pages,
        "text_file": f"{stem}.txt",
        "page_index_file": f"{stem}.page-index.json"
    })
    print(f"{label}: {len(doc)} trang PDF; {sum(x['chars'] for x in index):,} ký tự; {len(empty_pages)} trang ít/không có text")
    doc.close()

(OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("Đã trích xuất văn bản vào artifact tạm; không đưa toàn văn SGK vào website công khai.")
