import streamlit as st
import random
from datetime import datetime

# ══════════════════════════════════════════════════════════════════════════════
# CẤU HÌNH TRANG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="🌟 Siêu Sao Lớp 2",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
# DỮ LIỆU TỪ VỰNG – TIẾNG ANH (mảng lớn cho sinh câu hỏi tự động)
# ══════════════════════════════════════════════════════════════════════════════
ENG_VOCAB = {
    "colors": [
        ("red","đỏ"),("blue","xanh dương"),("green","xanh lá"),("yellow","vàng"),
        ("pink","hồng"),("purple","tím"),("orange","cam"),("white","trắng"),
        ("black","đen"),("brown","nâu"),("gray","xám"),("gold","vàng kim"),
    ],
    "animals": [
        ("cat","mèo"),("dog","chó"),("bird","chim"),("fish","cá"),
        ("cow","bò"),("pig","lợn"),("chicken","gà"),("duck","vịt"),
        ("horse","ngựa"),("elephant","voi"),("tiger","hổ"),("lion","sư tử"),
        ("rabbit","thỏ"),("frog","ếch"),("snake","rắn"),("bear","gấu"),
        ("monkey","khỉ"),("butterfly","bướm"),("bee","ong"),("ant","kiến"),
    ],
    "family": [
        ("mother","mẹ"),("father","bố"),("sister","chị/em gái"),("brother","anh/em trai"),
        ("grandmother","bà"),("grandfather","ông"),("baby","em bé"),
        ("aunt","cô/dì"),("uncle","chú/bác"),("family","gia đình"),
        ("girl","con gái"),("boy","con trai"),("child","đứa trẻ"),
    ],
    "school": [
        ("book","sách"),("pen","bút"),("pencil","bút chì"),("ruler","thước"),
        ("bag","cặp sách"),("desk","bàn"),("chair","ghế"),("board","bảng"),
        ("eraser","tẩy"),("notebook","vở"),("crayon","bút màu"),("scissors","kéo"),
        ("glue","keo"),("paper","giấy"),("teacher","giáo viên"),("student","học sinh"),
    ],
    "body": [
        ("head","đầu"),("eye","mắt"),("nose","mũi"),("mouth","miệng"),
        ("ear","tai"),("hand","tay"),("foot","chân"),("hair","tóc"),
        ("finger","ngón tay"),("leg","chân"),("arm","cánh tay"),("back","lưng"),
        ("face","khuôn mặt"),("tooth","răng"),("lip","môi"),("shoulder","vai"),
    ],
    "food": [
        ("rice","cơm"),("bread","bánh mì"),("egg","trứng"),("milk","sữa"),
        ("apple","táo"),("banana","chuối"),("orange","cam"),("mango","xoài"),
        ("water","nước"),("cake","bánh"),("fish","cá"),("meat","thịt"),
        ("vegetable","rau"),("soup","canh"),("noodle","mì"),("fruit","hoa quả"),
    ],
    "numbers": [
        ("one","1"),("two","2"),("three","3"),("four","4"),("five","5"),
        ("six","6"),("seven","7"),("eight","8"),("nine","9"),("ten","10"),
        ("eleven","11"),("twelve","12"),("twenty","20"),("thirty","30"),("hundred","100"),
    ],
    "greetings": [
        ("hello","xin chào"),("goodbye","tạm biệt"),("thank you","cảm ơn"),
        ("sorry","xin lỗi"),("please","làm ơn"),("yes","có/vâng"),("no","không"),
        ("good morning","chào buổi sáng"),("good night","chúc ngủ ngon"),
        ("how are you","bạn khỏe không"),("I am fine","tôi khỏe"),
        ("what is your name","tên bạn là gì"),("my name is","tên tôi là"),
    ],
}

# ══════════════════════════════════════════════════════════════════════════════
# DỮ LIỆU TỪ VỰNG – TIẾNG VIỆT (mảng lớn cho sinh câu hỏi tự động)
# ══════════════════════════════════════════════════════════════════════════════
VIET_VOCAB = {
    "chinh_ta_tr_ch": [
        ("trời","giời"),("trâu","châu"),("trường","chường"),("trăng","chăng"),
        ("trong","chong"),("trước","chước"),("trái","chái"),("trắng","chắng"),
        ("trẻ","chẻ"),("tròn","chòn"),("trung","chung"),("trốn","chốn"),
    ],
    "chinh_ta_s_x": [
        ("sách","xách"),("sân","xân"),("sáng","xáng"),("sông","xông"),
        ("suối","xuối"),("sao","xao"),("siêu","xiêu"),("sơn","xơn"),
        ("sữa","xữa"),("số","xố"),("sung","xung"),("sẽ","xẽ"),
    ],
    "chinh_ta_r_d_gi": [
        ("rau","dau","giau"),("ra","da","gia"),("rộng","dộng","giộng"),
        ("rừng","dừng","giừng"),("ròng","dòng","giòng"),("rẻ","dẻ","giẻ"),
    ],
    "dong_nghia": [
        ("vui","hạnh phúc"),("buồn","đau lòng"),("to","lớn"),("bé","nhỏ"),
        ("đẹp","xinh"),("xấu","khó coi"),("nhanh","mau"),("chậm","thong thả"),
        ("nhà","ngôi nhà"),("bạn","người bạn"),("thầy","thầy giáo"),
        ("học","ôn"),("ăn","dùng bữa"),("ngủ","nghỉ ngơi"),
    ],
    "trai_nghia": [
        ("ngày","đêm"),("to","bé"),("cao","thấp"),("nóng","lạnh"),
        ("sáng","tối"),("mở","đóng"),("nhanh","chậm"),("vui","buồn"),
        ("đẹp","xấu"),("mới","cũ"),("dài","ngắn"),("nặng","nhẹ"),
        ("rộng","hẹp"),("đúng","sai"),("thật","giả"),("khỏe","yếu"),
    ],
    "danh_tu": [
        ("bàn","đồ vật"),("ghế","đồ vật"),("sách","đồ vật"),("bút","đồ vật"),
        ("cô giáo","người"),("bạn bè","người"),("học sinh","người"),("mẹ","người"),
        ("trường học","nơi chốn"),("nhà","nơi chốn"),("sân chơi","nơi chốn"),("vườn","nơi chốn"),
        ("con mèo","con vật"),("con chó","con vật"),("con gà","con vật"),("con cá","con vật"),
    ],
    "cau_hoi": [
        ("Ai?","người"),("Cái gì?","đồ vật"),("Ở đâu?","nơi chốn"),
        ("Khi nào?","thời gian"),("Tại sao?","lý do"),("Như thế nào?","cách thức"),
        ("Bao nhiêu?","số lượng"),("Làm gì?","hành động"),
    ],
}

# ══════════════════════════════════════════════════════════════════════════════
# MODULE SINH CÂU HỎI – TOÁN HỌC
# ══════════════════════════════════════════════════════════════════════════════
def _make_mcq(q, ans, distractors, explain):
    """Tạo câu MCQ từ đáp án đúng và danh sách distractor."""
    opts = [str(ans)] + [str(d) for d in distractors[:3]]
    random.shuffle(opts)
    return {
        "type": "mcq",
        "q": q,
        "opts": opts,
        "ans": opts.index(str(ans)),
        "explain": explain,
    }

def _make_fill(q, ans, explain):
    return {"type": "fill_blank", "q": q, "ans_text": str(ans), "explain": explain}


def generate_math_addition(num_qs=10):
    """Phép cộng có nhớ – sinh ngẫu nhiên hàng nghìn tổ hợp."""
    qs = []
    for i in range(num_qs):
        b = random.randint(3, 9)
        a_unit = random.randint(10 - b + 1, 9)
        a_tens = random.randint(1, 8) * 10
        a = a_tens + a_unit
        ans = a + b
        remainder = b - (10 - a_unit)
        explain = (
            f"📝 Bước 1 – Tách để tròn chục: {a} + {10 - a_unit} = {a_tens + 10}\n"
            f"📝 Bước 2 – Cộng phần còn lại: {a_tens + 10} + {remainder} = {ans}\n"
            f"✅ Đáp số: {a} + {b} = {ans}"
        )
        if i % 3 == 2:
            qs.append(_make_fill(f"Tính: {a} + {b} = ___", ans, explain))
        else:
            qs.append(_make_mcq(f"{a} + {b} = ?", ans,
                                [ans - 1, ans + 1, ans + 10], explain))
    return qs


def generate_math_subtraction(num_qs=10):
    """Phép trừ có nhớ – sinh ngẫu nhiên."""
    qs = []
    for i in range(num_qs):
        a_unit = random.randint(1, 8)
        a_tens = random.randint(2, 9) * 10
        a = a_tens + a_unit
        b = random.randint(a_unit + 1, 9)
        ans = a - b
        explain = (
            f"📝 Bước 1 – Mượn 1 chục: {a_tens} - 10 = {a_tens - 10}, thêm 10 vào đơn vị: {a_unit} + 10 = {a_unit + 10}\n"
            f"📝 Bước 2 – Trừ đơn vị: {a_unit + 10} - {b} = {a_unit + 10 - b}\n"
            f"📝 Bước 3 – Ghép kết quả: {a_tens - 10} + {a_unit + 10 - b} = {ans}\n"
            f"✅ Đáp số: {a} - {b} = {ans}"
        )
        if i % 3 == 2:
            qs.append(_make_fill(f"Tính: {a} - {b} = ___", ans, explain))
        else:
            qs.append(_make_mcq(f"{a} - {b} = ?", ans,
                                [ans - 1, ans + 1, ans - 10], explain))
    return qs


def generate_math_comparison(num_qs=10):
    """So sánh số – sinh ngẫu nhiên."""
    qs = []
    modes = ["sign", "largest", "smallest", "next", "prev"]
    for _ in range(num_qs):
        mode = random.choice(modes)
        if mode == "sign":
            a = random.randint(10, 99)
            b = random.randint(10, 99)
            while a == b:
                b = random.randint(10, 99)
            ans = ">" if a > b else "<"
            explain = f"📝 So sánh hàng chục trước: {a//10} {'>' if a > b else '<'} {b//10} → {a} {ans} {b} ✔"
            qs.append(_make_mcq(f"Điền dấu: {a} ___ {b}",
                                ans, ["<" if ans == ">" else ">", "=", "≥"], explain))
        elif mode == "largest":
            nums = random.sample(range(10, 99), 4)
            ans = max(nums)
            explain = f"📝 So sánh từ lớn đến bé: {sorted(nums, reverse=True)} → Lớn nhất là {ans} ✔"
            qs.append(_make_mcq(f"Số nào lớn nhất: {', '.join(map(str, nums))}?",
                                ans, [n for n in nums if n != ans], explain))
        elif mode == "smallest":
            nums = random.sample(range(10, 99), 4)
            ans = min(nums)
            explain = f"📝 So sánh từ nhỏ đến lớn: {sorted(nums)} → Nhỏ nhất là {ans} ✔"
            qs.append(_make_mcq(f"Số nào nhỏ nhất: {', '.join(map(str, nums))}?",
                                ans, [n for n in nums if n != ans], explain))
        elif mode == "next":
            a = random.randint(10, 98)
            ans = a + 1
            explain = f"📝 Số liền sau = số đó + 1 → {a} + 1 = {ans} ✔"
            qs.append(_make_mcq(f"Số liền sau của {a} là?",
                                ans, [a - 1, a + 2, a - 2], explain))
        else:
            a = random.randint(11, 99)
            ans = a - 1
            explain = f"📝 Số liền trước = số đó − 1 → {a} − 1 = {ans} ✔"
            qs.append(_make_mcq(f"Số liền trước của {a} là?",
                                ans, [a + 1, a - 2, a + 2], explain))
    return qs


