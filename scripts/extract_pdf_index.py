from pathlib import Path
import json, re, fitz, pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "PDF_KNOWLEDGE"
OUT = ROOT / "extraction-output"
OUT.mkdir(exist_ok=True)

BOOKS = [
    ("03-sgk-toan-3-tap-mot.pdf", "Toán 3 - Tập 1", "vie"),
    ("03-sgk-toan-3-tap-hai.pdf", "Toán 3 - Tập 2", "vie"),
    ("03-sgk-tieng-viet-3-tap-mot.pdf", "Tiếng Việt 3 - Tập 1", "vie"),
    ("03-sgk-tieng-viet-3-tap-hai.pdf", "Tiếng Việt 3 - Tập 2", "vie"),
    ("03-sgk-tieng-anh-3-tap-1-global-success.pdf", "Tiếng Anh 3 Global Success - Tập 1", "eng"),
    ("03-sgk-tieng-anh-3-tap-2-global-success.pdf", "Tiếng Anh 3 Global Success - Tập 2", "eng"),
]
manifest = []
heading_re = re.compile(r"(?i)^(?:bài\s+\d+|tuần\s+\d+|unit\s+\d+|review\s+\d+|starter|chủ đề\s+\d+|\d+\.\s+\S.{2,})")

for filename, label, lang in BOOKS:
    path = SOURCE / filename
    if not path.exists():
        raise FileNotFoundError(f"Thiếu tệp nguồn: {path}")
    doc = fitz.open(path)
    blocks = []
    index = []
    empty_pages = []
    ocr_pages = 0
    for i, page in enumerate(doc):
        text = page.get_text("text", sort=True)
        text = text.replace("\x00", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        used_ocr = False
        if len(text) < 30:
            used_ocr = True
            pix = page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False)
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(
                image, lang=lang, config="--psm 6", timeout=60
            )
            text = text.replace("\x00", " ")
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r"\n{3,}", "\n\n", text).strip()
            ocr_pages += 1
        if len(text) < 30:
            empty_pages.append(i + 1)
        lines = [x.strip() for x in text.splitlines() if x.strip()]
        candidates = [x for x in lines if heading_re.match(x)]
        index.append({
            "pdf_page": i + 1,
            "chars": len(text),
            "ocr_used": used_ocr,
            "heading_candidates": candidates[:12],
            "preview": " | ".join(lines[:8])[:900]
        })
        blocks.append(f"\n\n===== PDF PAGE {i + 1} =====\n{text}")
        if (i + 1) % 25 == 0:
            print(f"{label}: đã xử lý {i + 1}/{len(doc)} trang")
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
        "ocr_pages": ocr_pages,
        "pages_with_little_or_no_text_after_ocr": empty_pages,
        "text_file": f"{stem}.txt",
        "page_index_file": f"{stem}.page-index.json"
    })
    print(f"{label}: {len(doc)} trang; {sum(x['chars'] for x in index):,} ký tự; OCR {ocr_pages} trang; còn ít/không có chữ: {len(empty_pages)} trang")
    doc.close()

(OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("Đã OCR vào artifact tạm; không đưa toàn văn SGK vào website công khai.")
