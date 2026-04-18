import streamlit as st
import random
from datetime import datetime

# ══════════════════════════════════════════════════════════════════════════════
# CẤU HÌNH TRANG – layout="wide" để dùng st.columns chia 2 cột
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="🌟 Siêu Sao Lớp 2",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
# MODULE SINH CÂU HỎI TOÁN TỰ ĐỘNG
# ══════════════════════════════════════════════════════════════════════════════
def generate_math_addition(num_qs=10):
    """Sinh ngẫu nhiên phép cộng có nhớ, kết hợp trắc nghiệm và tự luận."""
    qs = []
    for i in range(num_qs):
        b = random.randint(3, 9)
        a_unit = random.randint(10 - b + 1, 9)
        a_tens = random.randint(1, 8) * 10
        a = a_tens + a_unit
        ans = a + b
        explain = (f"📝 Cách tính: {a} + {b}\n"
                   f"→ Lấy {a} + {10 - a_unit} = {a_tens + 10} (tròn chục)\n"
                   f"→ Còn thừa {b - (10 - a_unit)}, lấy {a_tens + 10} + {b - (10 - a_unit)} = {ans} ✔")

        # Xen kẽ: câu lẻ → tự luận (fill_blank), câu chẵn → trắc nghiệm
        if i % 3 == 2:
            qs.append({
                "type":    "fill_blank",
                "q":       f"Tính: {a} + {b} = ___",
                "ans_text": str(ans),
                "explain": explain,
            })
        else:
            opts = [str(ans), str(ans - 1), str(ans + 1), str(ans + 10)]
            random.shuffle(opts)
            qs.append({
                "type":    "mcq",
                "q":       f"{a} + {b} = ?",
                "opts":    opts,
                "ans":     opts.index(str(ans)),
                "explain": explain,
            })
    return qs


def generate_math_subtraction(num_qs=10):
    """Sinh ngẫu nhiên phép trừ có nhớ, kết hợp trắc nghiệm và tự luận."""
    qs = []
    for i in range(num_qs):
        a_unit = random.randint(1, 8)
        a_tens = random.randint(2, 9) * 10
        a = a_tens + a_unit
        b = random.randint(a_unit + 1, 9)
        ans = a - b
        explain = (f"📝 Cách tính: {a} - {b}\n"
                   f"→ Lấy {a} - {a_unit} = {a_tens}\n"
                   f"→ Còn trừ {b - a_unit}, lấy {a_tens} - {b - a_unit} = {ans} ✔")

        if i % 3 == 2:
            qs.append({
                "type":    "fill_blank",
                "q":       f"Tính: {a} - {b} = ___",
                "ans_text": str(ans),
                "explain": explain,
            })
        else:
            opts = [str(ans), str(ans - 1), str(ans + 1), str(ans - 10)]
            random.shuffle(opts)
            qs.append({
                "type":    "mcq",
                "q":       f"{a} - {b} = ?",
                "opts":    opts,
                "ans":     opts.index(str(ans)),
                "explain": explain,
            })
    return qs


def generate_math_word_problems(num_qs=10):
    """Sinh ngẫu nhiên bài toán có lời văn lớp 2."""
    templates = [
        lambda: _word_prob_add(),
        lambda: _word_prob_sub(),
    ]
    qs = []
    for i in range(num_qs):
        fn = random.choice(templates)
        qs.append(fn())
    return qs


def _word_prob_add():
    a = random.randint(10, 50)
    b = random.randint(5, 30)
    ans = a + b
    items = random.choice(["quả táo", "cái kẹo", "bông hoa", "quyển sách", "viên bi"])
    explain = f"📝 Tất cả = {a} + {b} = {ans} {items} ✔"
    # Câu có lời văn → dạng tự luận điền số
    return {
        "type":    "fill_blank",
        "q":       f"An có {a} {items}. Bình cho An thêm {b} {items}.\nAn có tất cả bao nhiêu {items}? ___ {items}",
        "ans_text": str(ans),
        "explain": explain,
    }


def _word_prob_sub():
    total = random.randint(20, 60)
    used  = random.randint(5, total - 5)
    ans   = total - used
    items = random.choice(["quả cam", "tờ giấy", "chiếc bánh", "cái bút", "hạt đậu"])
    explain = f"📝 Còn lại = {total} - {used} = {ans} {items} ✔"
    return {
        "type":    "fill_blank",
        "q":       f"Trong hộp có {total} {items}.\nLấy ra {used} {items}. Còn lại bao nhiêu {items}? ___ {items}",
        "ans_text": str(ans),
        "explain": explain,
    }