def generate_math_measurement(num_qs=10):
    """Đo lường – sinh ngẫu nhiên."""
    qs = []
    conversions = [
        ("dm", "cm", 10), ("m", "dm", 10), ("m", "cm", 100),
        ("kg", "g", 1000), ("l", "dl", 10),
    ]
    for _ in range(num_qs):
        unit_from, unit_to, factor = random.choice(conversions)
        val = random.randint(1, 9)
        ans = val * factor
        explain = f"📝 {val} {unit_from} = {val} × {factor} = {ans} {unit_to} ✔"
        q_type = random.choice(["a_to_b", "b_to_a"])
        if q_type == "a_to_b":
            qs.append(_make_mcq(f"{val} {unit_from} = ? {unit_to}",
                                ans, [ans - factor, ans + factor, val], explain))
        else:
            rev_ans = val
            rev_val = ans
            rev_explain = f"📝 {rev_val} {unit_to} ÷ {factor} = {rev_ans} {unit_from} ✔"
            qs.append(_make_fill(f"{rev_val} {unit_to} = ___ {unit_from}", rev_ans, rev_explain))
    return qs


def generate_math_geometry(num_qs=10):
    """Hình học – sinh ngẫu nhiên."""
    shapes = [
        {"name": "hình vuông",     "sides": 4, "angles": 4, "right": True,  "equal": True},
        {"name": "hình chữ nhật",  "sides": 4, "angles": 4, "right": True,  "equal": False},
        {"name": "hình tam giác",  "sides": 3, "angles": 3, "right": False, "equal": False},
        {"name": "hình tròn",      "sides": 0, "angles": 0, "right": False, "equal": False},
    ]
    templates = [
        lambda s: _make_mcq(
            f"{s['name'].capitalize()} có bao nhiêu cạnh?",
            s["sides"],
            [x for x in [3, 4, 0] if x != s["sides"]],
            f"📝 {s['name'].capitalize()} có {s['sides']} cạnh ✔",
        ),
        lambda s: _make_mcq(
            f"{s['name'].capitalize()} có bao nhiêu góc?",
            s["angles"],
            [x for x in [2, 3, 4, 0] if x != s["angles"]],
            f"📝 {s['name'].capitalize()} có {s['angles']} góc ✔",
        ),
        lambda s: _make_fill(
            f"{s['name'].capitalize()} có ___ cạnh.",
            s["sides"],
            f"📝 {s['name'].capitalize()} có {s['sides']} cạnh ✔",
        ),
    ]
    qs = []
    for _ in range(num_qs):
        s = random.choice(shapes)
        fn = random.choice(templates)
        qs.append(fn(s))
    return qs


def _word_prob_add():
    a = random.randint(10, 50)
    b = random.randint(5, 30)
    ans = a + b
    items = random.choice(["quả táo","cái kẹo","bông hoa","quyển sách","viên bi","con tem","chiếc lá","hạt đậu"])
    names = random.choice([("An","Bình"),("Minh","Hoa"),("Nam","Lan"),("Tuấn","Mai")])
    explain = (
        f"📝 Câu lời giải: Số {items} {names[0]} có tất cả là:\n"
        f"📝 Phép tính: {a} + {b} = {ans} ({items})\n"
        f"✅ Đáp số: {ans} {items}"
    )
    return _make_fill(
        f"{names[0]} có {a} {items}. {names[1]} cho {names[0]} thêm {b} {items}.\n{names[0]} có tất cả bao nhiêu {items}? ___ {items}",
        ans, explain
    )


def _word_prob_sub():
    total = random.randint(20, 60)
    used = random.randint(5, total - 5)
    ans = total - used
    items = random.choice(["quả cam","tờ giấy","chiếc bánh","cái bút","hạt đậu","viên bi","bông hoa"])
    explain = (
        f"📝 Câu lời giải: Số {items} còn lại trong hộp là:\n"
        f"📝 Phép tính: {total} - {used} = {ans} ({items})\n"
        f"✅ Đáp số: {ans} {items}"
    )
    return _make_fill(
        f"Trong hộp có {total} {items}.\nLấy ra {used} {items}. Còn lại bao nhiêu {items}? ___ {items}",
        ans, explain
    )


def _word_prob_mul_simple():
    """Nhân đơn giản dạng cộng lặp."""
    n = random.randint(2, 5)
    each = random.randint(2, 8)
    ans = n * each
    unit = random.choice(["cái kẹo","quả bóng","bông hoa","cây bút","quyển vở"])
    explain = (
        f"📝 Câu lời giải: Số {unit} tất cả mọi người có là:\n"
        f"📝 Phép tính: {n} × {each} = {each + each if n==2 else ans} ({unit})\n"
        f"✅ Đáp số: {ans} {unit}"
    )
    return _make_fill(
        f"Có {n} bạn, mỗi bạn có {each} {unit}.\nHỏi tất cả có bao nhiêu {unit}? ___ {unit}",
        ans, explain
    )


def generate_math_word_problems(num_qs=10):
    templates = [_word_prob_add, _word_prob_sub, _word_prob_mul_simple]
    return [random.choice(templates)() for _ in range(num_qs)]


# ══════════════════════════════════════════════════════════════════════════════
# MODULE SINH CÂU HỎI – TIẾNG ANH (100% MCQ, sinh động)
# ══════════════════════════════════════════════════════════════════════════════
def _eng_q_viet_to_eng(word_vi, word_en, pool):
    """Hỏi từ tiếng Việt → chọn tiếng Anh."""
    wrong_pool = [w[0] for w in pool if w[0] != word_en]
    distractors = random.sample(wrong_pool, min(3, len(wrong_pool)))
    opts = [word_en] + distractors
    random.shuffle(opts)
    return {
        "type": "mcq",
        "q": f"'{word_vi}' trong tiếng Anh là gì?",
        "opts": opts,
        "ans": opts.index(word_en),
        "explain": f"📝 {word_en.capitalize()} = {word_vi} ✔",
    }


def _eng_q_eng_to_viet(word_en, word_vi, pool):
    """Hỏi từ tiếng Anh → chọn nghĩa tiếng Việt."""
    wrong_pool = [w[1] for w in pool if w[1] != word_vi]
    distractors = random.sample(wrong_pool, min(3, len(wrong_pool)))
    opts = [word_vi] + distractors
    random.shuffle(opts)
    return {
        "type": "mcq",
        "q": f"'{word_en.capitalize()}' có nghĩa là gì?",
        "opts": opts,
        "ans": opts.index(word_vi),
        "explain": f"📝 {word_en.capitalize()} = {word_vi} ✔",
    }


def _eng_q_odd_one_out(pool):
    """Câu hỏi tìm từ khác loại – dùng 2 category khác nhau."""
    cats = list(ENG_VOCAB.keys())
    cat1, cat2 = random.sample(cats, 2)
    words_cat1 = random.sample(ENG_VOCAB[cat1], 3)
    odd = random.choice(ENG_VOCAB[cat2])
    all4 = [w[0] for w in words_cat1] + [odd[0]]
    random.shuffle(all4)
    return {
        "type": "mcq",
        "q": f"Từ nào KHÁC LOẠI với các từ còn lại?\n{', '.join(all4)}",
        "opts": all4,
        "ans": all4.index(odd[0]),
        "explain": f"📝 '{odd[0]}' ({odd[1]}) thuộc nhóm khác ✔",
    }


def generate_eng_topic(category_key, num_qs=10):
    """Sinh MCQ Tiếng Anh cho 1 chủ đề – hàng trăm tổ hợp."""
    pool = ENG_VOCAB[category_key]
    qs = []
    for _ in range(num_qs):
        word_en, word_vi = random.choice(pool)
        mode = random.choice(["vi_to_en", "en_to_vi", "odd"])
        if mode == "vi_to_en":
            qs.append(_eng_q_viet_to_eng(word_vi, word_en, pool))
        elif mode == "en_to_vi":
            qs.append(_eng_q_eng_to_viet(word_en, word_vi, pool))
        else:
            qs.append(_eng_q_odd_one_out(pool))
    return qs


def generate_eng_mixed(num_qs=10):
    """Ôn tập Tiếng Anh – lấy ngẫu nhiên từ tất cả chủ đề."""
    qs = []
    for _ in range(num_qs):
        cat = random.choice(list(ENG_VOCAB.keys()))
        pool = ENG_VOCAB[cat]
        word_en, word_vi = random.choice(pool)
        mode = random.choice(["vi_to_en", "en_to_vi"])
        if mode == "vi_to_en":
            qs.append(_eng_q_viet_to_eng(word_vi, word_en, pool))
        else:
            qs.append(_eng_q_eng_to_viet(word_en, word_vi, pool))
    return qs


# ══════════════════════════════════════════════════════════════════════════════
# MODULE SINH CÂU HỎI – TIẾNG VIỆT (động, từ mảng dữ liệu)
# ══════════════════════════════════════════════════════════════════════════════
def generate_viet_chinh_ta(num_qs=10):
    """Chính tả tr/ch, s/x – sinh MCQ ngẫu nhiên từ mảng."""
    qs = []
    pool_tr_ch = VIET_VOCAB["chinh_ta_tr_ch"]
    pool_s_x   = VIET_VOCAB["chinh_ta_s_x"]
    for _ in range(num_qs):
        mode = random.choice(["tr_ch", "s_x", "pick_correct"])
        if mode == "tr_ch":
            pair = random.choice(pool_tr_ch)
            correct, wrong = pair
            opts = [correct, wrong, wrong.replace("tr","ch").replace("ch","tr")[::-1][:len(wrong)], correct+"ng"]
            opts = list(dict.fromkeys(opts))[:4]
            while len(opts) < 4:
                opts.append(wrong + str(random.randint(1,9)))
            random.shuffle(opts)
            if correct not in opts:
                opts[0] = correct
                random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": f"Từ nào viết đúng chính tả?\n(Gợi ý: dùng tr/ch)",
                "opts": opts,
                "ans": opts.index(correct),
                "explain": f"📝 '{correct}' viết đúng với 'tr' ✔",
            })
        elif mode == "s_x":
            pair = random.choice(pool_s_x)
            correct, wrong = pair
            opts = [correct, wrong,
                    correct.replace("s","x") if correct.startswith("s") else correct.replace("x","s"),
                    wrong + "h"]
            opts = list(dict.fromkeys(opts))[:4]
            while len(opts) < 4:
                opts.append(wrong + str(random.randint(1,9)))
            random.shuffle(opts)
            if correct not in opts:
                opts[0] = correct
                random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": f"Từ nào viết đúng chính tả?\n(Gợi ý: dùng s/x)",
                "opts": opts,
                "ans": opts.index(correct),
                "explain": f"📝 '{correct}' viết đúng ✔",
            })
        else:
            # Điền âm đầu tr hoặc ch
            pair = random.choice(pool_tr_ch)
            word = pair[0]  # từ đúng bắt đầu bằng tr
            prefix = "tr"
            rest = word[2:]
            opts = ["tr", "ch", "t", "d"]
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": f"Điền âm đầu đúng: ___" + rest,
                "opts": opts,
                "ans": opts.index(prefix),
                "explain": f"📝 Viết đúng là '{word}' → âm đầu 'tr' ✔",
            })
    return qs


