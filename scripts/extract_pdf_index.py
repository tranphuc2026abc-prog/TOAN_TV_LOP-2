from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
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
heading_re = re.compile(r"(?i)^(?:bài\s+\d+|tuần\s+\d+|unit\s+\d+|review\s+\d+|starter|chủ đề\s+\d+|\d+\.\s+\S.{2,})")

def process_chunk(args):
    filename, label, lang, start, end = args
    path = SOURCE / filename
    doc = fitz.open(path)
    results = []
    try:
        for i in range(start, end):
            page = doc.load_page(i)
            text = page.get_text("text", sort=True)
            text = text.replace("\x00", " ")
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r"\n{3,}", "\n\n", text).strip()
            used_ocr = False
            ocr_error = None
            if len(text) < 30:
                used_ocr = True
                try:
                    pix = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False)
                    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    text = pytesseract.image_to_string(image, lang=lang, config="--psm 6", timeout=45)
                except RuntimeError:
                    try:
                        pix = page.get_pixmap(matrix=fitz.Matrix(1.0, 1.0), alpha=False)
                        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                        text = pytesseract.image_to_string(image, lang=lang, config="--psm 11", timeout=45)
                    except RuntimeError as exc:
                        text = ""
                        ocr_error = str(exc)[:200]
                text = text.replace("\x00", " ")
                text = re.sub(r"[ \t]+", " ", text)
                text = re.sub(r"\n{3,}", "\n\n", text).strip()
            lines = [x.strip() for x in text.splitlines() if x.strip()]
            candidates = [x for x in lines if heading_re.match(x)]
            results.append({
                "pdf_page": i + 1,
                "text": text,
                "chars": len(text),
                "ocr_used": used_ocr,
                "ocr_error": ocr_error,
                "heading_candidates": candidates[:12],
                "preview": " | ".join(lines[:8])[:900]
            })
    finally:
        doc.close()
    return label, results

manifest = []
for filename, label, lang in BOOKS:
    path = SOURCE / filename
    if not path.exists():
        raise FileNotFoundError(f"Thiếu tệp nguồn: {path}")
    with fitz.open(path) as doc:
        total_pages = len(doc)
    chunk_size = 15
    chunks = [
        (filename, label, lang, start, min(start + chunk_size, total_pages))
        for start in range(0, total_pages, chunk_size)
    ]
    results = []
    print(f"Bắt đầu OCR {label}: {total_pages} trang, chia {len(chunks)} nhóm")
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(process_chunk, c) for c in chunks]
        for future in as_completed(futures):
            _, batch = future.result()
            results.extend(batch)
            print(f"{label}: hoàn thành {len(results)}/{total_pages} trang")
    results.sort(key=lambda x: x["pdf_page"])
    stem = path.stem
    blocks = [f"\n\n===== PDF PAGE {x['pdf_page']} =====\n{x['text']}" for x in results]
    (OUT / f"{stem}.txt").write_text("\n".join(blocks), encoding="utf-8")
    page_index = [{k: v for k, v in x.items() if k != "text"} for x in results]
    (OUT / f"{stem}.page-index.json").write_text(
        json.dumps({"book": label, "file": filename, "pages": page_index}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    empty_pages = [x["pdf_page"] for x in results if x["chars"] < 30]
    ocr_pages = sum(1 for x in results if x["ocr_used"])
    manifest.append({
        "book": label,
        "file": filename,
        "pdf_pages": total_pages,
        "extracted_characters": sum(x["chars"] for x in results),
        "ocr_pages": ocr_pages,
        "pages_with_little_or_no_text_after_ocr": empty_pages,
        "text_file": f"{stem}.txt",
        "page_index_file": f"{stem}.page-index.json"
    })
    print(f"{label}: {total_pages} trang; {sum(x['chars'] for x in results):,} ký tự; OCR {ocr_pages} trang; còn ít/không có chữ: {len(empty_pages)}")
(OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("Đã OCR vào artifact tạm; không đưa toàn văn SGK vào website công khai.")