# ══════════════════════════════════════════════════════════════════════════════
# CSS TOÀN CỤC – GIAO DIỆN TRẺ EM VUI NHỘN (nâng cấp 2-cột)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Baloo 2', cursive !important; }
.stApp {
    background-color: #FFF4FC;
    background-image:
        radial-gradient(circle at 10% 20%, #FFD6E8 0%, transparent 40%),
        radial-gradient(circle at 90% 10%, #C8F0FF 0%, transparent 40%),
        radial-gradient(circle at 50% 95%, #D4FFD6 0%, transparent 40%),
        radial-gradient(circle at 80% 80%, #FFF3B0 0%, transparent 30%),
        radial-gradient(#FFD93D18 1.5px, transparent 1.5px),
        radial-gradient(#FF6BCB18 1.5px, transparent 1.5px);
    background-size: 100% 100%, 100% 100%, 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    background-position: 0 0, 0 0, 0 0, 0 0, 0 0, 20px 20px;
}
header[data-testid="stHeader"] { display: none; }
/* Giảm padding để layout rộng hơn */
.block-container { padding-top: 0.5rem !important; padding-left: 1.5rem !important; padding-right: 1.5rem !important; max-width: 100% !important; }

/* ── PANEL TRÁI (thông tin + chủ đề) ── */
.left-panel {
    background: linear-gradient(160deg, #1a1a2e 0%, #16213e 100%);
    border-radius: 28px;
    padding: 24px 18px;
    min-height: 80vh;
    box-shadow: 0 8px 32px rgba(26,26,46,0.35);
    position: sticky;
    top: 0.5rem;
}
.student-card {
    background: rgba(255,255,255,0.08);
    border: 1.5px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 16px;
    margin-bottom: 20px;
    text-align: center;
}
.student-avatar { font-size: 52px; margin-bottom: 6px; display: block; animation: wobble 3s infinite; }
.student-name { font-size: 20px; font-weight: 800; color: #FFD93D; margin: 0 0 4px; }
.student-class { font-size: 13px; color: #9ca3af; font-weight: 600; }
.stat-row { display: flex; justify-content: space-around; margin-top: 12px; }
.stat-item { text-align: center; }
.stat-val  { font-size: 22px; font-weight: 800; color: #FF9A3C; }
.stat-lbl  { font-size: 10px; color: #6b7280; font-weight: 700; text-transform: uppercase; }

.panel-section-title {
    font-size: 11px; font-weight: 800; color: #6b7280;
    text-transform: uppercase; letter-spacing: .1em;
    margin: 0 0 10px; padding: 0 2px;
}
.subject-btn-math {
    background: linear-gradient(135deg, #FF9A3C, #FF6B6B);
    border-radius: 18px; padding: 14px 16px; margin-bottom: 10px;
    cursor: pointer; transition: transform .2s;
    display: flex; align-items: center; gap: 12px;
    box-shadow: 0 4px 14px rgba(255,107,107,0.35);
}
.subject-btn-viet {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    border-radius: 18px; padding: 14px 16px; margin-bottom: 10px;
    cursor: pointer; transition: transform .2s;
    display: flex; align-items: center; gap: 12px;
    box-shadow: 0 4px 14px rgba(34,197,94,0.35);
}
.subject-btn-eng {
    background: linear-gradient(135deg, #4D96FF, #1d4ed8);
    border-radius: 18px; padding: 14px 16px; margin-bottom: 10px;
    cursor: pointer; transition: transform .2s;
    display: flex; align-items: center; gap: 12px;
    box-shadow: 0 4px 14px rgba(77,150,255,0.35);
}
.subject-btn-icon { font-size: 30px; }
.subject-btn-text { color: #fff; font-weight: 800; font-size: 15px; }
.subject-btn-sub  { color: rgba(255,255,255,0.7); font-size: 12px; font-weight: 600; }

.topic-pill {
    background: rgba(255,255,255,0.07);
    border: 1.5px solid rgba(255,255,255,0.12);
    border-radius: 14px; padding: 10px 14px; margin-bottom: 8px;
    color: #e2e8f0; font-size: 14px; font-weight: 700;
    cursor: pointer; transition: all .2s;
}
.topic-pill:hover { background: rgba(255,255,255,0.14); border-color: #FFD93D; color: #FFD93D; }
.topic-pill-active { background: rgba(255,217,61,0.18) !important; border-color: #FFD93D !important; color: #FFD93D !important; }

/* ── PANEL PHẢI (nội dung) ── */
.float-emoji-wrap { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; overflow: hidden; }
.float-emoji { position: absolute; font-size: 28px; opacity: 0.12; animation: floatUp linear infinite; }
@keyframes floatUp { 0% { transform: translateY(110vh) rotate(0deg); opacity: 0.12; } 100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; } }
.confetti-piece { position: fixed; width: 10px; height: 10px; border-radius: 2px; animation: confettiFall linear forwards; z-index: 9999; pointer-events: none; }
@keyframes confettiFall { 0% { transform: translateY(-20px) rotate(0deg); opacity: 1; } 100% { transform: translateY(100vh) rotate(720deg); opacity: 0; } }

.onboard-wrap { text-align: center; padding: 20px 0 10px; animation: fadeSlideUp 0.7s ease both; position: relative; z-index: 1; }
.onboard-mascot { font-size: 110px; line-height: 1; margin-bottom: 10px; display: block; animation: wobble 2s infinite; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.15)); }
.onboard-title { font-family: 'Nunito', sans-serif; font-size: 38px; font-weight: 900; background: linear-gradient(135deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF, #a855f7); background-size: 300%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradShift 4s ease infinite; margin: 0 0 8px; line-height: 1.2; }
.onboard-sub { font-size: 18px; color: #7c3aed; font-weight: 700; margin: 0 0 20px; }
.star-row { font-size: 28px; letter-spacing: 8px; margin-bottom: 24px; animation: bounce 1.5s infinite; display: block; }

.greeting-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 14px 20px; margin-bottom: 18px; text-align: center; box-shadow: 0 8px 24px rgba(102,126,234,0.4); animation: fadeSlideUp 0.5s ease; position: relative; z-index: 1; }
.greeting-text { font-size: 21px; font-weight: 800; color: #fff; margin: 0; }

/* Hộp câu hỏi – font lớn hơn cho mắt trẻ lớp 2 */
.q-box-math { background: linear-gradient(135deg, #FF9A3C 0%, #FF6B6B 50%, #c2410c 100%); border-radius: 26px; padding: 32px 24px; text-align: center; margin-bottom: 20px; box-shadow: 0 10px 32px rgba(255,107,107,0.45); position: relative; overflow: hidden; animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1); z-index: 1; }
.q-box-viet { background: linear-gradient(135deg, #22c55e 0%, #16a34a 50%, #166534 100%); border-radius: 26px; padding: 32px 24px; text-align: center; margin-bottom: 20px; box-shadow: 0 10px 32px rgba(34,197,94,0.45); position: relative; overflow: hidden; animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1); z-index: 1; }
.q-box-eng  { background: linear-gradient(135deg, #4D96FF 0%, #1d4ed8 50%, #1e3a8a 100%); border-radius: 26px; padding: 32px 24px; text-align: center; margin-bottom: 20px; box-shadow: 0 10px 32px rgba(77,150,255,0.45); position: relative; overflow: hidden; animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1); z-index: 1; }
.q-box-math::before, .q-box-viet::before, .q-box-eng::before { content: '✨'; position: absolute; top: 10px; right: 16px; font-size: 30px; animation: sparkle 1s ease infinite alternate; }
.q-box-math::after { content: '🔢'; position: absolute; bottom: 10px; left: 16px; font-size: 28px; opacity: 0.4; }
.q-box-viet::after { content: '📖'; position: absolute; bottom: 10px; left: 16px; font-size: 28px; opacity: 0.4; }
.q-box-eng::after  { content: '🔤'; position: absolute; bottom: 10px; left: 16px; font-size: 28px; opacity: 0.4; }
/* Font size lớn – phù hợp mắt học sinh lớp 2 */
.q-text { font-size: 30px; font-weight: 800; color: #fff; margin: 0; line-height: 1.5; text-shadow: 0 3px 8px rgba(0,0,0,0.25); white-space: pre-line; }

/* Câu tự luận */
.fill-label { font-size: 15px; font-weight: 800; color: #7c3aed; margin: 0 0 6px; text-transform: uppercase; letter-spacing: .06em; }
div[data-testid="stTextInput"] input {
    font-family: 'Baloo 2', cursive !important;
    font-size: 26px !important; font-weight: 800 !important;
    border-radius: 16px !important; border: 3px solid #e9d5ff !important;
    padding: 14px 20px !important; background: #fff !important; color: #1a1a2e !important;
    text-align: center !important;
}
div[data-testid="stTextInput"] input:focus { border-color: #a855f7 !important; box-shadow: 0 0 0 4px rgba(168,85,247,0.15) !important; }

.opt-correct { background: linear-gradient(135deg, #DCFCE7, #BBF7D0); border: 3px solid #22c55e; border-radius: 18px; padding: 18px 20px; font-size: 20px; font-weight: 800; color: #14532d; width: 100%; text-align: left; margin-bottom: 10px; display: block; box-shadow: 0 4px 16px rgba(34,197,94,0.3); animation: popIn 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); }
.opt-wrong   { background: linear-gradient(135deg, #FEE2E2, #fca5a5); border: 3px solid #ef4444; border-radius: 18px; padding: 18px 20px; font-size: 20px; font-weight: 800; color: #7f1d1d; width: 100%; text-align: left; margin-bottom: 10px; display: block; animation: shake 0.4s ease; }
.opt-dim     { background: #f3f4f6; border: 2px solid #e5e7eb; border-radius: 18px; padding: 18px 20px; font-size: 20px; font-weight: 600; color: #9ca3af; width: 100%; text-align: left; margin-bottom: 10px; display: block; opacity: 0.5; }

.feedback-correct { background: linear-gradient(135deg, #DCFCE7, #D1FAE5); border: 3px solid #86efac; border-radius: 22px; padding: 22px 24px; margin-top: 6px; animation: popIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); text-align: center; box-shadow: 0 6px 20px rgba(34,197,94,0.2); }
.feedback-correct-emoji { font-size: 52px; display: block; margin-bottom: 4px; animation: bounce 1s infinite; }
.feedback-correct-title { font-size: 26px; font-weight: 800; color: #14532d; margin: 0 0 6px; }
.feedback-correct-msg   { font-size: 17px; font-weight: 600; color: #166534; margin: 0; }
.feedback-wrong { background: linear-gradient(135deg, #FFF7ED, #FEF3C7); border: 3px dashed #FB923C; border-radius: 22px; padding: 20px 22px; margin-top: 6px; animation: popIn 0.3s ease; box-shadow: 0 4px 16px rgba(251,146,60,0.15); }
.feedback-wrong-title { font-size: 21px; font-weight: 800; color: #c2410c; margin: 0 0 12px; text-align: center; }
.feedback-answer  { background: #DCFCE7; border: 2px solid #22c55e; border-radius: 14px; padding: 12px 16px; font-size: 18px; font-weight: 800; color: #14532d; margin-bottom: 10px; }
.feedback-explain { background: #FEF9C3; border: 2px solid #FCD34D; border-radius: 14px; padding: 12px 16px; font-size: 16px; font-weight: 600; color: #78350f; line-height: 1.8; white-space: pre-line; }
.explain-title { font-size: 13px; font-weight: 800; color: #92400e; text-transform: uppercase; letter-spacing: .06em; margin-bottom: 6px; }

.progress-outer { background: #e9d5ff; border-radius: 99px; height: 22px; margin-bottom: 16px; overflow: hidden; border: 2px solid #c4b5fd; position: relative; z-index: 1; }
.progress-inner { height: 22px; background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF, #a855f7); background-size: 400% 100%; border-radius: 99px; animation: shimmer 3s linear infinite; transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); position: relative; }
.progress-inner::after { content: '⭐'; position: absolute; right: -8px; top: -4px; font-size: 24px; animation: sparkle 0.8s ease infinite alternate; }
.q-counter { font-size: 16px; font-weight: 800; color: #7c3aed; text-align: right; margin-bottom: 6px; }

.streak-banner { background: linear-gradient(135deg, #FF6B6B, #FF9A3C); border-radius: 16px; padding: 10px 16px; text-align: center; font-size: 20px; font-weight: 800; color: #fff; margin-bottom: 12px; animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1); box-shadow: 0 6px 20px rgba(255,107,107,0.4); }
.bonus-banner  { background: linear-gradient(135deg, #FFD93D, #FF9A3C); border-radius: 16px; padding: 8px 16px; text-align: center; font-size: 18px; font-weight: 800; color: #1a1a2e; margin-bottom: 10px; animation: popIn 0.4s cubic-bezier(0.34,1.56,0.64,1); box-shadow: 0 4px 14px rgba(255,217,61,0.4); }

.result-wrap { text-align: center; padding: 10px 0 20px; animation: fadeSlideUp 0.7s ease both; position: relative; z-index: 1; }
.result-trophy { font-size: 100px; margin-bottom: 8px; display: block; animation: bounce 1.6s infinite; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.2)); }
.result-title  { font-family: 'Nunito', sans-serif; font-size: 40px; font-weight: 900; color: #1a1a2e; margin: 0 0 6px; }
.result-msg    { font-size: 18px; color: #6b7280; font-weight: 600; margin: 0 0 22px; }
.badge-earned  { display: inline-block; font-size: 17px; font-weight: 800; padding: 12px 28px; border-radius: 99px; margin-bottom: 20px; box-shadow: 0 6px 18px rgba(0,0,0,0.18); animation: popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.3s both; }
.badge-gold      { background: linear-gradient(135deg, #FFD700, #FF9A3C); color: #fff; }
.badge-silver    { background: linear-gradient(135deg, #a855f7, #7c3aed); color: #fff; }
.badge-bronze    { background: linear-gradient(135deg, #22c55e, #16a34a); color: #fff; }
.badge-try       { background: linear-gradient(135deg, #64748b, #475569); color: #fff; }
.badge-superstar { background: linear-gradient(135deg, #FFD700, #FF6B6B, #a855f7, #4D96FF); background-size: 300%; animation: gradShift 2s ease infinite, popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.3s both; color: #fff; font-size: 19px; }

.score-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 20px; }
.score-box-correct { background: linear-gradient(135deg, #DCFCE7, #BBF7D0); border: 2.5px solid #86efac; border-radius: 20px; padding: 22px; text-align: center; box-shadow: 0 4px 16px rgba(34,197,94,0.2); animation: fadeSlideUp 0.5s ease 0.2s both; }
.score-box-wrong   { background: linear-gradient(135deg, #FEE2E2, #fca5a5); border: 2.5px solid #fca5a5; border-radius: 20px; padding: 22px; text-align: center; box-shadow: 0 4px 16px rgba(239,68,68,0.15); animation: fadeSlideUp 0.5s ease 0.3s both; }
.score-num { font-size: 48px; font-weight: 800; }
.score-lbl { font-size: 14px; font-weight: 700; margin-top: 2px; }

.total-pts-box { background: linear-gradient(135deg, #1a1a2e, #16213e); border-radius: 22px; padding: 18px 24px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; gap: 18px; box-shadow: 0 8px 28px rgba(26,26,46,0.3); animation: fadeSlideUp 0.5s ease 0.1s both; }
.total-pts-icon { font-size: 34px; animation: sparkle 1s ease infinite alternate; }
.total-pts-val  { font-size: 30px; font-weight: 800; color: #FFD93D; }
.total-pts-lbl  { font-size: 13px; font-weight: 700; color: #9ca3af; text-transform: uppercase; }

/* Nút bấm toàn cục */
div.stButton > button { font-family: 'Baloo 2', cursive !important; font-weight: 800 !important; font-size: 18px !important; height: 58px !important; border-radius: 18px !important; transition: transform 0.18s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.18s !important; letter-spacing: .02em !important; position: relative; z-index: 1; }
div.stButton > button[kind="primary"]   { background: linear-gradient(135deg, #FF6B6B, #FF9A3C) !important; border: none !important; color: #fff !important; box-shadow: 0 6px 20px rgba(255,107,107,0.4) !important; }
div.stButton > button[kind="primary"]:hover   { transform: translateY(-3px) scale(1.04) !important; box-shadow: 0 12px 28px rgba(255,107,107,0.55) !important; }
div.stButton > button[kind="secondary"] { background: #fff !important; border: 2.5px solid #e9d5ff !important; color: #7c3aed !important; }
div.stButton > button[kind="secondary"]:hover { border-color: #a855f7 !important; background: #faf5ff !important; transform: translateY(-2px) !important; box-shadow: 0 6px 14px rgba(168,85,247,0.18) !important; }

/* Badge chip lịch sử */
.badge-history-box   { background: #fff; border: 2.5px solid #e9d5ff; border-radius: 20px; padding: 14px 18px; margin-bottom: 16px; box-shadow: 0 4px 14px rgba(124,58,237,0.1); animation: fadeSlideUp 0.6s ease 0.4s both; }
.badge-history-title { font-size: 13px; font-weight: 800; color: #7c3aed; text-transform: uppercase; letter-spacing: .06em; margin: 0 0 8px; }
.badge-history-row   { display: flex; flex-wrap: wrap; gap: 8px; }
.badge-chip { font-size: 13px; font-weight: 800; padding: 4px 12px; border-radius: 99px; color: #fff; display: inline-block; }

/* Nhãn lớp học trong onboard */
.class-badge { display: inline-block; background: linear-gradient(135deg, #4D96FF, #1d4ed8); color: #fff; font-size: 16px; font-weight: 800; padding: 8px 20px; border-radius: 99px; margin-top: 4px; }

/* Thông báo lưu Google Sheets */
.gs-success { background: #DCFCE7; border: 2px solid #22c55e; border-radius: 14px; padding: 10px 16px; font-size: 14px; font-weight: 700; color: #14532d; margin-top: 12px; }
.gs-error   { background: #FEE2E2; border: 2px dashed #ef4444; border-radius: 14px; padding: 10px 16px; font-size: 14px; font-weight: 700; color: #7f1d1d; margin-top: 12px; }

@keyframes bounce    { 0%,100%{transform:translateY(0)}      50%{transform:translateY(-10px)} }
@keyframes wobble    { 0%,100%{transform:rotate(0deg)} 15%{transform:rotate(-8deg)} 30%{transform:rotate(6deg)} 45%{transform:rotate(-4deg)} 60%{transform:rotate(2deg)} }
@keyframes popIn     { 0%{transform:scale(0.7);opacity:0}    100%{transform:scale(1);opacity:1} }
@keyframes shake     { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-10px)} 40%{transform:translateX(10px)} 60%{transform:translateX(-6px)} 80%{transform:translateX(6px)} }
@keyframes fadeSlideUp { 0%{opacity:0;transform:translateY(24px)} 100%{opacity:1;transform:translateY(0)} }
@keyframes gradShift { 0%,100%{background-position:0% 50%}   50%{background-position:100% 50%} }
@keyframes shimmer   { 0%{background-position:0% 50%}         100%{background-position:100% 50%} }
@keyframes sparkle   { 0%{transform:scale(1) rotate(0deg)}    100%{transform:scale(1.3) rotate(20deg)} }
audio { display: none; }

@media (max-width: 768px) {
    .left-panel { min-height: auto; position: static; margin-bottom: 20px; }
    .q-text { font-size: 22px; }
    .result-title { font-size: 30px; }
}
</style>
""", unsafe_allow_html=True)

# ── Hạt confetti nổi ──────────────────────────────────────────────────────────
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
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DỮ LIỆU CÂU HỎI – 3 MÔN: Toán, Tiếng Việt, Tiếng Anh
# ══════════════════════════════════════════════════════════════════════════════
SUBJECTS = {
    "math": {
        "label": "Toán học",
        "icon":  "🔢",
        "badge": "badge-math",
        "q_box_class": "q-box-math",
        "color": "#FF6B6B",
        "topics": [
            {"name": "Phép cộng có nhớ",   "qs": [], "auto_gen": "add"},
            {"name": "Phép trừ có nhớ",    "qs": [], "auto_gen": "sub"},
            {"name": "Toán có lời văn",     "qs": [], "auto_gen": "word"},
            {
                "name": "So sánh số",
                "qs": [
                    {"type":"mcq","q":"Số nào lớn hơn: 45 hay 54?",        "opts":["45","54","Bằng nhau","Không biết"],"ans":1,"explain":"📝 So sánh hàng chục: 45 có 4, 54 có 5 → 5>4 nên 54>45 ✔"},
                    {"type":"fill_blank","q":"Điền dấu (>, < hoặc =): 73 ___ 37","ans_text":">","explain":"📝 73 hàng chục=7, 37 hàng chục=3 → 7>3 nên 73 > 37 ✔"},
                    {"type":"mcq","q":"Số liền sau của 99 là?",              "opts":["98","100","101","97"],            "ans":1,"explain":"📝 Số liền sau = số đó + 1 → 99+1=100 ✔"},
                    {"type":"mcq","q":"Số liền trước của 50 là?",            "opts":["51","49","48","52"],             "ans":1,"explain":"📝 Số liền trước = số đó − 1 → 50−1=49 ✔"},
                    {"type":"fill_blank","q":"Điền dấu (>, < hoặc =): 68 ___ 86","ans_text":"<","explain":"📝 68 hàng chục=6, 86 hàng chục=8 → 6<8 nên 68 < 86 ✔"},
                    {"type":"mcq","q":"Số nào nhỏ nhất: 25, 52, 22, 55?",   "opts":["25","52","22","55"],             "ans":2,"explain":"📝 Hàng chục nhỏ nhất là 2 → so đơn vị: 22<25 → 22 nhỏ nhất ✔"},
                    {"type":"mcq","q":"Số nào lớn nhất: 31, 13, 33, 11?",   "opts":["31","13","33","11"],             "ans":2,"explain":"📝 Hàng chục lớn nhất là 3 → so đơn vị: 33>31 → 33 lớn nhất ✔"},
                    {"type":"fill_blank","q":"Điền dấu (>, < hoặc =): 40 ___ 40","ans_text":"=","explain":"📝 Hai số giống nhau → 40 = 40 ✔"},
                    {"type":"mcq","q":"Số liền sau của 79 là?",              "opts":["78","80","81","77"],             "ans":1,"explain":"📝 79+1=80 ✔"},
                    {"type":"mcq","q":"Số liền trước của 100 là?",           "opts":["99","101","98","102"],           "ans":0,"explain":"📝 100−1=99 ✔"},
                ],
            },
            {
                "name": "Đo lường",
                "qs": [
                    {"type":"mcq","q":"1 dm = ? cm",   "opts":["5 cm","10 cm","100 cm","1 cm"],   "ans":1,"explain":"📝 1 dm = 10 cm ✔"},
                    {"type":"mcq","q":"1 m = ? dm",    "opts":["100 dm","1 dm","10 dm","5 dm"],   "ans":2,"explain":"📝 1 m = 10 dm ✔"},
                    {"type":"fill_blank","q":"30 cm = ___ dm",                                     "ans_text":"3","explain":"📝 30÷10=3 dm ✔"},
                    {"type":"fill_blank","q":"20 dm = ___ m",                                      "ans_text":"2","explain":"📝 20÷10=2 m ✔"},
                    {"type":"mcq","q":"1 m = ? cm",    "opts":["10 cm","1000 cm","100 cm","1 cm"],"ans":2,"explain":"📝 1 m = 100 cm ✔"},
                    {"type":"fill_blank","q":"5 dm = ___ cm",                                      "ans_text":"50","explain":"📝 5×10=50 cm ✔"},
                    {"type":"mcq","q":"2 m = ? dm",    "opts":["2 dm","200 dm","20 dm","12 dm"],  "ans":2,"explain":"📝 2×10=20 dm ✔"},
                    {"type":"fill_blank","q":"40 cm = ___ dm",                                     "ans_text":"4","explain":"📝 40÷10=4 dm ✔"},
                    {"type":"mcq","q":"3 m = ? cm",    "opts":["3 cm","30 cm","300 cm","3000 cm"],"ans":2,"explain":"📝 3×100=300 cm ✔"},
                    {"type":"fill_blank","q":"6 dm = ___ cm",                                      "ans_text":"60","explain":"📝 6×10=60 cm ✔"},
                ],
            },
            {
                "name": "Hình học",
                "qs": [
                    {"type":"mcq","q":"Hình chữ nhật có bao nhiêu góc vuông?",    "opts":["2","3","4","1"],                                           "ans":2,"explain":"📝 Hình chữ nhật có 4 góc vuông (90°) ✔"},
                    {"type":"mcq","q":"Hình vuông có bao nhiêu cạnh bằng nhau?",  "opts":["2","3","0","4"],                                           "ans":3,"explain":"📝 Hình vuông: 4 cạnh đều bằng nhau ✔"},
                    {"type":"fill_blank","q":"Hình tam giác có ___ cạnh.",          "ans_text":"3","explain":"📝 Tam giác = ba + góc → 3 cạnh ✔"},
                    {"type":"mcq","q":"Hình nào có tất cả các cạnh bằng nhau?",   "opts":["Hình chữ nhật","Hình tam giác","Hình vuông","Hình thang"],"ans":2,"explain":"📝 Hình vuông: 4 cạnh bằng nhau ✔"},
                    {"type":"mcq","q":"Hình tròn có bao nhiêu góc?",              "opts":["1","2","3","0"],                                           "ans":3,"explain":"📝 Hình tròn không có góc ✔"},
                    {"type":"fill_blank","q":"Hình chữ nhật có ___ cạnh.",         "ans_text":"4","explain":"📝 Hình chữ nhật có 4 cạnh ✔"},
                    {"type":"mcq","q":"Hình nào KHÔNG có góc vuông?",             "opts":["Hình vuông","Hình chữ nhật","Hình tròn","Tất cả"],        "ans":2,"explain":"📝 Hình tròn không có góc ✔"},
                    {"type":"mcq","q":"Hình tam giác có bao nhiêu góc?",          "opts":["2","4","3","1"],                                           "ans":2,"explain":"📝 Tam giác có 3 góc ✔"},
                    {"type":"fill_blank","q":"Hình vuông có ___ cạnh bằng nhau.",  "ans_text":"4","explain":"📝 4 cạnh bằng nhau ✔"},
                    {"type":"mcq","q":"Cạnh dài của hình chữ nhật gọi là?",       "opts":["Chiều rộng","Chiều cao","Chiều dài","Cạnh bên"],           "ans":2,"explain":"📝 Cạnh dài = chiều dài ✔"},
                ],
            },
        ],
    },

    "viet": {
        "label": "Tiếng Việt",
        "icon":  "📖",
        "badge": "badge-viet",
        "q_box_class": "q-box-viet",
        "color": "#22c55e",
        "topics": [
            {
                "name": "Chính tả – âm vần",
                "qs": [
                    {"type":"mcq","q":"Chọn từ viết đúng chính tả:",           "opts":["giòng sông","dòng sông","giòng xông","dòng xông"],  "ans":1,"explain":"📝 'dòng sông' viết với 'd' ✔"},
                    {"type":"fill_blank","q":"Điền âm đầu: con ___ò (chọn c hoặc k)","ans_text":"c","explain":"📝 'c' đứng trước o, a, ô... → con cò ✔"},
                    {"type":"mcq","q":"Chọn từ đúng: trời mưa hay giời mưa?",  "opts":["giời mưa","trời mưa","trởi mưa","chời mưa"],       "ans":1,"explain":"📝 'Trời' viết với 'tr' ✔"},
                    {"type":"fill_blank","q":"Điền vào: bầu ___ời (tr/ch)",     "ans_text":"tr","explain":"📝 'bầu trời' → 'tr' ✔"},
                    {"type":"mcq","q":"Chọn từ đúng:",                          "opts":["con trâu","con châu","con trau","con chau"],        "ans":0,"explain":"📝 'con trâu' viết với 'tr' + dấu huyền ✔"},
                    {"type":"mcq","q":"Từ nào viết đúng?",                      "opts":["buổi sáng","buổi xáng","buỗi sáng","buổi sạng"],  "ans":0,"explain":"📝 'buổi sáng' – dấu hỏi trên ô, dấu sắc trên a ✔"},
                    {"type":"fill_blank","q":"Điền vào: hoa ___ồng (h/r)",      "ans_text":"h","explain":"📝 'hoa hồng' → 'h' ✔"},
                    {"type":"mcq","q":"Từ nào viết sai?",                       "opts":["quả cam","quả xoài","quả dưa","quả khôm"],         "ans":3,"explain":"📝 Viết đúng là 'quả khóm' ✔"},
                    {"type":"mcq","q":"Chọn từ đúng:",                          "opts":["lá cây","lá kây","la cây","lá cay"],               "ans":0,"explain":"📝 'lá cây' – 'cây' không dấu ✔"},
                    {"type":"mcq","q":"Từ nào viết đúng?",                      "opts":["xanh lá cây","sanh lá cây","xanh lá kay","xang lá cây"],"ans":0,"explain":"📝 'xanh' viết với 'x' ✔"},
                ],
            },
            {
                "name": "Từ loại – danh từ",
                "qs": [
                    {"type":"mcq","q":"Từ nào là danh từ?",              "opts":["chạy","đẹp","bàn","nhanh"],              "ans":2,"explain":"📝 'bàn' là đồ vật → danh từ ✔"},
                    {"type":"fill_blank","q":"'Thầy giáo' là danh từ chỉ ___. (người/đồ vật)","ans_text":"người","explain":"📝 Thầy giáo là người → danh từ chỉ người ✔"},
                    {"type":"mcq","q":"Từ nào KHÔNG phải danh từ?",       "opts":["sách","vở","đọc","bút"],                "ans":2,"explain":"📝 'đọc' là hành động → động từ ✔"},
                    {"type":"mcq","q":"Chọn danh từ chỉ con vật:",        "opts":["bay","to","con mèo","nhanh"],           "ans":2,"explain":"📝 'con mèo' là tên con vật → danh từ ✔"},
                    {"type":"fill_blank","q":"'Trường học' là danh từ chỉ ___ chốn. (nơi/người)","ans_text":"nơi","explain":"📝 Trường học là địa điểm → danh từ chỉ nơi chốn ✔"},
                    {"type":"mcq","q":"Từ nào là danh từ?",              "opts":["học","ghế","vui","xanh"],                "ans":1,"explain":"📝 'ghế' là đồ vật → danh từ ✔"},
                    {"type":"mcq","q":"Danh từ chỉ đồ vật:",             "opts":["cái bàn","chạy","đẹp","xanh"],          "ans":0,"explain":"📝 'cái bàn' là đồ vật → danh từ ✔"},
                    {"type":"mcq","q":"Chọn danh từ:",                   "opts":["nhìn","ngủ","ăn","cây bút"],            "ans":3,"explain":"📝 'cây bút' là đồ vật → danh từ ✔"},
                    {"type":"fill_blank","q":"'Ngôi nhà' là danh từ chỉ ___ chốn. (nơi/người)","ans_text":"nơi","explain":"📝 Ngôi nhà là nơi ở → danh từ chỉ nơi chốn ✔"},
                    {"type":"mcq","q":"Từ nào là danh từ?",              "opts":["nhảy","hát","trường học","vui vẻ"],      "ans":2,"explain":"📝 'trường học' là nơi chốn → danh từ ✔"},
                ],
            },
            {
                "name": "Câu hỏi – câu kể",
                "qs": [
                    {"type":"mcq","q":"Câu hỏi thường dùng từ nào?",                "opts":["vì","và","Ai? Cái gì?","nhưng"],                "ans":2,"explain":"📝 Câu hỏi dùng: Ai? Cái gì? Ở đâu? Khi nào? ✔"},
                    {"type":"fill_blank","q":"Câu hỏi kết thúc bằng dấu ___.","ans_text":"?","explain":"📝 Câu hỏi → dấu chấm hỏi (?) ✔"},
                    {"type":"mcq","q":"'Tại sao bạn khóc?' hỏi về điều gì?",        "opts":["Người","Nơi chốn","Thời gian","Lý do"],         "ans":3,"explain":"📝 'Tại sao?' hỏi về lý do ✔"},
                    {"type":"mcq","q":"Từ hỏi 'Ở đâu?' hỏi về điều gì?",           "opts":["Người","Nơi chốn","Thời gian","Số lượng"],      "ans":1,"explain":"📝 'Ở đâu?' → hỏi về nơi chốn ✔"},
                    {"type":"fill_blank","q":"'Khi nào?' là từ hỏi về ___. (thời gian/nơi chốn)","ans_text":"thời gian","explain":"📝 'Khi nào?' hỏi về thời gian ✔"},
                    {"type":"mcq","q":"Chọn câu hỏi:",                              "opts":["Trời mưa to.","Trời có mưa không?","Trời mưa rất to!","Trời mưa, lạnh quá."],"ans":1,"explain":"📝 'Trời có mưa không?' là câu hỏi ✔"},
                    {"type":"mcq","q":"'Ai đang học bài?' — Từ hỏi là?",            "opts":["đang","học","Ai","bài"],                        "ans":2,"explain":"📝 'Ai?' hỏi về người ✔"},
                    {"type":"mcq","q":"Câu 'Con đang làm gì?' hỏi về điều gì?",    "opts":["Người","Thời gian","Hành động","Nơi chốn"],     "ans":2,"explain":"📝 'Làm gì?' → hỏi về hành động ✔"},
                    {"type":"fill_blank","q":"Câu kể kết thúc bằng dấu ___.",       "ans_text":".","explain":"📝 Câu kể → dấu chấm (.) ✔"},
                    {"type":"mcq","q":"'Hãy giữ gìn sách vở.' là câu gì?",         "opts":["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"],  "ans":3,"explain":"📝 Có từ 'Hãy' → câu cầu khiến ✔"},
                ],
            },
            {
                "name": "Từ đồng nghĩa – trái nghĩa",
                "qs": [
                    {"type":"mcq","q":"Từ trái nghĩa với 'to' là?",       "opts":["lớn","bé","cao","nặng"],       "ans":1,"explain":"📝 to ↔ bé ✔"},
                    {"type":"fill_blank","q":"Từ trái nghĩa với 'ngày' là ___","ans_text":"đêm","explain":"📝 ngày ↔ đêm ✔"},
                    {"type":"mcq","q":"Từ đồng nghĩa với 'vui' là?",      "opts":["buồn","hạnh phúc","khóc","đau"],"ans":1,"explain":"📝 vui ≈ hạnh phúc ✔"},
                    {"type":"fill_blank","q":"Từ trái nghĩa với 'nhanh' là ___","ans_text":"chậm","explain":"📝 nhanh ↔ chậm ✔"},
                    {"type":"mcq","q":"Từ trái nghĩa với 'sáng' là?",     "opts":["tối","đẹp","màu","rộng"],      "ans":0,"explain":"📝 sáng ↔ tối ✔"},
                    {"type":"mcq","q":"Từ đồng nghĩa với 'nhà' là?",      "opts":["trường","gia đình","ngôi nhà","phòng"],"ans":2,"explain":"📝 nhà ≈ ngôi nhà ✔"},
                    {"type":"fill_blank","q":"Từ trái nghĩa với 'cao' là ___","ans_text":"thấp","explain":"📝 cao ↔ thấp ✔"},
                    {"type":"mcq","q":"Từ trái nghĩa với 'nóng' là?",     "opts":["ấm","lạnh","mát","vừa"],       "ans":1,"explain":"📝 nóng ↔ lạnh ✔"},
                    {"type":"fill_blank","q":"Từ đồng nghĩa với 'xinh' là ___","ans_text":"đẹp","explain":"📝 xinh ≈ đẹp ✔"},
                    {"type":"mcq","q":"Từ trái nghĩa với 'mở' là?",       "opts":["bật","đóng","vào","ra"],       "ans":1,"explain":"📝 mở ↔ đóng ✔"},
                ],
            },
            {
                "name": "Tập làm văn ngắn",
                "qs": [
                    {"type":"mcq","q":"'Mùa hè, trời ____.' — Điền từ phù hợp:",     "opts":["lạnh giá","mưa phùn","nắng nóng","có tuyết"],  "ans":2,"explain":"📝 Mùa hè ở Việt Nam → nắng nóng ✔"},
                    {"type":"fill_blank","q":"Hoàn thành câu: 'Buổi sáng, em thức dậy và đánh ___.'","ans_text":"răng","explain":"📝 Buổi sáng đánh răng → vệ sinh cá nhân ✔"},
                    {"type":"mcq","q":"Đoạn văn tả cảnh vườn thường có từ nào?",      "opts":["xe cộ","hoa lá","sóng biển","núi cao"],        "ans":1,"explain":"📝 Vườn → hoa lá, cây cối ✔"},
                    {"type":"fill_blank","q":"Hoàn thành câu: 'Bầu trời mùa thu ___ và trong xanh.'","ans_text":"cao","explain":"📝 Bầu trời mùa thu cao và trong xanh ✔"},
                    {"type":"mcq","q":"Câu 'Ơi, đẹp quá!' là câu gì?",               "opts":["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans":2,"explain":"📝 Có từ 'Ơi', 'quá' và dấu ! → câu cảm ✔"},
                    {"type":"mcq","q":"Từ nào chỉ màu sắc?",                          "opts":["chạy","đỏ","bàn","vui"],                       "ans":1,"explain":"📝 'đỏ' là màu sắc ✔"},
                    {"type":"fill_blank","q":"Hoàn thành câu: 'Con mèo có bốn cái ___.'","ans_text":"chân","explain":"📝 Con mèo có 4 chân ✔"},
                    {"type":"mcq","q":"Câu 'Bầu trời xanh trong.' tả điều gì?",       "opts":["Con vật","Cảnh vật","Người","Đồ vật"],         "ans":1,"explain":"📝 Bầu trời là cảnh thiên nhiên ✔"},
                    {"type":"fill_blank","q":"Hoàn thành câu: 'Em rất yêu cha và ___.'","ans_text":"mẹ","explain":"📝 Cha và mẹ ✔"},
                    {"type":"mcq","q":"'Em thích ăn quả gì?' — Đây là câu gì?",       "opts":["Câu kể","Câu cảm","Câu hỏi","Câu cầu khiến"],"ans":2,"explain":"📝 Có từ hỏi 'gì?' + dấu ? → câu hỏi ✔"},
                ],
            },
        ],
    },

    "eng": {
        "label": "Tiếng Anh",
        "icon":  "🔤",
        "badge": "badge-eng",
        "q_box_class": "q-box-eng",
        "color": "#4D96FF",
        "topics": [
            {
                "name": "Từ vựng – Gia đình",
                "qs": [
                    {"type":"mcq","q":"'Mẹ' trong tiếng Anh là gì?",       "opts":["Father","Mother","Sister","Brother"],"ans":1,"explain":"📝 Mother = Mẹ ✔"},
                    {"type":"fill_blank","q":"Father = ___ (tiếng Việt)",    "ans_text":"cha","explain":"📝 Father = Cha / Bố ✔"},
                    {"type":"mcq","q":"'Anh trai' trong tiếng Anh là?",     "opts":["Sister","Mother","Brother","Father"],"ans":2,"explain":"📝 Brother = Anh trai / Em trai ✔"},
                    {"type":"fill_blank","q":"Sister = ___ (tiếng Việt)",    "ans_text":"chị","explain":"📝 Sister = Chị gái / Em gái ✔"},
                    {"type":"mcq","q":"'Ông nội/ngoại' trong tiếng Anh?",   "opts":["Uncle","Grandfather","Grandmother","Cousin"],"ans":1,"explain":"📝 Grandfather = Ông ✔"},
                    {"type":"fill_blank","q":"Grandmother = ___ (tiếng Việt)","ans_text":"bà","explain":"📝 Grandmother = Bà ✔"},
                    {"type":"mcq","q":"'Baby' có nghĩa là gì?",             "opts":["Trẻ em","Em bé","Con trai","Con gái"],"ans":1,"explain":"📝 Baby = Em bé ✔"},
                    {"type":"fill_blank","q":"Family = ___ (tiếng Việt)",    "ans_text":"gia đình","explain":"📝 Family = Gia đình ✔"},
                    {"type":"mcq","q":"'Con trai' trong tiếng Anh là?",     "opts":["Girl","Boy","Baby","Child"],         "ans":1,"explain":"📝 Boy = Con trai ✔"},
                    {"type":"fill_blank","q":"Girl = ___ (tiếng Việt)",      "ans_text":"con gái","explain":"📝 Girl = Con gái ✔"},
                ],
            },
            {
                "name": "Từ vựng – Màu sắc & Số",
                "qs": [
                    {"type":"mcq","q":"'Màu đỏ' trong tiếng Anh là?",      "opts":["Blue","Green","Red","Yellow"],       "ans":2,"explain":"📝 Red = Đỏ ✔"},
                    {"type":"fill_blank","q":"Blue = màu ___ (tiếng Việt)", "ans_text":"xanh","explain":"📝 Blue = Màu xanh ✔"},
                    {"type":"mcq","q":"'Yellow' có nghĩa là màu gì?",       "opts":["Tím","Vàng","Cam","Hồng"],          "ans":1,"explain":"📝 Yellow = Màu vàng ✔"},
                    {"type":"fill_blank","q":"Green = màu ___ (tiếng Việt)","ans_text":"xanh lá","explain":"📝 Green = Màu xanh lá cây ✔"},
                    {"type":"mcq","q":"'Three' là số mấy?",                 "opts":["2","3","4","5"],                     "ans":1,"explain":"📝 Three = 3 ✔"},
                    {"type":"fill_blank","q":"Five = số ___ (tiếng Việt)",  "ans_text":"5","explain":"📝 Five = 5 ✔"},
                    {"type":"mcq","q":"Số 10 trong tiếng Anh là?",          "opts":["Eight","Nine","Ten","Seven"],        "ans":2,"explain":"📝 Ten = 10 ✔"},
                    {"type":"fill_blank","q":"Seven = số ___",              "ans_text":"7","explain":"📝 Seven = 7 ✔"},
                    {"type":"mcq","q":"'Pink' là màu gì?",                  "opts":["Tím","Hồng","Cam","Đen"],            "ans":1,"explain":"📝 Pink = Màu hồng ✔"},
                    {"type":"fill_blank","q":"Black = màu ___ (tiếng Việt)","ans_text":"đen","explain":"📝 Black = Màu đen ✔"},
                ],
            },
            {
                "name": "Từ vựng – Đồ vật & Con vật",
                "qs": [
                    {"type":"mcq","q":"'Con mèo' trong tiếng Anh là?",      "opts":["Dog","Cat","Bird","Fish"],           "ans":1,"explain":"📝 Cat = Con mèo ✔"},
                    {"type":"fill_blank","q":"Dog = con ___ (tiếng Việt)",   "ans_text":"chó","explain":"📝 Dog = Con chó ✔"},
                    {"type":"mcq","q":"'Bird' có nghĩa là gì?",              "opts":["Con cá","Con gà","Con chim","Con heo"],"ans":2,"explain":"📝 Bird = Con chim ✔"},
                    {"type":"fill_blank","q":"Fish = con ___ (tiếng Việt)",  "ans_text":"cá","explain":"📝 Fish = Con cá ✔"},
                    {"type":"mcq","q":"'Cái bàn' trong tiếng Anh là?",       "opts":["Chair","Table","Book","Pen"],        "ans":1,"explain":"📝 Table = Cái bàn ✔"},
                    {"type":"fill_blank","q":"Chair = cái ___ (tiếng Việt)", "ans_text":"ghế","explain":"📝 Chair = Cái ghế ✔"},
                    {"type":"mcq","q":"'Book' có nghĩa là gì?",              "opts":["Bút","Bàn","Sách","Ghế"],           "ans":2,"explain":"📝 Book = Quyển sách ✔"},
                    {"type":"fill_blank","q":"Pen = cái ___ (tiếng Việt)",   "ans_text":"bút","explain":"📝 Pen = Cái bút ✔"},
                    {"type":"mcq","q":"'Con gà' trong tiếng Anh là?",        "opts":["Duck","Pig","Chicken","Cow"],        "ans":2,"explain":"📝 Chicken = Con gà ✔"},
                    {"type":"fill_blank","q":"Cow = con ___ (tiếng Việt)",   "ans_text":"bò","explain":"📝 Cow = Con bò ✔"},
                ],
            },
            {
                "name": "Chào hỏi & Câu đơn giản",
                "qs": [
                    {"type":"mcq","q":"'Xin chào' trong tiếng Anh là?",          "opts":["Goodbye","Hello","Thank you","Sorry"],"ans":1,"explain":"📝 Hello = Xin chào ✔"},
                    {"type":"fill_blank","q":"Goodbye = ___ (tiếng Việt)",         "ans_text":"tạm biệt","explain":"📝 Goodbye = Tạm biệt ✔"},
                    {"type":"mcq","q":"'Cảm ơn' trong tiếng Anh là?",            "opts":["Sorry","Please","Thank you","Yes"],  "ans":2,"explain":"📝 Thank you = Cảm ơn ✔"},
                    {"type":"fill_blank","q":"Yes = ___ (tiếng Việt)",             "ans_text":"có","explain":"📝 Yes = Có / Vâng ✔"},
                    {"type":"mcq","q":"'No' có nghĩa là gì?",                     "opts":["Có","Không","Được","Xin lỗi"],      "ans":1,"explain":"📝 No = Không ✔"},
                    {"type":"fill_blank","q":"Please = ___ (tiếng Việt)",          "ans_text":"làm ơn","explain":"📝 Please = Làm ơn / Xin ✔"},
                    {"type":"mcq","q":"'My name is Nam.' nghĩa là gì?",           "opts":["Bạn tên là Nam","Tên tôi là Nam","Anh ấy tên Nam","Em tên Nam"],"ans":1,"explain":"📝 My name is = Tên tôi là ✔"},
                    {"type":"fill_blank","q":"Sorry = ___ (tiếng Việt)",           "ans_text":"xin lỗi","explain":"📝 Sorry = Xin lỗi ✔"},
                    {"type":"mcq","q":"'Good morning' nghĩa là gì?",              "opts":["Chúc ngủ ngon","Tạm biệt","Chào buổi sáng","Cảm ơn"],"ans":2,"explain":"📝 Good morning = Chào buổi sáng ✔"},
                    {"type":"fill_blank","q":"Good night = ___ (tiếng Việt)",      "ans_text":"chúc ngủ ngon","explain":"📝 Good night = Chúc ngủ ngon ✔"},
                ],
            },
        ],
    },
}

# Thêm CSS badge cho Tiếng Anh
st.markdown("""
<style>
.badge-eng { background: linear-gradient(135deg, #4D96FF, #1d4ed8); color: #fff; }
</style>
""", unsafe_allow_html=True)

PRAISE = [
    "🎉 Tuyệt vời! Thông minh quá!",
    "⭐ Chính xác! Giỏi lắm!",
    "🌟 Đúng rồi! Cố lên nhé!",
    "🏆 Xuất sắc! Học rất giỏi!",
    "🎊 Đúng rồi! Tài năng thật!",
    "🥳 Chính xác! Thông minh quá!",
    "💫 Hoàn hảo! Làm tiếp nào!",
    "🚀 Siêu đỉnh! Bạn quá giỏi!",
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
# Sử dụng gspread + service account được cấu hình trong Streamlit Secrets
# ══════════════════════════════════════════════════════════════════════════════
def save_to_google_sheet(data: dict):
    """
    Ghi một hàng kết quả vào Google Sheets.
    Cấu hình cần thiết trong .streamlit/secrets.toml:
      [gcp_service_account]   ← JSON key từ Google Cloud Service Account
      google_sheet_id = "..."  ← ID file Sheets (từ URL)
    """
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        # Lấy thông tin xác thực từ Streamlit Secrets
        creds_dict = st.secrets.get("gcp_service_account", None)
        if creds_dict is None:
            st.markdown('<div class="gs-error">⚠️ Chưa cấu hình [gcp_service_account] trong Secrets. Kết quả chưa được lưu.</div>', unsafe_allow_html=True)
            return

        creds  = Credentials.from_service_account_info(dict(creds_dict), scopes=scopes)
        client = gspread.authorize(creds)

        # Lấy ID file Google Sheets từ Secrets
        sheet_id = st.secrets.get("google_sheet_id", "").strip()
        if not sheet_id:
            # Fallback: thử lấy ID từ URL mặc định
            sheet_id = "1vo-EhmSYZ6hkQT1TQoPmJ2IcRXzUfzEgaFZTkkBrat4"

        sh = client.open_by_key(sheet_id)
        ws = sh.sheet1

        # Kiểm tra nếu Sheet chưa có tiêu đề, thêm vào dòng đầu
        try:
            first_row = ws.row_values(1)
        except Exception:
            first_row = []

        if not first_row or first_row[0] != "Tên học sinh":
            ws.insert_row(
                ["Tên học sinh", "Lớp", "Môn học", "Chủ đề",
                 "Câu đúng", "Tổng câu", "Điểm tích lũy",
                 "Huy hiệu", "Thời gian hoàn thành"],
                index=1,
            )

        # Ghi dữ liệu
        row = [
            data.get("name",      ""),
            data.get("class_name","Lớp 2"),
            data.get("subject",   ""),
            data.get("topic",     ""),
            data.get("score",     0),
            data.get("total",     0),
            data.get("points",    0),
            data.get("badge",     ""),
            str(data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))),
        ]
        ws.append_row(row, value_input_option="USER_ENTERED")
        st.markdown('<div class="gs-success">✅ Đã lưu kết quả vào Google Sheets thành công!</div>', unsafe_allow_html=True)

    except Exception as e:
        # Hiển thị lỗi chi tiết để giáo viên/phụ huynh dễ debug
        st.markdown(f'<div class="gs-error">⚠️ Chưa kết nối được Google Sheets. Kết quả vẫn hiển thị bình thường.<br><small>Chi tiết: {e}</small></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# KHỞI TẠO SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
def init_state():
    defaults = {
        "screen":        "onboard",   # onboard → home → topics → quiz → result
        "username":      "",
        "class_name":    "Lớp 2",
        "subject":       None,
        "topic_idx":     None,
        "q_idx":         0,
        "score":         0,
        "answered":      False,
        "selected":      None,         # index đáp án đã chọn (MCQ)
        "fill_input":    "",           # nội dung ô điền (fill_blank)
        "fill_submitted": False,       # đã bấm "Kiểm tra" chưa
        "shuffled_qs":   [],
        "recent":        None,
        "total_pts":     0,
        "streak":        0,
        "best_streak":   0,
        "badge_history": [],
        "leaderboard":   [],
        "bonus_this":    0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ══════════════════════════════════════════════════════════════════════════════
# HÀM TIỆN ÍCH
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
        return {"key": "try",       "label": "💪 Cố Gắng!",   "css": "badge-try"}


def go_home():
    st.session_state.screen = "home"


def go_topics(subj: str):
    st.session_state.subject = subj
    st.session_state.screen  = "topics"


def go_quiz(topic_idx: int):
    """
    Bắt đầu / Luyện lại bài quiz.
    Mỗi lần gọi sẽ sinh lại hoặc xáo trộn ngẫu nhiên câu hỏi
    → đảm bảo "Luyện lại" không lặp thứ tự cũ.
    """
    subj = st.session_state.subject

    if subj == "math" and topic_idx == 0:
        shuffled = generate_math_addition(10)
    elif subj == "math" and topic_idx == 1:
        shuffled = generate_math_subtraction(10)
    elif subj == "math" and topic_idx == 2:
        shuffled = generate_math_word_problems(10)
    else:
        topic_data  = SUBJECTS[subj]["topics"][topic_idx]["qs"]
        sample_size = min(10, len(topic_data))
        shuffled    = random.sample(topic_data, sample_size)   # random.sample đảm bảo thứ tự khác nhau mỗi lần

    # Reset toàn bộ trạng thái quiz
    st.session_state.update({
        "topic_idx":    topic_idx,
        "shuffled_qs":  shuffled,
        "q_idx":        0,
        "score":        0,
        "answered":     False,
        "selected":     None,
        "fill_input":   "",
        "fill_submitted": False,
        "streak":       0,
        "bonus_this":   0,
        "screen":       "quiz",
    })


def answer_mcq(i: int):
    """Xử lý khi học sinh chọn đáp án trắc nghiệm."""
    if st.session_state.answered:
        return
    st.session_state.selected  = i
    st.session_state.answered  = True
    st.session_state.bonus_this = 0
    q = st.session_state.shuffled_qs[st.session_state.q_idx]
    _evaluate_answer(i == q["ans"])


def answer_fill(user_text: str, correct_text: str):
    """Xử lý khi học sinh điền câu trả lời tự luận."""
    if st.session_state.answered:
        return
    st.session_state.fill_submitted = True
    st.session_state.answered = True
    st.session_state.bonus_this = 0
    # So sánh không phân biệt hoa thường, bỏ khoảng trắng thừa
    is_correct = user_text.strip().lower() == correct_text.strip().lower()
    _evaluate_answer(is_correct)


def _evaluate_answer(is_correct: bool):
    """Cộng điểm, streak nếu đúng."""
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
    """Khi kết thúc bài: tính kết quả, cập nhật leaderboard, lưu Sheets."""
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

    # Lưu Google Sheets
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
# UI HELPER – RENDER HUD, ÂM THANH, CONFETTI
# ══════════════════════════════════════════════════════════════════════════════
def render_sound(correct: bool):
    if correct:
        js = """<script>(function(){var c=new(window.AudioContext||window.webkitAudioContext)();function tone(f,t,d){var o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);o.type='sine';o.frequency.value=f;g.gain.setValueAtTime(0.3,t);g.gain.exponentialRampToValueAtTime(0.001,t+d);o.start(t);o.stop(t+d);}tone(880,c.currentTime,0.15);tone(1100,c.currentTime+0.15,0.15);tone(1320,c.currentTime+0.3,0.3);})();</script>"""
    else:
        js = """<script>(function(){var c=new(window.AudioContext||window.webkitAudioContext)();var o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);o.type='sawtooth';o.frequency.setValueAtTime(300,c.currentTime);o.frequency.exponentialRampToValueAtTime(100,c.currentTime+0.4);g.gain.setValueAtTime(0.2,c.currentTime);g.gain.exponentialRampToValueAtTime(0.001,c.currentTime+0.4);o.start(c.currentTime);o.stop(c.currentTime+0.4);})();</script>"""
    st.markdown(js, unsafe_allow_html=True)


def render_celebration_sound():
    js = """<script>(function(){var c=new(window.AudioContext||window.webkitAudioContext)();var notes=[523,659,784,1047,1319];notes.forEach(function(f,i){var o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);o.type='sine';o.frequency.value=f;var t=c.currentTime+i*0.15;g.gain.setValueAtTime(0.25,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.3);o.start(t);o.stop(t+0.3);});})();</script>"""
    st.markdown(js, unsafe_allow_html=True)


def render_confetti():
    colors = ["#FF6B6B","#FF9A3C","#FFD93D","#6BCB77","#4D96FF","#a855f7","#FF69B4"]
    pieces = ""
    for i in range(40):
        c   = random.choice(colors)
        lft = random.randint(0, 100)
        dur = random.uniform(1.5, 3.5)
        dly = random.uniform(0, 1.5)
        sz  = random.randint(8, 14)
        rot = random.randint(0, 360)
        pieces += (f'<div class="confetti-piece" style="left:{lft}%;top:-20px;background:{c};'
                   f'width:{sz}px;height:{sz}px;animation-duration:{dur:.1f}s;'
                   f'animation-delay:{dly:.1f}s;transform:rotate({rot}deg);"></div>')
    st.markdown(f'<div style="pointer-events:none;position:relative;z-index:9999;">{pieces}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LAYOUT CHÍNH – CHIA 2 CỘT
# Panel trái: thông tin học sinh + chọn môn/chủ đề
# Panel phải: nội dung màn hình hiện tại
# ══════════════════════════════════════════════════════════════════════════════

# Chỉ hiển thị panel 2 cột sau khi đã đăng nhập (screen != "onboard")
if st.session_state.screen == "onboard":
    # ── MÀN 0 – ONBOARDING (full width) ────────────────────────────────────
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

        name_input  = st.text_input("🎮 Tên hoặc biệt danh của bạn:", placeholder="Ví dụ: Siêu Sao, Nam Ngầu, Bé Kute...", max_chars=20)

        # Chọn lớp học (mở rộng sau này)
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
    # ── BỐ CỤC 2 CỘT cho các màn hình sau onboard ──────────────────────────
    left_col, right_col = st.columns([1, 2.8], gap="medium")

    # ════════════════════════════════
    # PANEL TRÁI – thông tin + chọn môn
    # ════════════════════════════════
    with left_col:
        name       = st.session_state.username or "Bạn"
        pts        = st.session_state.total_pts
        lv         = get_level(pts)
        streak     = st.session_state.streak
        class_name = st.session_state.class_name

        st.markdown(f"""
        <div class="left-panel">
            <div class="student-card">
                <span class="student-avatar">🦊</span>
                <div class="student-name">👋 {name}</div>
                <div class="student-class">{class_name}</div>
                <div class="stat-row">
                    <div class="stat-item"><div class="stat-val">⭐ {pts}</div><div class="stat-lbl">Điểm</div></div>
                    <div class="stat-item"><div class="stat-val">Lv.{lv}</div><div class="stat-lbl">Level</div></div>
                    <div class="stat-item"><div class="stat-val">{'🔥'+str(streak) if streak >= 3 else '—'}</div><div class="stat-lbl">Streak</div></div>
                </div>
            </div>
            <div class="panel-section-title">📚 Chọn Môn Học</div>
        </div>
        """, unsafe_allow_html=True)

        # Nút chọn môn học bên trong panel trái – sử dụng st.button
        # Hiển thị màu active cho môn đang chọn
        current_subj = st.session_state.get("subject")

        for subj_key, subj_data in SUBJECTS.items():
            topic_count = len(subj_data["topics"])
            btn_label   = f"{subj_data['icon']}  {subj_data['label']}  · {topic_count} chủ đề"
            if st.button(btn_label, key=f"nav_{subj_key}", use_container_width=True,
                         type="primary" if current_subj == subj_key else "secondary"):
                go_topics(subj_key)
                st.rerun()

        # Nút về trang chủ
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🏠 Trang Chủ", key="nav_home", use_container_width=True, type="secondary"):
            go_home()
            st.rerun()

    # ════════════════════════════════
    # PANEL PHẢI – nội dung màn hình
    # ════════════════════════════════
    with right_col:

        # ── MÀN 1 – TRANG CHỦ ─────────────────────────────────────────────
        if st.session_state.screen == "home":
            name = st.session_state.username
            st.markdown(f'<div class="greeting-box"><p class="greeting-text">Xin chào, {name}! 👋 Hôm nay học gì nào? 🎯</p></div>', unsafe_allow_html=True)
            st.markdown('<div style="text-align:center;font-family:Nunito,sans-serif;font-size:36px;font-weight:900;color:#1a1a2e;margin-bottom:6px;">🌟 Ôn Luyện Lớp 2</div>', unsafe_allow_html=True)
            st.markdown('<div style="text-align:center;font-size:17px;color:#7c3aed;font-weight:700;margin-bottom:20px;">Chọn môn ở bên trái để bắt đầu luyện tập! 🎮</div>', unsafe_allow_html=True)

            # 3 thẻ môn học
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div style="background:linear-gradient(135deg,#FFF3CD,#FFE082,#FFD93D);border:3px solid #FFD93D;border-radius:24px;padding:24px 12px;text-align:center;box-shadow:0 8px 24px rgba(255,217,61,0.35)"><span style="font-size:52px;">🔢</span><div style="font-size:20px;font-weight:800;color:#1a1a2e;margin-top:8px;">Toán học</div><div style="font-size:13px;color:#4b5563;font-weight:600;">6 chủ đề</div></div>', unsafe_allow_html=True)
                if st.button("➕ Học Toán", key="home_math", type="primary", use_container_width=True):
                    go_topics("math"); st.rerun()
            with c2:
                st.markdown('<div style="background:linear-gradient(135deg,#DCFCE7,#BBF7D0,#4ade80);border:3px solid #22c55e;border-radius:24px;padding:24px 12px;text-align:center;box-shadow:0 8px 24px rgba(34,197,94,0.35)"><span style="font-size:52px;">📖</span><div style="font-size:20px;font-weight:800;color:#1a1a2e;margin-top:8px;">Tiếng Việt</div><div style="font-size:13px;color:#4b5563;font-weight:600;">5 chủ đề</div></div>', unsafe_allow_html=True)
                if st.button("✏️ Học Tiếng Việt", key="home_viet", type="primary", use_container_width=True):
                    go_topics("viet"); st.rerun()
            with c3:
                st.markdown('<div style="background:linear-gradient(135deg,#DBEAFE,#93C5FD,#60A5FA);border:3px solid #4D96FF;border-radius:24px;padding:24px 12px;text-align:center;box-shadow:0 8px 24px rgba(77,150,255,0.35)"><span style="font-size:52px;">🔤</span><div style="font-size:20px;font-weight:800;color:#1a1a2e;margin-top:8px;">Tiếng Anh</div><div style="font-size:13px;color:#4b5563;font-weight:600;">4 chủ đề</div></div>', unsafe_allow_html=True)
                if st.button("🌍 Học Tiếng Anh", key="home_eng", type="primary", use_container_width=True):
                    go_topics("eng"); st.rerun()

            # Kết quả gần đây
            if st.session_state.recent:
                r = st.session_state.recent
                score_color = "#16a34a" if r["score"] >= 7 else "#f59e0b" if r["score"] >= 5 else "#ef4444"
                st.markdown(f"""
                <div style="background:#fff;border:2.5px solid #e9d5ff;border-radius:20px;padding:14px 18px;margin-top:20px;box-shadow:0 4px 16px rgba(124,58,237,0.12);">
                    <div style="font-size:12px;font-weight:800;color:#7c3aed;text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px;">🕐 Kết quả gần đây</div>
                    <div style="display:flex;align-items:center;gap:8px;font-size:15px;font-weight:700;color:#374151;">
                        <span>{r['name']}</span>
                        <span style="background:linear-gradient(135deg,#FF9A3C,#FF6B6B);color:#fff;font-size:11px;font-weight:800;padding:3px 10px;border-radius:99px;">{r['subj']}</span>
                        <span style="margin-left:auto;font-size:16px;font-weight:800;color:{score_color};">{r['score']}/{r['total']} ✅</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # ── MÀN 2 – CHỌN CHỦ ĐỀ ──────────────────────────────────────────
        elif st.session_state.screen == "topics":
            subj = st.session_state.subject
            sub  = SUBJECTS[subj]

            st.markdown(f'<div style="font-size:28px;font-weight:900;color:#1a1a2e;margin-bottom:6px;">{sub["icon"]} {sub["label"]}</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size:15px;color:#7c3aed;font-weight:700;margin-bottom:20px;">Chọn chủ đề để bắt đầu luyện tập! 🎯</div>', unsafe_allow_html=True)

            for i, topic in enumerate(sub["topics"]):
                t_col1, t_col2 = st.columns([4, 1])
                with t_col1:
                    st.markdown(f"""
                    <div style="background:#fff;border:2.5px solid #e9d5ff;border-radius:18px;padding:16px 20px;
                                font-size:18px;font-weight:700;color:#1a1a2e;margin-bottom:10px;
                                box-shadow:0 3px 12px rgba(0,0,0,0.05);">
                        📚 {topic['name']}
                    </div>""", unsafe_allow_html=True)
                with t_col2:
                    if st.button("▶ Bắt đầu", key=f"topic_{i}", type="primary", use_container_width=True):
                        go_quiz(i)
                        st.rerun()

        # ── MÀN 3 – CÂU HỎI ──────────────────────────────────────────────
        elif st.session_state.screen == "quiz":
            subj     = st.session_state.subject
            sub      = SUBJECTS[subj]
            qs       = st.session_state.shuffled_qs
            q_idx    = st.session_state.q_idx
            total    = len(qs)
            answered = st.session_state.answered
            name     = st.session_state.username
            q        = qs[q_idx]
            q_type   = q.get("type", "mcq")

            # Đếm câu + thanh tiến trình
            cnt_col, back_col = st.columns([3, 1])
            with cnt_col:
                st.markdown(f'<div class="q-counter">Câu {q_idx + 1} / {total} {'📝' if q_type=="fill_blank" else "🔘"}</div>', unsafe_allow_html=True)
            with back_col:
                if st.button("← Chủ đề", key="back_topics_quiz", type="secondary"):
                    go_topics(subj); st.rerun()

            pct = int((q_idx / total) * 100)
            st.markdown(f'<div class="progress-outer"><div class="progress-inner" style="width:{pct}%;"></div></div>', unsafe_allow_html=True)

            # Banner streak
            streak = st.session_state.streak
            if not answered and streak >= 3:
                st.markdown(f'<div class="streak-banner">{"🔥🔥🔥" if streak >= 5 else "🔥🔥"} Chuỗi đúng {streak} câu! Siêu đỉnh!</div>', unsafe_allow_html=True)

            # Hộp câu hỏi (font size lớn)
            st.markdown(f'<div class="{sub["q_box_class"]}"><p class="q-text">{q["q"]}</p></div>', unsafe_allow_html=True)

            # ── Render theo loại câu ────────────────────────────────────
            if q_type == "mcq":
                # Trắc nghiệm 4 đáp án
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
                # Tự luận – điền vào chỗ trống
                st.markdown('<div class="fill-label">✍️ Điền câu trả lời của em vào ô bên dưới:</div>', unsafe_allow_html=True)
                correct_text = q.get("ans_text", "")

                if not answered:
                    # Dùng form để bắt Enter
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
                else:
                    # Hiển thị kết quả điền
                    user_ans    = st.session_state.get(f"fill_{q_idx}", "")
                    is_correct  = user_ans.strip().lower() == correct_text.strip().lower()

            # ── Feedback sau khi trả lời ────────────────────────────────
            if answered:
                # Xác định đúng/sai
                if q_type == "mcq":
                    is_correct = (st.session_state.selected == q["ans"])
                else:
                    user_ans   = st.session_state.get(f"fill_{q_idx}", "")
                    is_correct = user_ans.strip().lower() == q.get("ans_text","").strip().lower()

                if is_correct:
                    praise = random.choice(PRAISE)
                    render_sound(True)
                    if st.session_state.bonus_this:
                        st.markdown(f'<div class="bonus-banner">🎁 STREAK BONUS +{st.session_state.bonus_this} điểm! Tuyệt vời!</div>', unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="feedback-correct">
                        <span class="feedback-correct-emoji">🌟</span>
                        <div class="feedback-correct-title">Giỏi quá {name}! +10 điểm ⭐</div>
                        <div class="feedback-correct-msg">{praise} Tiếp tục phát huy nhé! 🚀</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    render_sound(False)
                    correct_display = q["opts"][q["ans"]] if q_type == "mcq" else q.get("ans_text","")
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

        # ── MÀN 4 – KẾT QUẢ ──────────────────────────────────────────────
        elif st.session_state.screen == "result":
            score  = st.session_state.score
            total  = len(st.session_state.shuffled_qs)
            pts    = st.session_state.total_pts
            bstrk  = st.session_state.best_streak
            name   = st.session_state.username
            badge  = get_badge_for_result(score, total, bstrk)

            if badge["key"] == "superstar":
                mascot, title, msg = MASCOTS["superstar"], "🔥 Siêu Sao Hoàn Hảo!", f"Xuất sắc {name}! {total}/{total} câu đúng + chuỗi {bstrk}! Bạn là thiên tài! 🚀"
                render_celebration_sound(); render_confetti(); st.balloons()
            elif badge["key"] == "gold":
                mascot, title, msg = MASCOTS["perfect"], "🏆 Hoàn Hảo!", f"Tuyệt vời {name}! Đúng tất cả {total}/{total} câu!"
                render_celebration_sound(); render_confetti(); st.balloons()
            elif badge["key"] == "silver":
                mascot, title, msg = MASCOTS["great"], "⭐ Xuất Sắc!", f"Tuyệt vời {name}! Đúng {score}/{total} câu!"
                st.balloons()
            elif badge["key"] == "bronze":
                mascot, title, msg = MASCOTS["good"], "👍 Khá Tốt!", f"Cố lên {name}! Đúng {score}/{total} câu!"
            else:
                mascot, title, msg = MASCOTS["try"], "💪 Cố Lên Nào!", f"Không sao {name}! Luyện thêm rồi thử lại nhé! {score}/{total} câu đúng."

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
                    <div class="score-num" style="color:#16a34a;">{score}</div>
                    <div class="score-lbl" style="color:#166534;">Câu đúng ✅</div>
                </div>
                <div class="score-box-wrong">
                    <div class="score-num" style="color:#dc2626;">{total - score}</div>
                    <div class="score-lbl" style="color:#7f1d1d;">Câu sai ❌</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Huy hiệu lịch sử
            bh = st.session_state.badge_history
            if len(bh) > 1:
                chips = "".join(f'<span class="badge-chip {b["css"]}" title="{b["topic"]}">{b["label"]}</span>' for b in bh[-8:])
                st.markdown(f'<div class="badge-history-box"><div class="badge-history-title">🎖️ Huy Hiệu Đã Đạt</div><div class="badge-history-row">{chips}</div></div>', unsafe_allow_html=True)

            # Nút hành động
            r1, r2, r3 = st.columns(3)
            with r1:
                # Luyện lại → go_quiz sẽ sinh bộ câu hỏi MỚI/ngẫu nhiên khác
                if st.button("🔄 Luyện lại", key="retry", type="secondary", use_container_width=True):
                    go_quiz(st.session_state.topic_idx)
                    st.rerun()
            with r2:
                if st.button("📚 Chủ đề khác", key="other_topic", type="primary", use_container_width=True):
                    go_topics(st.session_state.subject)
                    st.rerun()
            with r3:
                if st.button("🏠 Trang Chủ", key="home_result", type="secondary", use_container_width=True):
                    go_home()
                    st.rerun()