def generate_viet_tu_loai(num_qs=10):
    """Từ loại – danh từ, động từ, tính từ – sinh MCQ ngẫu nhiên."""
    danh_tu  = [d[0] for d in VIET_VOCAB["danh_tu"]]
    dong_tu  = ["chạy","nhảy","đọc","viết","ăn","ngủ","học","chơi","hát","múa","vẽ","nói","nghe","nhìn"]
    tinh_tu  = ["đẹp","xấu","to","bé","nhanh","chậm","vui","buồn","cao","thấp","nóng","lạnh","sáng","tối"]
    qs = []
    for _ in range(num_qs):
        mode = random.choice(["find_dt", "find_dgt", "find_tt", "not_dt"])
        if mode == "find_dt":
            correct = random.choice(danh_tu)
            wrong3  = random.sample(dong_tu + tinh_tu, 3)
            opts = [correct] + wrong3
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": "Từ nào là DANH TỪ?",
                "opts": opts,
                "ans": opts.index(correct),
                "explain": f"📝 '{correct}' là danh từ (chỉ sự vật/nơi chốn/người) ✔",
            })
        elif mode == "find_dgt":
            correct = random.choice(dong_tu)
            wrong3  = random.sample(danh_tu + tinh_tu, 3)
            opts = [correct] + wrong3
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": "Từ nào là ĐỘNG TỪ (chỉ hành động)?",
                "opts": opts,
                "ans": opts.index(correct),
                "explain": f"📝 '{correct}' là động từ (chỉ hành động) ✔",
            })
        elif mode == "find_tt":
            correct = random.choice(tinh_tu)
            wrong3  = random.sample(danh_tu + dong_tu, 3)
            opts = [correct] + wrong3
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": "Từ nào là TÍNH TỪ (chỉ đặc điểm)?",
                "opts": opts,
                "ans": opts.index(correct),
                "explain": f"📝 '{correct}' là tính từ (chỉ đặc điểm, tính chất) ✔",
            })
        else:
            wrong = random.choice(dong_tu)
            corrects = random.sample(danh_tu, 3)
            opts = corrects + [wrong]
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": "Từ nào KHÔNG phải danh từ?",
                "opts": opts,
                "ans": opts.index(wrong),
                "explain": f"📝 '{wrong}' là động từ, không phải danh từ ✔",
            })
    return qs


def generate_viet_dong_nghia_trai_nghia(num_qs=10):
    """Từ đồng nghĩa / trái nghĩa – sinh MCQ ngẫu nhiên từ mảng."""
    qs = []
    for _ in range(num_qs):
        mode = random.choice(["dong", "trai"])
        if mode == "dong":
            pair = random.choice(VIET_VOCAB["dong_nghia"])
            w1, w2 = pair
            # Hỏi đồng nghĩa
            wrong_pool = [p[1] for p in VIET_VOCAB["trai_nghia"]]
            distractors = random.sample(wrong_pool, 3)
            opts = [w2] + distractors
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": f"Từ đồng nghĩa với '{w1}' là?",
                "opts": opts,
                "ans": opts.index(w2),
                "explain": f"📝 {w1} ≈ {w2} (cùng nghĩa) ✔",
            })
        else:
            pair = random.choice(VIET_VOCAB["trai_nghia"])
            w1, w2 = pair
            wrong_pool = [p[0] for p in VIET_VOCAB["trai_nghia"] if p[0] != w1 and p[0] != w2]
            distractors = random.sample(wrong_pool, 3)
            opts = [w2] + distractors
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": f"Từ trái nghĩa với '{w1}' là?",
                "opts": opts,
                "ans": opts.index(w2),
                "explain": f"📝 {w1} ↔ {w2} (trái nghĩa) ✔",
            })
    return qs


def generate_viet_cau_van(num_qs=10):
    """Câu hỏi / câu kể / câu cảm – sinh MCQ ngẫu nhiên."""
    cau_hoi_vi_du = [
        ("Bạn tên là gì?", "câu hỏi", "?"),
        ("Hôm nay thứ mấy?", "câu hỏi", "?"),
        ("Em có khỏe không?", "câu hỏi", "?"),
        ("Con đang làm gì vậy?", "câu hỏi", "?"),
        ("Ai đang hát ngoài sân?", "câu hỏi", "?"),
    ]
    cau_ke_vi_du = [
        ("Trời hôm nay rất đẹp.", "câu kể", "."),
        ("Em đang học bài.", "câu kể", "."),
        ("Bạn Nam rất chăm học.", "câu kể", "."),
        ("Mẹ đang nấu cơm.", "câu kể", "."),
        ("Vườn nhà em có nhiều hoa.", "câu kể", "."),
    ]
    cau_cam_vi_du = [
        ("Ôi, đẹp quá!", "câu cảm", "!"),
        ("Chà, ngon thật!", "câu cảm", "!"),
        ("Ồ, bất ngờ quá!", "câu cảm", "!"),
        ("Ôi trời, lạnh ghê!", "câu cảm", "!"),
        ("Wow, tuyệt vời!", "câu cảm", "!"),
    ]
    all_examples = cau_hoi_vi_du + cau_ke_vi_du + cau_cam_vi_du
    tu_hoi_data = VIET_VOCAB["cau_hoi"]
    qs = []
    for _ in range(num_qs):
        mode = random.choice(["loai_cau", "dau_cau", "tu_hoi"])
        if mode == "loai_cau":
            ex = random.choice(all_examples)
            cau, loai, _ = ex
            opts = ["câu hỏi", "câu kể", "câu cảm", "câu cầu khiến"]
            qs.append({
                "type": "mcq",
                "q": f"Câu sau là loại câu gì?\n'{cau}'",
                "opts": opts,
                "ans": opts.index(loai),
                "explain": f"📝 '{cau}' là {loai} ✔",
            })
        elif mode == "dau_cau":
            ex = random.choice(all_examples)
            cau, loai, dau = ex
            opts = [".", "?", "!", ","]
            qs.append({
                "type": "mcq",
                "q": f"{loai.capitalize()} kết thúc bằng dấu gì?",
                "opts": opts,
                "ans": opts.index(dau),
                "explain": f"📝 {loai.capitalize()} kết thúc bằng dấu '{dau}' ✔",
            })
        else:
            pair = random.choice(tu_hoi_data)
            tu, hoi_ve = pair
            wrong_pool = [p[1] for p in tu_hoi_data if p[1] != hoi_ve]
            distractors = random.sample(wrong_pool, min(3, len(wrong_pool)))
            opts = [hoi_ve] + distractors
            random.shuffle(opts)
            qs.append({
                "type": "mcq",
                "q": f"Từ hỏi '{tu}' dùng để hỏi về điều gì?",
                "opts": opts,
                "ans": opts.index(hoi_ve),
                "explain": f"📝 '{tu}' → hỏi về {hoi_ve} ✔",
            })
    return qs


def generate_viet_tap_lam_van(num_qs=10):
    """Tập làm văn – điền từ, hoàn thành câu – MCQ ngẫu nhiên."""
    mua_templates = [
        ("Mùa hè, trời ____.", ["nắng nóng","mưa phùn","lạnh giá","có tuyết"], 0, "Mùa hè nắng nóng"),
        ("Mùa đông, trời ____.", ["lạnh giá","nắng chang chang","oi bức","mát mẻ"], 0, "Mùa đông lạnh"),
        ("Mùa xuân, cây cối ____.", ["đâm chồi nảy lộc","rụng lá","khô héo","đứng im"], 0, "Mùa xuân cây đâm chồi"),
        ("Mùa thu, lá ____.", ["rụng nhiều","nở hoa","xanh tươi","mọc cao"], 0, "Mùa thu lá rụng"),
    ]
    ta_canh_templates = [
        ("Bầu trời mùa thu ____ và trong xanh.", ["cao","thấp","đen","mờ"], 0, "Bầu trời mùa thu cao"),
        ("Mặt trời mọc ở hướng ____.", ["đông","tây","nam","bắc"], 0, "Mặt trời mọc hướng đông"),
        ("Hoa hồng có màu ____.", ["đỏ","đen","xanh","vàng"], 0, "Hoa hồng màu đỏ"),
        ("Cây xanh cần ____ để sống.", ["ánh sáng và nước","cát và sỏi","đá và muối","gió và băng"], 0, "Cây cần ánh sáng và nước"),
    ]
    all_t = mua_templates + ta_canh_templates
    qs = []
    for _ in range(num_qs):
        tmpl = random.choice(all_t)
        q_text, opts, ans_idx, explain_text = tmpl
        random.shuffle(opts)
        # Tìm lại đáp án sau shuffle
        correct_ans = tmpl[1][tmpl[2]]
        new_ans = opts.index(correct_ans)
        qs.append({
            "type": "mcq",
            "q": q_text,
            "opts": opts,
            "ans": new_ans,
            "explain": f"📝 {explain_text} ✔",
        })
    return qs


def generate_viet_mixed(num_qs=15):
    """Ôn tập Tiếng Việt tổng hợp – lấy ngẫu nhiên từ tất cả module."""
    all_qs = (
        generate_viet_chinh_ta(4) +
        generate_viet_tu_loai(4) +
        generate_viet_dong_nghia_trai_nghia(4) +
        generate_viet_cau_van(3)
    )
    random.shuffle(all_qs)
    return all_qs[:num_qs]


