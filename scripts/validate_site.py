from pathlib import Path
import json, re, subprocess, tempfile

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")
data = json.loads((root / "data/CHUONG_TRINH_LOP_3_FULL.json").read_text(encoding="utf-8"))
lessons = data.get("lessons", [])
ids = [x.get("id") for x in lessons]
assert len(lessons) == 168, f"Expected 168 curriculum entries, got {len(lessons)}"
assert len(ids) == len(set(ids)), "Duplicate lesson IDs found"
counts = {
    "toan": sum(x.get("subject") == "toan" for x in lessons),
    "tv": sum(x.get("subject") == "tv" for x in lessons),
    "ta": sum(x.get("subject") == "ta" for x in lessons),
}
assert counts == {"toan": 81, "tv": 62, "ta": 25}, f"Unexpected subject counts: {counts}"

scripts = re.findall(r"<script(?:\s[^>]*)?>([\s\S]*?)</script\s*>", html, flags=re.I)
inline = [s for s in scripts if s.strip()]
assert inline, "No inline JavaScript found"
with tempfile.TemporaryDirectory() as tmp:
    for i, source in enumerate(inline, 1):
        path = Path(tmp) / f"inline-{i}.js"
        path.write_text(source, encoding="utf-8")
        subprocess.run(["node", "--check", str(path)], check=True)
print(f"Validated {len(lessons)} curriculum entries: {counts}; JavaScript syntax OK.")