# ══════════════════════════════════════════════════════════════════════════════
# CẤU TRÚC SUBJECTS – Dùng "auto_gen" thay vì hardcode câu hỏi
# ══════════════════════════════════════════════════════════════════════════════
SUBJECTS = {
    "math": {
        "label": "Toán học",
        "icon":  "🔢",
        "badge": "badge-math",
        "q_box_class": "q-box-math",
        "color": "#FF6B6B",
        "topics": [
            {"name": "Phép cộng có nhớ",  "qs": [], "auto_gen": "add"},
            {"name": "Phép trừ có nhớ",   "qs": [], "auto_gen": "sub"},
            {"name": "Toán có lời văn",    "qs": [], "auto_gen": "word"},
            {"name": "So sánh số",         "qs": [], "auto_gen": "compare"},
            {"name": "Đo lường",           "qs": [], "auto_gen": "measure"},
            {"name": "Hình học",           "qs": [], "auto_gen": "geometry"},
            {"name": "🌟 Ôn tập tổng hợp","qs": [], "auto_gen": "math_mixed"},
        ],
    },
    "viet": {
        "label": "Tiếng Việt",
        "icon":  "📖",
        "badge": "badge-viet",
        "q_box_class": "q-box-viet",
        "color": "#22c55e",
        "topics": [
            {"name": "Chính tả – âm vần",         "qs": [], "auto_gen": "viet_chinh_ta"},
            {"name": "Từ loại",                    "qs": [], "auto_gen": "viet_tu_loai"},
            {"name": "Từ đồng nghĩa – trái nghĩa", "qs": [], "auto_gen": "viet_dong_trai"},
            {"name": "Câu hỏi – câu kể – câu cảm", "qs": [], "auto_gen": "viet_cau_van"},
            {"name": "Tập làm văn",                "qs": [], "auto_gen": "viet_tap_van"},
            {"name": "🌟 Ôn tập tổng hợp",         "qs": [], "auto_gen": "viet_mixed"},
        ],
    },
    "eng": {
        "label": "Tiếng Anh",
        "icon":  "🔤",
        "badge": "badge-eng",
        "q_box_class": "q-box-eng",
        "color": "#4D96FF",
        "topics": [
            {"name": "Màu sắc (Colors)",         "qs": [], "auto_gen": "eng_colors"},
            {"name": "Động vật (Animals)",        "qs": [], "auto_gen": "eng_animals"},
            {"name": "Gia đình (Family)",         "qs": [], "auto_gen": "eng_family"},
            {"name": "Đồ dùng học tập (School)",  "qs": [], "auto_gen": "eng_school"},
            {"name": "Bộ phận cơ thể (Body)",     "qs": [], "auto_gen": "eng_body"},
            {"name": "Thức ăn (Food)",             "qs": [], "auto_gen": "eng_food"},
            {"name": "Số đếm (Numbers)",          "qs": [], "auto_gen": "eng_numbers"},
            {"name": "Chào hỏi (Greetings)",      "qs": [], "auto_gen": "eng_greetings"},
            {"name": "🌟 Ôn tập tổng hợp",        "qs": [], "auto_gen": "eng_mixed"},
        ],
    },
}

AUTO_GEN_MAP = {
    "add":            lambda: generate_math_addition(10),
    "sub":            lambda: generate_math_subtraction(10),
    "word":           lambda: generate_math_word_problems(10),
    "compare":        lambda: generate_math_comparison(10),
    "measure":        lambda: generate_math_measurement(10),
    "geometry":       lambda: generate_math_geometry(10),
    "math_mixed":     lambda: _math_mixed(15),
    "viet_chinh_ta":  lambda: generate_viet_chinh_ta(10),
    "viet_tu_loai":   lambda: generate_viet_tu_loai(10),
    "viet_dong_trai": lambda: generate_viet_dong_nghia_trai_nghia(10),
    "viet_cau_van":   lambda: generate_viet_cau_van(10),
    "viet_tap_van":   lambda: generate_viet_tap_lam_van(10),
    "viet_mixed":     lambda: generate_viet_mixed(15),
    "eng_colors":     lambda: generate_eng_topic("colors", 10),
    "eng_animals":    lambda: generate_eng_topic("animals", 10),
    "eng_family":     lambda: generate_eng_topic("family", 10),
    "eng_school":     lambda: generate_eng_topic("school", 10),
    "eng_body":       lambda: generate_eng_topic("body", 10),
    "eng_food":       lambda: generate_eng_topic("food", 10),
    "eng_numbers":    lambda: generate_eng_topic("numbers", 10),
    "eng_greetings":  lambda: generate_eng_topic("greetings", 10),
    "eng_mixed":      lambda: generate_eng_mixed(15),
}

def _math_mixed(num_qs=15):
    all_qs = (
        generate_math_addition(3) +
        generate_math_subtraction(3) +
        generate_math_word_problems(3) +
        generate_math_comparison(3) +
        generate_math_geometry(2) +
        generate_math_measurement(1)
    )
    random.shuffle(all_qs)
    return all_qs[:num_qs]


# ══════════════════════════════════════════════════════════════════════════════
# CSS TOÀN CỤC – GLASSMORPHISM + NEUMORPHISM EdTech
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Baloo 2', cursive !important; }

.stApp {
    background: #0f0c29;
    background-image:
        radial-gradient(ellipse at 0% 0%, rgba(255,107,107,0.25) 0%, transparent 50%),
        radial-gradient(ellipse at 100% 0%, rgba(77,150,255,0.2) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 100%, rgba(168,85,247,0.2) 0%, transparent 50%),
        linear-gradient(135deg, #0f0c29 0%, #1a1a40 50%, #302b63 100%);
    min-height: 100vh;
}

header[data-testid="stHeader"] { display: none; }
.block-container {
    padding-top: 0.6rem !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
    max-width: 100% !important;
}

/* ─── FLOATING BACKGROUND PARTICLES ─── */
.float-emoji-wrap {
    position: fixed; top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none; z-index: 0; overflow: hidden;
}
.float-emoji {
    position: absolute; font-size: 24px;
    opacity: 0.06; animation: floatUp linear infinite;
}
@keyframes floatUp {
    0%   { transform: translateY(110vh) rotate(0deg); opacity: 0.06; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}

/* ─── LEFT PANEL – Glassmorphism ─── */
.left-panel {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 28px;
    padding: 22px 16px;
    min-height: 82vh;
    box-shadow:
        0 8px 32px rgba(0,0,0,0.4),
        inset 0 1px 0 rgba(255,255,255,0.08);
    position: sticky;
    top: 0.6rem;
}
.student-card {
    background: linear-gradient(135deg, rgba(255,217,61,0.12), rgba(255,107,107,0.08));
    border: 1.5px solid rgba(255,217,61,0.25);
    border-radius: 22px;
    padding: 18px 14px;
    margin-bottom: 18px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(255,217,61,0.1);
}
.student-avatar {
    font-size: 56px; margin-bottom: 6px;
    display: block; animation: wobble 3s infinite;
    filter: drop-shadow(0 4px 12px rgba(255,217,61,0.4));
}
.student-name  { font-size: 19px; font-weight: 800; color: #FFD93D; margin: 0 0 3px; }
.student-class { font-size: 12px; color: rgba(255,255,255,0.45); font-weight: 700; }
.stat-row { display: flex; justify-content: space-around; margin-top: 14px; }
.stat-item { text-align: center; }
.stat-val { font-size: 20px; font-weight: 800; color: #FF9A3C; line-height: 1.2; }
.stat-lbl { font-size: 9px; color: rgba(255,255,255,0.4); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; }

.panel-divider { height: 1px; background: rgba(255,255,255,0.08); margin: 14px 0; }
.panel-section-title {
    font-size: 10px; font-weight: 800;
    color: rgba(255,255,255,0.35);
    text-transform: uppercase; letter-spacing: .12em;
    margin: 0 0 10px; padding: 0 2px;
}

/* ─── MAIN CONTENT AREA ─── */
.right-panel {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 28px;
    padding: 24px 28px;
    min-height: 80vh;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* ─── ONBOARDING ─── */
.onboard-wrap {
    text-align: center; padding: 20px 0 12px;
    animation: fadeSlideUp 0.7s ease both;
    position: relative; z-index: 1;
}
.onboard-mascot {
    font-size: 120px; line-height: 1; margin-bottom: 12px;
    display: block; animation: wobble 2.5s infinite;
    filter: drop-shadow(0 12px 24px rgba(255,217,61,0.4));
}
.onboard-title {
    font-family: 'Nunito', sans-serif;
    font-size: 40px; font-weight: 900;
    background: linear-gradient(135deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF, #a855f7);
    background-size: 300%; -webkit-background-clip: text;
    -webkit-text-fill-color: transparent; background-clip: text;
    animation: gradShift 4s ease infinite;
    margin: 0 0 10px; line-height: 1.2;
}
.onboard-sub { font-size: 18px; color: rgba(255,255,255,0.65); font-weight: 700; margin: 0 0 20px; }
.star-row { font-size: 30px; letter-spacing: 8px; margin-bottom: 28px; animation: bounce 1.5s infinite; display: block; }

/* ─── GREETING BOX ─── */
.greeting-box {
    background: linear-gradient(135deg, rgba(102,126,234,0.3), rgba(118,75,162,0.3));
    border: 1.5px solid rgba(168,85,247,0.4);
    backdrop-filter: blur(10px);
    border-radius: 22px; padding: 16px 22px; margin-bottom: 20px;
    text-align: center;
    box-shadow: 0 8px 28px rgba(102,126,234,0.25);
    animation: fadeSlideUp 0.5s ease;
}
.greeting-text { font-size: 22px; font-weight: 800; color: #fff; margin: 0; }

/* ─── SUBJECT CARDS ─── */
.subject-card {
    border-radius: 24px; padding: 26px 14px;
    text-align: center;
    transition: transform 0.2s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s;
    cursor: pointer;
    position: relative; overflow: hidden;
}
.subject-card:hover { transform: translateY(-4px) scale(1.02); }

/* ─── TOPIC LIST ─── */
.topic-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.10);
    border-radius: 18px; padding: 16px 20px;
    font-size: 17px; font-weight: 700;
    color: rgba(255,255,255,0.9);
    margin-bottom: 10px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.2);
    transition: border-color 0.2s, background 0.2s;
    display: flex; align-items: center; gap: 10px;
}
.topic-card:hover { background: rgba(255,255,255,0.09); border-color: rgba(255,217,61,0.4); }
.topic-mixed {
    background: linear-gradient(135deg, rgba(255,217,61,0.12), rgba(168,85,247,0.12)) !important;
    border-color: rgba(255,217,61,0.35) !important;
}

/* ─── QUESTION BOX ─── */
.q-box-math {
    background: linear-gradient(135deg, #FF6B6B 0%, #FF9A3C 60%, #c2410c 100%);
    border-radius: 26px; padding: 34px 26px;
    text-align: center; margin-bottom: 20px;
    box-shadow: 0 12px 36px rgba(255,107,107,0.5), inset 0 1px 0 rgba(255,255,255,0.2);
    position: relative; overflow: hidden;
    animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.q-box-viet {
    background: linear-gradient(135deg, #22c55e 0%, #16a34a 60%, #166534 100%);
    border-radius: 26px; padding: 34px 26px;
    text-align: center; margin-bottom: 20px;
    box-shadow: 0 12px 36px rgba(34,197,94,0.5), inset 0 1px 0 rgba(255,255,255,0.2);
    position: relative; overflow: hidden;
    animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.q-box-eng {
    background: linear-gradient(135deg, #4D96FF 0%, #1d4ed8 60%, #1e3a8a 100%);
    border-radius: 26px; padding: 34px 26px;
    text-align: center; margin-bottom: 20px;
    box-shadow: 0 12px 36px rgba(77,150,255,0.5), inset 0 1px 0 rgba(255,255,255,0.2);
    position: relative; overflow: hidden;
    animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.q-box-math::before  { content:'✨'; position:absolute; top:10px; right:16px; font-size:28px; animation: sparkle 1s ease infinite alternate; }
.q-box-math::after   { content:'🔢'; position:absolute; bottom:10px; left:16px; font-size:26px; opacity:0.4; }
.q-box-viet::before  { content:'✨'; position:absolute; top:10px; right:16px; font-size:28px; animation: sparkle 1s ease infinite alternate; }
.q-box-viet::after   { content:'📖'; position:absolute; bottom:10px; left:16px; font-size:26px; opacity:0.4; }
.q-box-eng::before   { content:'✨'; position:absolute; top:10px; right:16px; font-size:28px; animation: sparkle 1s ease infinite alternate; }
.q-box-eng::after    { content:'🔤'; position:absolute; bottom:10px; left:16px; font-size:26px; opacity:0.4; }

.q-text {
    font-size: 30px; font-weight: 800; color: #fff;
    margin: 0; line-height: 1.55;
    text-shadow: 0 3px 10px rgba(0,0,0,0.3);
    white-space: pre-line;
}

/* ─── OPTIONS ─── */
.opt-correct {
    background: linear-gradient(135deg, #DCFCE7, #BBF7D0);
    border: 3px solid #22c55e; border-radius: 18px;
    padding: 18px 22px; font-size: 20px; font-weight: 800;
    color: #14532d; width: 100%; text-align: left;
    margin-bottom: 10px; display: block;
    box-shadow: 0 6px 20px rgba(34,197,94,0.35);
    animation: popIn 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
.opt-wrong {
    background: linear-gradient(135deg, #FEE2E2, #fca5a5);
    border: 3px solid #ef4444; border-radius: 18px;
    padding: 18px 22px; font-size: 20px; font-weight: 800;
    color: #7f1d1d; width: 100%; text-align: left;
    margin-bottom: 10px; display: block;
    animation: shake 0.4s ease;
}
.opt-dim {
    background: rgba(255,255,255,0.05); border: 2px solid rgba(255,255,255,0.1);
    border-radius: 18px; padding: 18px 22px; font-size: 20px;
    font-weight: 600; color: rgba(255,255,255,0.3);
    width: 100%; text-align: left; margin-bottom: 10px; display: block; opacity: 0.5;
}

/* ─── FILL BLANK ─── */
.fill-label {
    font-size: 15px; font-weight: 800; color: #a78bfa;
    margin: 0 0 6px; text-transform: uppercase; letter-spacing: .06em;
}
div[data-testid="stTextInput"] input {
    font-family: 'Baloo 2', cursive !important;
    font-size: 28px !important; font-weight: 800 !important;
    border-radius: 16px !important;
    border: 3px solid rgba(168,85,247,0.4) !important;
    padding: 14px 20px !important;
    background: rgba(255,255,255,0.07) !important;
    color: #fff !important;
    text-align: center !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #a855f7 !important;
    box-shadow: 0 0 0 4px rgba(168,85,247,0.2) !important;
}

/* ─── FEEDBACK ─── */
.feedback-correct {
    background: linear-gradient(135deg, rgba(34,197,94,0.15), rgba(22,163,74,0.1));
    border: 2.5px solid rgba(34,197,94,0.5);
    backdrop-filter: blur(10px);
    border-radius: 22px; padding: 24px 26px; margin-top: 6px;
    animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1);
    text-align: center;
    box-shadow: 0 8px 28px rgba(34,197,94,0.2);
}
.feedback-correct-emoji { font-size: 56px; display: block; margin-bottom: 4px; animation: bounce 1s infinite; }
.feedback-correct-title { font-size: 26px; font-weight: 800; color: #6ee7b7; margin: 0 0 6px; }
.feedback-correct-msg   { font-size: 16px; font-weight: 600; color: rgba(255,255,255,0.7); margin: 0; }

.feedback-wrong {
    background: linear-gradient(135deg, rgba(251,146,60,0.12), rgba(234,179,8,0.08));
    border: 2.5px dashed rgba(251,146,60,0.5);
    backdrop-filter: blur(10px);
    border-radius: 22px; padding: 20px 24px; margin-top: 6px;
    animation: popIn 0.3s ease;
    box-shadow: 0 4px 20px rgba(251,146,60,0.15);
}
.feedback-wrong-title {
    font-size: 20px; font-weight: 800; color: #FB923C;
    margin: 0 0 12px; text-align: center;
}
.feedback-answer {
    background: rgba(34,197,94,0.15); border: 2px solid rgba(34,197,94,0.4);
    border-radius: 14px; padding: 12px 16px;
    font-size: 18px; font-weight: 800; color: #6ee7b7; margin-bottom: 10px;
}
.feedback-explain {
    background: rgba(234,179,8,0.1); border: 2px solid rgba(234,179,8,0.3);
    border-radius: 14px; padding: 12px 16px;
    font-size: 15px; font-weight: 600;
    color: rgba(255,255,255,0.75); line-height: 1.9; white-space: pre-line;
}
.explain-title {
    font-size: 12px; font-weight: 800; color: rgba(234,179,8,0.9);
    text-transform: uppercase; letter-spacing: .06em; margin-bottom: 6px;
}

/* ─── PROGRESS BAR ─── */
.progress-outer {
    background: rgba(255,255,255,0.08); border-radius: 99px;
    height: 20px; margin-bottom: 16px;
    overflow: hidden; border: 1.5px solid rgba(255,255,255,0.1);
}
.progress-inner {
    height: 20px;
    background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF, #a855f7);
    background-size: 400% 100%;
    border-radius: 99px;
    animation: shimmer 3s linear infinite;
    transition: width 0.6s cubic-bezier(0.34,1.56,0.64,1);
    position: relative;
}
.progress-inner::after {
    content: '⭐'; position: absolute; right: -8px; top: -5px;
    font-size: 24px; animation: sparkle 0.8s ease infinite alternate;
}
.q-counter {
    font-size: 15px; font-weight: 800;
    color: rgba(255,255,255,0.7); text-align: right; margin-bottom: 6px;
}

/* ─── STREAK / BONUS BANNERS ─── */
.streak-banner {
    background: linear-gradient(135deg, #FF6B6B, #FF9A3C);
    border-radius: 16px; padding: 10px 16px;
    text-align: center; font-size: 20px; font-weight: 800; color: #fff;
    margin-bottom: 12px;
    animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1);
    box-shadow: 0 6px 24px rgba(255,107,107,0.45);
}
.bonus-banner {
    background: linear-gradient(135deg, #FFD93D, #FF9A3C);
    border-radius: 16px; padding: 8px 16px;
    text-align: center; font-size: 18px; font-weight: 800; color: #1a1a2e;
    margin-bottom: 10px;
    animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1);
    box-shadow: 0 4px 16px rgba(255,217,61,0.45);
}

/* ─── RESULT SCREEN ─── */
.result-wrap {
    text-align: center; padding: 10px 0 22px;
    animation: fadeSlideUp 0.7s ease both;
}
.result-trophy {
    font-size: 110px; margin-bottom: 8px; display: block;
    animation: bounce 1.6s infinite;
    filter: drop-shadow(0 10px 20px rgba(255,217,61,0.4));
}
.result-title {
    font-family: 'Nunito', sans-serif; font-size: 42px; font-weight: 900;
    color: #fff; margin: 0 0 6px;
    text-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.result-msg { font-size: 18px; color: rgba(255,255,255,0.65); font-weight: 600; margin: 0 0 22px; }
.badge-earned {
    display: inline-block; font-size: 17px; font-weight: 800;
    padding: 12px 30px; border-radius: 99px; margin-bottom: 22px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    animation: popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.3s both;
}
.badge-math     { background: linear-gradient(135deg, #FF9A3C, #FF6B6B); color: #fff; }
.badge-viet     { background: linear-gradient(135deg, #22c55e, #16a34a); color: #fff; }
.badge-eng      { background: linear-gradient(135deg, #4D96FF, #1d4ed8); color: #fff; }
.badge-gold     { background: linear-gradient(135deg, #FFD700, #FF9A3C); color: #fff; }
.badge-silver   { background: linear-gradient(135deg, #a855f7, #7c3aed); color: #fff; }
.badge-bronze   { background: linear-gradient(135deg, #22c55e, #16a34a); color: #fff; }
.badge-try      { background: linear-gradient(135deg, #64748b, #475569); color: #fff; }
.badge-superstar {
    background: linear-gradient(135deg, #FFD700, #FF6B6B, #a855f7, #4D96FF);
    background-size: 300%;
    animation: gradShift 2s ease infinite, popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.3s both;
    color: #fff; font-size: 20px;
}

.score-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 20px; }
.score-box-correct {
    background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(22,163,74,0.1));
    border: 2.5px solid rgba(34,197,94,0.4);
    border-radius: 22px; padding: 24px; text-align: center;
    box-shadow: 0 4px 20px rgba(34,197,94,0.15);
    animation: fadeSlideUp 0.5s ease 0.2s both;
}
.score-box-wrong {
    background: linear-gradient(135deg, rgba(239,68,68,0.2), rgba(220,38,38,0.1));
    border: 2.5px solid rgba(239,68,68,0.4);
    border-radius: 22px; padding: 24px; text-align: center;
    box-shadow: 0 4px 20px rgba(239,68,68,0.15);
    animation: fadeSlideUp 0.5s ease 0.3s both;
}
.score-num { font-size: 50px; font-weight: 800; }
.score-lbl { font-size: 14px; font-weight: 700; margin-top: 2px; color: rgba(255,255,255,0.7); }

.total-pts-box {
    background: linear-gradient(135deg, rgba(255,217,61,0.12), rgba(255,154,60,0.08));
    border: 1.5px solid rgba(255,217,61,0.3);
    backdrop-filter: blur(10px);
    border-radius: 22px; padding: 18px 26px; margin-bottom: 22px;
    display: flex; align-items: center; justify-content: center; gap: 20px;
    box-shadow: 0 8px 28px rgba(255,217,61,0.15);
    animation: fadeSlideUp 0.5s ease 0.1s both;
}
.total-pts-icon { font-size: 36px; animation: sparkle 1s ease infinite alternate; }
.total-pts-val  { font-size: 32px; font-weight: 800; color: #FFD93D; }
.total-pts-lbl  { font-size: 12px; font-weight: 700; color: rgba(255,255,255,0.5); text-transform: uppercase; }

/* ─── BADGE HISTORY ─── */
.badge-history-box {
    background: rgba(255,255,255,0.04);
    border: 1.5px solid rgba(255,255,255,0.1);
    border-radius: 20px; padding: 14px 18px; margin-bottom: 16px;
    animation: fadeSlideUp 0.6s ease 0.4s both;
}
.badge-history-title { font-size: 12px; font-weight: 800; color: #a78bfa; text-transform: uppercase; letter-spacing:.06em; margin: 0 0 8px; }
.badge-history-row   { display: flex; flex-wrap: wrap; gap: 8px; }
.badge-chip { font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 99px; color: #fff; display: inline-block; }

/* ─── BUTTONS ─── */
div.stButton > button {
    font-family: 'Baloo 2', cursive !important;
    font-weight: 800 !important; font-size: 17px !important;
    height: 56px !important; border-radius: 18px !important;
    transition: transform 0.18s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.18s !important;
    letter-spacing: .02em !important;
    position: relative; z-index: 1;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #FF6B6B, #FF9A3C) !important;
    border: none !important; color: #fff !important;
    box-shadow: 0 6px 20px rgba(255,107,107,0.45) !important;
}
div.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px) scale(1.04) !important;
    box-shadow: 0 14px 30px rgba(255,107,107,0.6) !important;
}
div.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,0.06) !important;
    border: 2px solid rgba(255,255,255,0.15) !important;
    color: rgba(255,255,255,0.85) !important;
    backdrop-filter: blur(10px);
}
div.stButton > button[kind="secondary"]:hover {
    border-color: rgba(168,85,247,0.5) !important;
    background: rgba(168,85,247,0.12) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 16px rgba(168,85,247,0.2) !important;
}

/* ─── SELECTBOX & TEXT INPUT (onboard) ─── */
div[data-testid="stSelectbox"] > div > div,
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.07) !important;
    border: 2px solid rgba(255,255,255,0.15) !important;
    border-radius: 14px !important;
    color: #fff !important;
    font-size: 16px !important;
    font-weight: 700 !important;
}

/* ─── CONFETTI ─── */
.confetti-piece {
    position: fixed; border-radius: 3px;
    animation: confettiFall linear forwards;
    z-index: 9999; pointer-events: none;
}
@keyframes confettiFall {
    0%   { transform: translateY(-20px) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
}

/* ─── GOOGLE SHEETS STATUS ─── */
.gs-success {
    background: rgba(34,197,94,0.12); border: 2px solid rgba(34,197,94,0.4);
    border-radius: 14px; padding: 10px 16px;
    font-size: 14px; font-weight: 700; color: #6ee7b7; margin-top: 12px;
}
.gs-error {
    background: rgba(239,68,68,0.1); border: 2px dashed rgba(239,68,68,0.4);
    border-radius: 14px; padding: 10px 16px;
    font-size: 14px; font-weight: 700; color: #fca5a5; margin-top: 12px;
}

/* ─── RECENT RESULT ─── */
.recent-box {
    background: rgba(255,255,255,0.04);
    border: 1.5px solid rgba(255,255,255,0.1);
    border-radius: 20px; padding: 14px 18px; margin-top: 20px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
}
.recent-title { font-size: 11px; font-weight: 800; color: #a78bfa; text-transform: uppercase; letter-spacing:.06em; margin-bottom: 8px; }
.class-badge {
    display: inline-block;
    background: linear-gradient(135deg, #4D96FF, #1d4ed8);
    color: #fff; font-size: 15px; font-weight: 800;
    padding: 7px 20px; border-radius: 99px; margin-top: 4px;
}

/* ─── ANIMATIONS ─── */
@keyframes bounce    { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
@keyframes wobble    { 0%,100%{transform:rotate(0deg)} 15%{transform:rotate(-8deg)} 30%{transform:rotate(6deg)} 45%{transform:rotate(-4deg)} 60%{transform:rotate(2deg)} }
@keyframes popIn     { 0%{transform:scale(0.7);opacity:0} 100%{transform:scale(1);opacity:1} }
@keyframes shake     { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-10px)} 40%{transform:translateX(10px)} 60%{transform:translateX(-6px)} 80%{transform:translateX(6px)} }
@keyframes fadeSlideUp { 0%{opacity:0;transform:translateY(24px)} 100%{opacity:1;transform:translateY(0)} }
@keyframes gradShift { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
@keyframes shimmer   { 0%{background-position:0% 50%} 100%{background-position:100% 50%} }
@keyframes sparkle   { 0%{transform:scale(1) rotate(0deg)} 100%{transform:scale(1.3) rotate(20deg)} }
audio { display: none; }

@media (max-width: 768px) {
    .left-panel { min-height: auto; position: static; margin-bottom: 16px; }
    .q-text { font-size: 22px; }
    .result-title { font-size: 30px; }
    .onboard-title { font-size: 28px; }
}
</style>
""", unsafe_allow_html=True)

# ─── Floating background particles ───────────────────────────────────────────
st.markdown("""
<div class="float-emoji-wrap">
  <span class="float-emoji" style="left:5%;animation-duration:14s;animation-delay:0s;">⭐</span>
  <span class="float-emoji" style="left:15%;animation-duration:18s;animation-delay:2s;">🌟</span>
  <span class="float-emoji" style="left:30%;animation-duration:12s;animation-delay:5s;">✨</span>
  <span class="float-emoji" style="left:50%;animation-duration:20s;animation-delay:1s;">🎈</span>
  <span class="float-emoji" style="left:65%;animation-duration:16s;animation-delay:3s;">🎉</span>
  <span class="float-emoji" style="left:78%;animation-duration:11s;animation-delay:7s;">🍀</span>
  <span class="float-emoji" style="left:90%;animation-duration:17s;animation-delay:4s;">💫</span>
  <span class="float-emoji" style="left:22%;animation-duration:15s;animation-delay:6s;">🌈</span>
  <span class="float-emoji" style="left:42%;animation-duration:19s;animation-delay:9s;">🚀</span>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════
PRAISE = [
    "🎉 Tuyệt vời! Thông minh quá!",
    "⭐ Chính xác! Giỏi lắm!",
    "🌟 Đúng rồi! Cố lên nhé!",
    "🏆 Xuất sắc! Học rất giỏi!",
    "🎊 Đúng rồi! Tài năng thật!",
    "🥳 Chính xác! Thông minh quá!",
    "💫 Hoàn hảo! Làm tiếp nào!",
    "🚀 Siêu đỉnh! Bạn quá giỏi!",
    "🎯 Bắn trúng đích! Xuất sắc!",
    "🦁 Dũng cảm! Tự tin lên!",
]

MASCOTS = {
    "perfect":   "🦁",
    "superstar": "🌟",
    "great":     "🐯",
    "good":      "🐻",
    "try":       "🐨",
}


# ══════════════════════════════════════════════════════════════════════════════
# GOOGLE SHEETS INTEGRATION
# ══════════════════════════════════════════════════════════════════════════════
def save_to_google_sheet(data: dict):
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        creds_dict = st.secrets.get("gcp_service_account", None)
        if creds_dict is None:
            st.markdown('<div class="gs-error">⚠️ Chưa cấu hình [gcp_service_account] trong Secrets.</div>', unsafe_allow_html=True)
            return
        creds  = Credentials.from_service_account_info(dict(creds_dict), scopes=scopes)
        client = gspread.authorize(creds)
        sheet_id = st.secrets.get("google_sheet_id", "").strip()
        if not sheet_id:
            sheet_id = "1vo-EhmSYZ6hkQT1TQoPmJ2IcRXzUfzEgaFZTkkBrat4"
        sh = client.open_by_key(sheet_id)
        ws = sh.sheet1
        try:
            first_row = ws.row_values(1)
        except Exception:
            first_row = []
        if not first_row or first_row[0] != "Tên học sinh":
            ws.insert_row(
                ["Tên học sinh","Lớp","Môn học","Chủ đề",
                 "Câu đúng","Tổng câu","Điểm tích lũy","Huy hiệu","Thời gian"],
                index=1,
            )
        row = [
            data.get("name",""), data.get("class_name","Lớp 2"),
            data.get("subject",""), data.get("topic",""),
            data.get("score",0), data.get("total",0),
            data.get("points",0), data.get("badge",""),
            str(data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))),
        ]
        ws.append_row(row, value_input_option="USER_ENTERED")
        st.markdown('<div class="gs-success">✅ Đã lưu kết quả vào Google Sheets!</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="gs-error">⚠️ Chưa kết nối Google Sheets. Kết quả vẫn hiển thị bình thường.<br><small>{e}</small></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
def init_state():
    defaults = {
        "screen":         "onboard",
        "username":       "",
        "class_name":     "Lớp 2",
        "subject":        None,
        "topic_idx":      None,
        "q_idx":          0,
        "score":          0,
        "answered":       False,
        "selected":       None,
        "fill_input":     "",
        "fill_submitted": False,
        "shuffled_qs":    [],
        "recent":         None,
        "total_pts":      0,
        "streak":         0,
        "best_streak":    0,
        "badge_history":  [],
        "leaderboard":    [],
        "bonus_this":     0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════
def get_level(pts: int) -> int:
    return max(1, pts // 50 + 1)


def get_badge_for_result(score: int, total: int, streak: int) -> dict:
    pct = score / total if total else 0
    if pct == 1.0 and streak >= 5:
        return {"key": "superstar", "label": "🔥 Siêu Sao!",  "css": "badge-superstar"}
    elif pct == 1.0:
        return {"key": "gold",      "label": "🥇 Vàng",        "css": "badge-gold"}
    elif score >= 8:
        return {"key": "silver",    "label": "🥈 Bạc",         "css": "badge-silver"}
    elif score >= 5:
        return {"key": "bronze",    "label": "🥉 Đồng",        "css": "badge-bronze"}
    else:
        return {"key": "try",       "label": "💪 Cố Gắng!",    "css": "badge-try"}


def go_home():
    st.session_state.screen = "home"


def go_topics(subj: str):
    st.session_state.subject = subj
    st.session_state.screen  = "topics"


def go_quiz(topic_idx: int):
    subj = st.session_state.subject
    topic = SUBJECTS[subj]["topics"][topic_idx]
    gen_key = topic.get("auto_gen")
    if gen_key and gen_key in AUTO_GEN_MAP:
        shuffled = AUTO_GEN_MAP[gen_key]()
    else:
        topic_data = topic["qs"]
        sample_size = min(10, len(topic_data))
        shuffled = random.sample(topic_data, sample_size)

    st.session_state.update({
        "topic_idx":      topic_idx,
        "shuffled_qs":    shuffled,
        "q_idx":          0,
        "score":          0,
        "answered":       False,
        "selected":       None,
        "fill_input":     "",
        "fill_submitted": False,
        "streak":         0,
        "bonus_this":     0,
        "screen":         "quiz",
    })


def answer_mcq(i: int):
    if st.session_state.answered:
        return
    st.session_state.selected  = i
    st.session_state.answered  = True
    st.session_state.bonus_this = 0
    q = st.session_state.shuffled_qs[st.session_state.q_idx]
    _evaluate_answer(i == q["ans"])


def answer_fill(user_text: str, correct_text: str):
    if st.session_state.answered:
        return
    st.session_state.fill_submitted = True
    st.session_state.answered = True
    st.session_state.bonus_this = 0
    is_correct = user_text.strip().lower() == correct_text.strip().lower()
    _evaluate_answer(is_correct)


def _evaluate_answer(is_correct: bool):
    if is_correct:
        st.session_state.score     += 1
        st.session_state.total_pts += 10
        st.session_state.streak    += 1
        if st.session_state.streak > st.session_state.best_streak:
            st.session_state.best_streak = st.session_state.streak
        bonus = 0
        if st.session_state.streak == 5:
            bonus = 10
        elif st.session_state.streak == 3:
            bonus = 5
        if bonus:
            st.session_state.total_pts += bonus
            st.session_state.bonus_this = bonus
    else:
        st.session_state.streak = 0


def next_q():
    st.session_state.q_idx        += 1
    st.session_state.answered      = False
    st.session_state.selected      = None
    st.session_state.fill_input    = ""
    st.session_state.fill_submitted = False
    st.session_state.bonus_this    = 0
    if st.session_state.q_idx >= len(st.session_state.shuffled_qs):
        _finish_quiz()


def _finish_quiz():
    subj       = st.session_state.subject
    topic_idx  = st.session_state.topic_idx
    score      = st.session_state.score
    total      = len(st.session_state.shuffled_qs)
    pts        = st.session_state.total_pts
    name       = st.session_state.username
    class_name = st.session_state.class_name
    streak     = st.session_state.best_streak
    badge      = get_badge_for_result(score, total, streak)
    topic_name = SUBJECTS[subj]["topics"][topic_idx]["name"]
    subj_label = SUBJECTS[subj]["label"]

    st.session_state.recent = {
        "name":  topic_name,
        "subj":  subj_label,
        "badge": SUBJECTS[subj]["badge"],
        "score": score,
        "total": total,
    }
    st.session_state.badge_history.append({
        "label": badge["label"],
        "css":   badge["css"],
        "topic": topic_name,
    })
    lb = st.session_state.leaderboard
    lb.append({"name": name, "pts": pts, "badge": badge["label"]})
    lb.sort(key=lambda x: x["pts"], reverse=True)
    st.session_state.leaderboard = lb[:10]

    save_to_google_sheet({
        "name":       name,
        "class_name": class_name,
        "subject":    subj_label,
        "topic":      topic_name,
        "score":      score,
        "total":      total,
        "points":     pts,
        "badge":      badge["label"],
        "timestamp":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    st.session_state.screen = "result"


# ══════════════════════════════════════════════════════════════════════════════
# RENDER HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def render_sound(correct: bool):
    if correct:
        js = ("<script>(function(){var c=new(window.AudioContext||window.webkitAudioContext)();"
              "function tone(f,t,d){var o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);"
              "o.type='sine';o.frequency.value=f;g.gain.setValueAtTime(0.3,t);g.gain.exponentialRampToValueAtTime(0.001,t+d);"
              "o.start(t);o.stop(t+d);}tone(880,c.currentTime,0.15);tone(1100,c.currentTime+0.15,0.15);"
              "tone(1320,c.currentTime+0.3,0.3);})();</script>")
    else:
        js = ("<script>(function(){var c=new(window.AudioContext||window.webkitAudioContext)();"
              "var o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);"
              "o.type='sawtooth';o.frequency.setValueAtTime(300,c.currentTime);"
              "o.frequency.exponentialRampToValueAtTime(100,c.currentTime+0.4);"
              "g.gain.setValueAtTime(0.2,c.currentTime);g.gain.exponentialRampToValueAtTime(0.001,c.currentTime+0.4);"
              "o.start(c.currentTime);o.stop(c.currentTime+0.4);})();</script>")
    st.markdown(js, unsafe_allow_html=True)


def render_celebration_sound():
    js = ("<script>(function(){var c=new(window.AudioContext||window.webkitAudioContext)();"
          "var notes=[523,659,784,1047,1319];notes.forEach(function(f,i){"
          "var o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);"
          "o.type='sine';o.frequency.value=f;var t=c.currentTime+i*0.15;"
          "g.gain.setValueAtTime(0.25,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.3);"
          "o.start(t);o.stop(t+0.3);});})();</script>")
    st.markdown(js, unsafe_allow_html=True)


def render_confetti():
    colors = ["#FF6B6B","#FF9A3C","#FFD93D","#6BCB77","#4D96FF","#a855f7","#FF69B4","#00ffcc"]
    pieces = ""
    for i in range(50):
        c   = random.choice(colors)
        lft = random.randint(0, 100)
        dur = random.uniform(1.5, 3.5)
        dly = random.uniform(0, 1.5)
        sz  = random.randint(8, 15)
        rot = random.randint(0, 360)
        pieces += (f'<div class="confetti-piece" style="left:{lft}%;top:-20px;background:{c};'
                   f'width:{sz}px;height:{sz}px;animation-duration:{dur:.1f}s;'
                   f'animation-delay:{dly:.1f}s;transform:rotate({rot}deg);"></div>')
    st.markdown(f'<div style="pointer-events:none;position:relative;z-index:9999;">{pieces}</div>',
                unsafe_allow_html=True)


def render_left_panel():
    """Render Panel trái: thông tin học sinh + menu môn học."""
    name       = st.session_state.username or "Bạn"
    pts        = st.session_state.total_pts
    lv         = get_level(pts)
    streak     = st.session_state.streak
    class_name = st.session_state.class_name
    current_subj = st.session_state.get("subject")

    st.markdown(f"""
    <div class="left-panel">
        <div class="student-card">
            <span class="student-avatar">🦊</span>
            <div class="student-name">👋 {name}</div>
            <div class="student-class">{class_name}</div>
            <div class="stat-row">
                <div class="stat-item">
                    <div class="stat-val">⭐{pts}</div>
                    <div class="stat-lbl">Điểm</div>
                </div>
                <div class="stat-item">
                    <div class="stat-val">Lv.{lv}</div>
                    <div class="stat-lbl">Level</div>
                </div>
                <div class="stat-item">
                    <div class="stat-val">{'🔥' + str(streak) if streak >= 3 else '—'}</div>
                    <div class="stat-lbl">Streak</div>
                </div>
            </div>
        </div>
        <div class="panel-divider"></div>
        <div class="panel-section-title">📚 Môn học</div>
    </div>
    """, unsafe_allow_html=True)

    for subj_key, subj_data in SUBJECTS.items():
        tc = len(subj_data["topics"])
        label = f"{subj_data['icon']}  {subj_data['label']}  · {tc} chủ đề"
        btn_type = "primary" if current_subj == subj_key else "secondary"
        if st.button(label, key=f"nav_{subj_key}", use_container_width=True, type=btn_type):
            go_topics(subj_key)
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Trang Chủ", key="nav_home", use_container_width=True, type="secondary"):
        go_home()
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# SCREEN RENDERERS
# ══════════════════════════════════════════════════════════════════════════════
def render_screen_home():
    name = st.session_state.username
    st.markdown(
        f'<div class="greeting-box"><p class="greeting-text">Xin chào, {name}! 👋 Hôm nay học gì nào? 🎯</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="text-align:center;font-family:Nunito,sans-serif;font-size:38px;font-weight:900;'
        'color:#fff;margin-bottom:6px;text-shadow:0 4px 12px rgba(0,0,0,0.4);">🌟 Ôn Luyện Lớp 2</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="text-align:center;font-size:17px;color:rgba(255,255,255,0.55);'
        'font-weight:700;margin-bottom:24px;">Chọn môn ở bên trái để bắt đầu luyện tập! 🎮</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    card_style = (
        "border-radius:24px;padding:28px 14px;text-align:center;"
        "backdrop-filter:blur(10px);border:1.5px solid;"
    )
    with c1:
        st.markdown(
            f'<div style="{card_style}background:rgba(255,154,60,0.15);border-color:rgba(255,107,107,0.4);">'
            f'<span style="font-size:54px;">🔢</span>'
            f'<div style="font-size:20px;font-weight:800;color:#fff;margin-top:10px;">Toán học</div>'
            f'<div style="font-size:13px;color:rgba(255,255,255,0.5);font-weight:600;">'
            f'{len(SUBJECTS["math"]["topics"])} chủ đề</div></div>',
            unsafe_allow_html=True,
        )
        if st.button("➕ Học Toán", key="home_math", type="primary", use_container_width=True):
            go_topics("math"); st.rerun()
    with c2:
        st.markdown(
            f'<div style="{card_style}background:rgba(34,197,94,0.12);border-color:rgba(34,197,94,0.4);">'
            f'<span style="font-size:54px;">📖</span>'
            f'<div style="font-size:20px;font-weight:800;color:#fff;margin-top:10px;">Tiếng Việt</div>'
            f'<div style="font-size:13px;color:rgba(255,255,255,0.5);font-weight:600;">'
            f'{len(SUBJECTS["viet"]["topics"])} chủ đề</div></div>',
            unsafe_allow_html=True,
        )
        if st.button("✏️ Học Tiếng Việt", key="home_viet", type="primary", use_container_width=True):
            go_topics("viet"); st.rerun()
    with c3:
        st.markdown(
            f'<div style="{card_style}background:rgba(77,150,255,0.12);border-color:rgba(77,150,255,0.4);">'
            f'<span style="font-size:54px;">🔤</span>'
            f'<div style="font-size:20px;font-weight:800;color:#fff;margin-top:10px;">Tiếng Anh</div>'
            f'<div style="font-size:13px;color:rgba(255,255,255,0.5);font-weight:600;">'
            f'{len(SUBJECTS["eng"]["topics"])} chủ đề</div></div>',
            unsafe_allow_html=True,
        )
        if st.button("🌍 Học Tiếng Anh", key="home_eng", type="primary", use_container_width=True):
            go_topics("eng"); st.rerun()

    if st.session_state.recent:
        r = st.session_state.recent
        score_color = "#6ee7b7" if r["score"] >= 7 else "#fbbf24" if r["score"] >= 5 else "#fca5a5"
        st.markdown(f"""
        <div class="recent-box">
            <div class="recent-title">🕐 Kết quả gần đây</div>
            <div style="display:flex;align-items:center;gap:10px;font-size:15px;font-weight:700;color:rgba(255,255,255,0.85);">
                <span>{r['name']}</span>
                <span style="background:linear-gradient(135deg,#FF9A3C,#FF6B6B);color:#fff;font-size:11px;
                             font-weight:800;padding:3px 10px;border-radius:99px;">{r['subj']}</span>
                <span style="margin-left:auto;font-size:17px;font-weight:800;color:{score_color};">{r['score']}/{r['total']} ✅</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Mini leaderboard
    lb = st.session_state.leaderboard
    if lb:
        st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:16px;font-weight:800;color:rgba(255,255,255,0.7);margin-bottom:10px;">🏆 Bảng xếp hạng phiên này</div>',
            unsafe_allow_html=True,
        )
        for rank, entry in enumerate(lb[:5], 1):
            medal = ["🥇","🥈","🥉","4️⃣","5️⃣"][rank-1]
            st.markdown(
                f'<div style="display:flex;align-items:center;gap:10px;padding:8px 14px;'
                f'background:rgba(255,255,255,0.04);border-radius:12px;margin-bottom:6px;">'
                f'<span style="font-size:20px;">{medal}</span>'
                f'<span style="font-weight:700;color:#fff;flex:1;">{entry["name"]}</span>'
                f'<span style="font-weight:800;color:#FFD93D;">⭐{entry["pts"]}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )


def render_screen_topics():
    subj = st.session_state.subject
    sub  = SUBJECTS[subj]
    st.markdown(
        f'<div style="font-size:30px;font-weight:900;color:#fff;margin-bottom:4px;">'
        f'{sub["icon"]} {sub["label"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="font-size:15px;color:rgba(255,255,255,0.5);font-weight:700;margin-bottom:22px;">'
        'Chọn chủ đề để bắt đầu luyện tập! 🎯</div>',
        unsafe_allow_html=True,
    )
    for i, topic in enumerate(sub["topics"]):
        is_mixed = "mixed" in topic.get("auto_gen", "")
        card_cls = "topic-card topic-mixed" if is_mixed else "topic-card"
        t_col1, t_col2 = st.columns([4, 1])
        with t_col1:
            icon = "🌟" if is_mixed else "📚"
            st.markdown(
                f'<div class="{card_cls}">'
                f'<span style="font-size:22px;">{icon}</span>'
                f'{topic["name"]}</div>',
                unsafe_allow_html=True,
            )
        with t_col2:
            if st.button("▶ Bắt đầu", key=f"topic_{i}", type="primary", use_container_width=True):
                go_quiz(i)
                st.rerun()


def render_screen_quiz():
    subj     = st.session_state.subject
    sub      = SUBJECTS[subj]
    qs       = st.session_state.shuffled_qs
    q_idx    = st.session_state.q_idx
    total    = len(qs)
    answered = st.session_state.answered
    name     = st.session_state.username
    q        = qs[q_idx]
    q_type   = q.get("type", "mcq")

    # Header
    cnt_col, back_col = st.columns([3, 1])
    with cnt_col:
        icon_q = "📝" if q_type == "fill_blank" else "🔘"
        st.markdown(
            f'<div class="q-counter">Câu {q_idx + 1} / {total} {icon_q}</div>',
            unsafe_allow_html=True,
        )
    with back_col:
        if st.button("← Chủ đề", key="back_topics_quiz", type="secondary"):
            go_topics(subj); st.rerun()

    pct = int(((q_idx) / total) * 100)
    st.markdown(
        f'<div class="progress-outer"><div class="progress-inner" style="width:{pct}%;"></div></div>',
        unsafe_allow_html=True,
    )

    # Streak banner
    streak = st.session_state.streak
    if not answered and streak >= 3:
        fire = "🔥🔥🔥" if streak >= 5 else "🔥🔥"
        st.markdown(
            f'<div class="streak-banner">{fire} Chuỗi đúng {streak} câu liên tiếp! Siêu đỉnh!</div>',
            unsafe_allow_html=True,
        )

    # Question box
    st.markdown(
        f'<div class="{sub["q_box_class"]}"><p class="q-text">{q["q"]}</p></div>',
        unsafe_allow_html=True,
    )

    # Answer rendering
    if q_type == "mcq":
        selected = st.session_state.selected
        for i, opt in enumerate(q["opts"]):
            is_correct  = (i == q["ans"])
            is_selected = (i == selected)
            if not answered:
                if st.button(opt, key=f"opt_{q_idx}_{i}", use_container_width=True, type="secondary"):
                    answer_mcq(i)
                    st.rerun()
            else:
                if is_correct:
                    st.markdown(f'<div class="opt-correct">✅ {opt}</div>', unsafe_allow_html=True)
                elif is_selected and not is_correct:
                    st.markdown(f'<div class="opt-wrong">❌ {opt}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="opt-dim">{opt}</div>', unsafe_allow_html=True)
    else:
        # Fill blank
        st.markdown('<div class="fill-label">✍️ Điền câu trả lời của em:</div>', unsafe_allow_html=True)
        correct_text = q.get("ans_text", "")
        if not answered:
            fill_val = st.text_input(
                "Câu trả lời:",
                key=f"fill_{q_idx}",
                placeholder="Gõ câu trả lời vào đây...",
                label_visibility="collapsed",
            )
            if st.button("✅ Kiểm tra", key=f"check_{q_idx}", type="primary", use_container_width=True):
                if fill_val.strip() == "":
                    st.warning("⚠️ Em chưa nhập câu trả lời!")
                else:
                    answer_fill(fill_val, correct_text)
                    st.rerun()

    # Feedback after answering
    if answered:
        if q_type == "mcq":
            is_correct = (st.session_state.selected == q["ans"])
        else:
            user_ans   = st.session_state.get(f"fill_{q_idx}", "")
            is_correct = user_ans.strip().lower() == q.get("ans_text", "").strip().lower()

        if is_correct:
            praise = random.choice(PRAISE)
            render_sound(True)
            if st.session_state.bonus_this:
                st.markdown(
                    f'<div class="bonus-banner">🎁 STREAK BONUS +{st.session_state.bonus_this} điểm! Tuyệt vời!</div>',
                    unsafe_allow_html=True,
                )
            st.markdown(f"""
            <div class="feedback-correct">
                <span class="feedback-correct-emoji">🌟</span>
                <div class="feedback-correct-title">Giỏi quá {name}! +10 điểm ⭐</div>
                <div class="feedback-correct-msg">{praise} Tiếp tục phát huy nhé! 🚀</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            render_sound(False)
            correct_display = q["opts"][q["ans"]] if q_type == "mcq" else q.get("ans_text", "")
            st.markdown(f"""
            <div class="feedback-wrong">
                <div class="feedback-wrong-title">😅 Ồ chưa đúng rồi {name}! Không sao, xem lại nhé!</div>
                <div class="feedback-answer">✅ Đáp án đúng: <strong>{correct_display}</strong></div>
                <div class="explain-title">📚 Giải thích</div>
                <div class="feedback-explain">{q.get("explain","")}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        next_label = "Câu tiếp theo →" if q_idx < total - 1 else "🏁 Xem kết quả →"
        if st.button(next_label, key="next_q", type="primary", use_container_width=True):
            next_q()
            st.rerun()


def render_screen_result():
    score  = st.session_state.score
    total  = len(st.session_state.shuffled_qs)
    pts    = st.session_state.total_pts
    bstrk  = st.session_state.best_streak
    name   = st.session_state.username
    badge  = get_badge_for_result(score, total, bstrk)

    if badge["key"] == "superstar":
        mascot = MASCOTS["superstar"]
        title  = "🔥 Siêu Sao Hoàn Hảo!"
        msg    = f"Xuất sắc {name}! {total}/{total} câu đúng + chuỗi {bstrk}! Bạn là thiên tài! 🚀"
        render_celebration_sound(); render_confetti(); st.balloons()
    elif badge["key"] == "gold":
        mascot = MASCOTS["perfect"]
        title  = "🏆 Hoàn Hảo!"
        msg    = f"Tuyệt vời {name}! Đúng tất cả {total}/{total} câu!"
        render_celebration_sound(); render_confetti(); st.balloons()
    elif badge["key"] == "silver":
        mascot = MASCOTS["great"]
        title  = "⭐ Xuất Sắc!"
        msg    = f"Tuyệt vời {name}! Đúng {score}/{total} câu!"
        st.balloons()
    elif badge["key"] == "bronze":
        mascot = MASCOTS["good"]
        title  = "👍 Khá Tốt!"
        msg    = f"Cố lên {name}! Đúng {score}/{total} câu!"
    else:
        mascot = MASCOTS["try"]
        title  = "💪 Cố Lên Nào!"
        msg    = f"Không sao {name}! Luyện thêm rồi thử lại nhé! {score}/{total} câu đúng."

    st.markdown(f"""
    <div class="result-wrap">
        <span class="result-trophy">{mascot}</span>
        <div class="result-title">{title}</div>
        <div class="result-msg">{msg}</div>
        <span class="badge-earned {badge['css']}">{badge['label']}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="total-pts-box">
        <span class="total-pts-icon">⭐</span>
        <div>
            <div class="total-pts-val">{pts} điểm</div>
            <div class="total-pts-lbl">Level {get_level(pts)} · Streak tốt nhất: {bstrk}</div>
        </div>
        <span class="total-pts-icon">🎮</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="score-grid">
        <div class="score-box-correct">
            <div class="score-num" style="color:#6ee7b7;">{score}</div>
            <div class="score-lbl">Câu đúng ✅</div>
        </div>
        <div class="score-box-wrong">
            <div class="score-num" style="color:#fca5a5;">{total - score}</div>
            <div class="score-lbl">Câu sai ❌</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    bh = st.session_state.badge_history
    if len(bh) > 1:
        chips = "".join(
            f'<span class="badge-chip {b["css"]}" title="{b["topic"]}">{b["label"]}</span>'
            for b in bh[-8:]
        )
        st.markdown(
            f'<div class="badge-history-box">'
            f'<div class="badge-history-title">🎖️ Huy Hiệu Đã Đạt</div>'
            f'<div class="badge-history-row">{chips}</div></div>',
            unsafe_allow_html=True,
        )

    r1, r2, r3 = st.columns(3)
    with r1:
        if st.button("🔄 Luyện lại", key="retry", type="secondary", use_container_width=True):
            go_quiz(st.session_state.topic_idx); st.rerun()
    with r2:
        if st.button("📚 Chủ đề khác", key="other_topic", type="primary", use_container_width=True):
            go_topics(st.session_state.subject); st.rerun()
    with r3:
        if st.button("🏠 Trang Chủ", key="home_result", type="secondary", use_container_width=True):
            go_home(); st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# MAIN LAYOUT – ROUTING
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == "onboard":
    # Full-width onboarding screen
    col_c = st.columns([1, 2, 1])[1]
    with col_c:
        st.markdown("""
        <div class="onboard-wrap">
            <span class="onboard-mascot">🦊</span>
            <div class="onboard-title">Chào mừng đến với<br>Thế Giới Học Tập! 🌈</div>
            <div class="onboard-sub">Học vui – Hiểu nhanh – Nhớ lâu ✨</div>
            <span class="star-row">⭐ ⭐ ⭐ ⭐ ⭐</span>
        </div>
        """, unsafe_allow_html=True)

        name_input = st.text_input(
            "🎮 Tên hoặc biệt danh của bạn:",
            placeholder="Ví dụ: Siêu Sao, Nam Ngầu, Bé Kute...",
            max_chars=20,
        )
        class_options = ["Lớp 1", "Lớp 2", "Lớp 3"]
        class_choice  = st.selectbox("🏫 Chọn lớp của bạn:", class_options, index=1)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Bắt đầu học ngay!", key="btn_start", type="primary", use_container_width=True):
            name = name_input.strip()
            if not name:
                st.warning("⚠️ Bạn chưa nhập tên! Nhập tên để bắt đầu nhé 😊")
            else:
                st.session_state.username   = name
                st.session_state.class_name = class_choice
                st.session_state.screen     = "home"
                st.rerun()

else:
    # Two-column layout for all other screens
    left_col, right_col = st.columns([1, 2.8], gap="medium")

    with left_col:
        render_left_panel()

    with right_col:
        screen = st.session_state.screen
        if screen == "home":
            render_screen_home()
        elif screen == "topics":
            render_screen_topics()
        elif screen == "quiz":
            render_screen_quiz()
        elif screen == "result":
            render_screen_result()
