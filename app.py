import streamlit as st
import random
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json

# ══════════════════════════════════════════════════════════════════════════════
# CẤU HÌNH TRANG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="🌟 Siêu Sao Lớp 2",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
# GOOGLE SHEETS INTEGRATION (PLACEHOLDER CONFIG)
# ══════════════════════════════════════════════════════════════════════════════
def save_to_google_sheet(data):
    """Lưu dữ liệu kết quả học tập vào Google Sheets"""
    try:
        # Cần cấu hình st.secrets["gcp_service_account"] và st.secrets["sheet_url"] trên Streamlit Cloud
        if "gcp_service_account" in st.secrets and "sheet_url" in st.secrets:
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            creds_dict = json.loads(st.secrets["gcp_service_account"])
            creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
            client = gspread.authorize(creds)
            sheet = client.open_by_url(st.secrets["sheet_url"]).sheet1
            
            row = [
                data.get("name", ""),
                data.get("subject", ""),
                data.get("topic", ""),
                data.get("score", 0),
                data.get("total", 0),
                data.get("points", 0),
                data.get("level", 1),
                data.get("timestamp", "")
            ]
            sheet.append_row(row)
    except Exception as e:
        # Bỏ qua lỗi để không làm gián đoạn trải nghiệm của trẻ
        pass

# ══════════════════════════════════════════════════════════════════════════════
# CSS TOÀN CỤC – GIAO DIỆN TRẺ EM VUI NHỘN (UPGRADED)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

/* ── Nền & Font ── */
html, body, [class*="css"], .stApp {
    font-family: 'Baloo 2', cursive !important;
}
.stApp {
    background-color: #FFF4FC;
    background-image:
        radial-gradient(circle at 15% 15%, #FFD6E8 0%, transparent 35%),
        radial-gradient(circle at 85% 10%, #C8F0FF 0%, transparent 35%),
        radial-gradient(circle at 50% 90%, #D4FFD6 0%, transparent 35%),
        radial-gradient(#FFD93D22 2px, transparent 2px),
        radial-gradient(#FF6BCB22 2px, transparent 2px);
    background-size: 100% 100%, 100% 100%, 100% 100%, 50px 50px, 50px 50px;
    background-position: 0 0, 0 0, 0 0, 0 0, 25px 25px;
    animation: bgFloat 20s infinite alternate linear;
}
header[data-testid="stHeader"] { display: none; }
.block-container { padding-top: 1rem !important; max-width: 700px !important; }

/* ══ MÀN ONBOARDING ══ */
.onboard-wrap { text-align: center; padding: 20px 0 10px; animation: fadeSlideUp 0.6s ease both; }
.onboard-mascot { font-size: 120px; line-height: 1; margin-bottom: 10px; display: block; animation: floatMascot 3s ease-in-out infinite; }
.onboard-title { font-family: 'Nunito', sans-serif; font-size: 40px; font-weight: 900; background: linear-gradient(135deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF); background-size: 300%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradShift 4s ease infinite; margin: 0 0 6px; line-height: 1.2; }
.onboard-sub { font-size: 18px; color: #7c3aed; font-weight: 700; margin: 0 0 28px; }

/* ══ HUD THANH TRẠNG THÁI ══ */
.hud-bar { display: flex; align-items: center; justify-content: space-between; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 20px; padding: 10px 18px; margin-bottom: 16px; box-shadow: 0 4px 18px rgba(26,26,46,0.25); gap: 8px; flex-wrap: wrap; border: 2px solid #FFD93D; }
.hud-item { display: flex; flex-direction: column; align-items: center; gap: 1px; min-width: 60px; }
.hud-val { font-size: 20px; font-weight: 800; color: #FFD93D; line-height: 1; }
.hud-lbl { font-size: 10px; font-weight: 700; color: #9ca3af; text-transform: uppercase; letter-spacing: .06em; }
.hud-sep { width: 2px; height: 32px; background: #ffffff33; flex-shrink: 0; }
.hud-name { font-size: 14px; font-weight: 800; color: #ffffff; background: linear-gradient(135deg, #FF6B6B, #FF9A3C); padding: 4px 12px; border-radius: 99px; white-space: nowrap; box-shadow: 0 2px 10px rgba(255,107,107,0.4); }

/* ══ TRANG CHỦ ══ */
.home-title { text-align: center; font-family: 'Nunito', sans-serif; font-size: 42px; font-weight: 900; color: #1a1a2e; margin: 4px 0 4px; animation: bounce 2s infinite; }
.home-sub { text-align: center; font-size: 16px; color: #7c3aed; margin: 0 0 20px; font-weight: 600; }
.greeting-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 18px; padding: 14px 20px; margin-bottom: 18px; text-align: center; box-shadow: 0 6px 20px rgba(102,126,234,0.35); position: relative; overflow: hidden; }
.greeting-box::after { content: '✨'; position: absolute; right: 10px; top: 10px; opacity: 0.5; animation: sparkle 2s infinite; }
.greeting-text { font-size: 22px; font-weight: 800; color: #fff; margin: 0; }

/* ══ CARD MÔN HỌC ══ */
.subject-card-math, .subject-card-viet { border-radius: 28px; padding: 28px 16px 22px; text-align: center; margin-bottom: 10px; transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s; position: relative; overflow: hidden; }
.subject-card-math { background: linear-gradient(135deg, #FFF3CD 0%, #FFE082 60%, #FFD93D 100%); border: 3px solid #FFD93D; box-shadow: 0 8px 24px rgba(255,217,61,0.3); }
.subject-card-viet { background: linear-gradient(135deg, #DCFCE7 0%, #BBF7D0 60%, #4ade80 100%); border: 3px solid #22c55e; box-shadow: 0 8px 24px rgba(34,197,94,0.3); }
.subject-card-math:hover, .subject-card-viet:hover { transform: translateY(-8px) scale(1.02); box-shadow: 0 12px 30px rgba(0,0,0,0.15); }
.subject-icon { font-size: 65px; line-height: 1.1; margin-bottom: 10px; display: block; animation: wobble 3s infinite; filter: drop-shadow(0px 4px 4px rgba(0,0,0,0.1)); }
.subject-name { font-size: 26px; font-weight: 900; color: #1a1a2e; margin: 0 0 4px; }
.subject-count { font-size: 14px; color: #4b5563; font-weight: 700; }
.badge { display: inline-block; font-size: 13px; font-weight: 800; padding: 6px 16px; border-radius: 99px; margin-top: 10px; letter-spacing: .04em; text-transform: uppercase; }
.badge-math { background: linear-gradient(135deg, #FF9A3C, #FF6B6B); color: #fff; box-shadow: 0 4px 10px rgba(255,107,107,0.4); }
.badge-viet { background: linear-gradient(135deg, #22c55e, #16a34a); color: #fff; box-shadow: 0 4px 10px rgba(34,197,94,0.4); }

/* ══ KẾT QUẢ & LEADERBOARD ══ */
.dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 10px; }
.recent-box, .badge-box { background: #ffffff; border: 2.5px solid #e9d5ff; border-radius: 20px; padding: 14px 18px; box-shadow: 0 3px 12px rgba(124,58,237,0.1); }
.box-title { font-size: 14px; font-weight: 900; color: #7c3aed; text-transform: uppercase; letter-spacing: .06em; margin: 0 0 12px; display: flex; align-items: center; gap: 6px; }

/* ══ CHỌN CHỦ ĐỀ ══ */
.topic-item { background: #fff; border: 3px solid #e9d5ff; border-radius: 18px; padding: 16px 20px; font-size: 18px; font-weight: 800; color: #1a1a2e; margin-bottom: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: all 0.2s; display: flex; align-items: center; }
.topic-item:hover { border-color: #a855f7; transform: translateX(5px); }

/* ══ TIẾN TRÌNH ══ */
.progress-outer { background: #e9d5ff; border-radius: 99px; height: 22px; margin-bottom: 16px; overflow: hidden; border: 3px solid #c4b5fd; position: relative; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1); }
.progress-inner { height: 100%; background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF, #a855f7); background-size: 400% 100%; border-radius: 99px; animation: shimmer 3s linear infinite; transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); position: relative; }
.progress-inner::after { content: '⭐'; position: absolute; right: -10px; top: -5px; font-size: 24px; animation: sparkle 0.8s ease infinite alternate; filter: drop-shadow(0 2px 2px rgba(0,0,0,0.2)); }
.q-counter { font-size: 16px; font-weight: 900; color: #7c3aed; text-align: right; margin-bottom: 6px; }

/* ══ KHUNG CÂU HỎI ══ */
.q-box { border-radius: 26px; padding: 35px 24px; text-align: center; margin-bottom: 24px; position: relative; overflow: hidden; animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.q-box-math { background: linear-gradient(135deg, #FF9A3C 0%, #FF6B6B 50%, #c2410c 100%); box-shadow: 0 8px 28px rgba(255,107,107,0.4); border: 4px solid #ffedd5; }
.q-box-viet { background: linear-gradient(135deg, #22c55e 0%, #16a34a 50%, #166534 100%); box-shadow: 0 8px 28px rgba(34,197,94,0.4); border: 4px solid #dcfce7; }
.q-box::before { content: '✨'; position: absolute; top: 12px; right: 18px; font-size: 32px; animation: sparkle 1s ease infinite alternate; }
.q-text { font-size: 28px; font-weight: 900; color: #fff; margin: 0; line-height: 1.4; text-shadow: 0 3px 8px rgba(0,0,0,0.3); }

/* ══ ĐÁP ÁN ══ */
.opt-btn { background: #fff; border: 3px solid #e5e7eb; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 800; color: #374151; width: 100%; text-align: left; margin-bottom: 12px; display: block; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: all 0.2s; }
.opt-correct { background: linear-gradient(135deg, #DCFCE7, #BBF7D0); border: 4px solid #22c55e; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 900; color: #14532d; width: 100%; text-align: left; margin-bottom: 12px; display: block; box-shadow: 0 6px 16px rgba(34,197,94,0.3); animation: correctPulse 0.5s ease; position: relative; }
.opt-correct::after { content: '✅'; position: absolute; right: 20px; font-size: 24px; }
.opt-wrong { background: linear-gradient(135deg, #FEE2E2, #fca5a5); border: 4px solid #ef4444; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 900; color: #7f1d1d; width: 100%; text-align: left; margin-bottom: 12px; display: block; animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both; position: relative; }
.opt-wrong::after { content: '❌'; position: absolute; right: 20px; font-size: 24px; }
.opt-dim { background: #f3f4f6; border: 3px solid #e5e7eb; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 700; color: #9ca3af; width: 100%; text-align: left; margin-bottom: 12px; display: block; opacity: 0.6; }

/* ══ FEEDBACK ══ */
.feedback-box { border-radius: 24px; padding: 24px; margin-top: 10px; animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,0.1); }
.feedback-correct { background: linear-gradient(135deg, #DCFCE7, #d1fae5); border: 4px solid #4ade80; }
.feedback-wrong { background: linear-gradient(135deg, #FFF7ED, #ffedd5); border: 4px dashed #fb923c; }
.feedback-title { font-size: 24px; font-weight: 900; margin: 0 0 8px; }
.txt-correct { color: #166534; } .txt-wrong { color: #9a3412; }
.feedback-msg { font-size: 18px; font-weight: 700; margin: 0 0 12px; }
.bonus-badge { display: inline-block; background: linear-gradient(135deg, #FFD700, #FF8C00); color: white; padding: 4px 12px; border-radius: 20px; font-size: 14px; font-weight: 900; animation: bounce 1s infinite; margin-top: 8px; box-shadow: 0 4px 10px rgba(255,140,0,0.4); }

.feedback-answer { background: #DCFCE7; border: 2px solid #22c55e; border-radius: 16px; padding: 14px; font-size: 18px; font-weight: 900; color: #14532d; margin-bottom: 12px; }
.feedback-explain { background: #FEF9C3; border: 2px solid #FCD34D; border-radius: 16px; padding: 14px; font-size: 16px; font-weight: 700; color: #78350f; line-height: 1.6; white-space: pre-line; text-align: left; }
.explain-title { font-size: 14px; font-weight: 900; color: #92400e; text-transform: uppercase; letter-spacing: .06em; margin-bottom: 8px; text-align: left; }

/* ══ STREAK BANNER ══ */
.streak-banner { background: linear-gradient(135deg, #ff007f, #ff8c00); border-radius: 20px; padding: 12px 20px; text-align: center; font-size: 20px; font-weight: 900; color: #fff; margin-bottom: 16px; animation: slideDown 0.4s cubic-bezier(0.34,1.56,0.64,1); box-shadow: 0 6px 20px rgba(255,140,0,0.4); border: 3px solid #ffd700; }

/* ══ MÀN KẾT QUẢ ══ */
.result-wrap { text-align: center; padding: 10px 0 20px; animation: popIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.result-trophy { font-size: 100px; margin-bottom: 10px; display: block; animation: floatMascot 2.5s infinite ease-in-out; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.2)); }
.result-title { font-family: 'Nunito', sans-serif; font-size: 42px; font-weight: 900; color: #1a1a2e; margin: 0 0 10px; }
.result-msg { font-size: 18px; color: #4b5563; font-weight: 700; margin: 0 0 24px; padding: 0 20px; }

/* BADGES MỚI */
.badge-earned { display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 20px; font-weight: 900; padding: 12px 30px; border-radius: 99px; margin-bottom: 24px; box-shadow: 0 8px 20px rgba(0,0,0,0.2); animation: pulseBadge 2s infinite; }
.badge-superstar { background: linear-gradient(270deg, #ff007f, #ff8c00, #ffd700, #00fa9a, #1e90ff, #9400d3); background-size: 600% 600%; animation: rainbowBG 4s ease infinite; color: #fff; border: 4px solid #fff; }
.badge-gold { background: linear-gradient(135deg, #FFD700, #FFA500); color: #fff; border: 3px solid #fff; }
.badge-silver { background: linear-gradient(135deg, #E0E0E0, #9E9E9E); color: #fff; border: 3px solid #fff; }
.badge-bronze { background: linear-gradient(135deg, #CD7F32, #8B4513); color: #fff; border: 3px solid #fff; }
.badge-try { background: linear-gradient(135deg, #64748b, #475569); color: #fff; }

.score-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; }
.score-box-correct, .score-box-wrong { border-radius: 24px; padding: 24px; text-align: center; }
.score-box-correct { background: linear-gradient(135deg, #DCFCE7, #BBF7D0); border: 3px solid #4ade80; box-shadow: 0 6px 16px rgba(34,197,94,0.25); }
.score-box-wrong { background: linear-gradient(135deg, #FEE2E2, #fca5a5); border: 3px solid #f87171; box-shadow: 0 6px 16px rgba(239,68,68,0.25); }
.score-num { font-size: 50px; font-weight: 900; line-height: 1; }
.score-lbl { font-size: 16px; font-weight: 800; margin-top: 6px; text-transform: uppercase; }

/* ══ THANH TỔNG ĐIỂM KẾT QUẢ ══ */
.total-pts-box { background: linear-gradient(135deg, #1a1a2e, #16213e); border-radius: 24px; padding: 20px; margin-bottom: 24px; display: flex; align-items: center; justify-content: center; gap: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.3); border: 3px solid #FFD93D; animation: popIn 1s; }
.total-pts-icon { font-size: 40px; animation: wobble 2s infinite; }
.total-pts-val { font-size: 32px; font-weight: 900; color: #FFD93D; line-height: 1.1; }
.total-pts-lbl { font-size: 14px; font-weight: 800; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.05em; }

/* ══ BUTTONS ══ */
div.stButton > button { font-family: 'Baloo 2', cursive !important; font-weight: 900 !important; font-size: 18px !important; height: 60px !important; border-radius: 20px !important; transition: transform 0.2s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s !important; letter-spacing: .02em !important; }
div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #FF6B6B, #FF9A3C) !important; border: none !important; color: #fff !important; box-shadow: 0 8px 20px rgba(255,107,107,0.4) !important; }
div.stButton > button[kind="primary"]:hover { transform: translateY(-4px) scale(1.02) !important; box-shadow: 0 12px 28px rgba(255,107,107,0.5) !important; }
div.stButton > button[kind="primary"]:active { transform: scale(0.95) !important; }
div.stButton > button[kind="secondary"] { background: #fff !important; border: 3px solid #e9d5ff !important; color: #7c3aed !important; box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important; }
div.stButton > button[kind="secondary"]:hover { border-color: #a855f7 !important; background: #faf5ff !important; transform: translateY(-3px) !important; box-shadow: 0 8px 16px rgba(168,85,247,0.2) !important; }

/* ══ INPUT ══ */
div[data-testid="stTextInput"] input { font-family: 'Baloo 2', cursive !important; font-size: 20px !important; font-weight: 800 !important; border-radius: 20px !important; border: 3px solid #e9d5ff !important; padding: 14px 20px !important; background: #fff !important; color: #1a1a2e !important; text-align: center; box-shadow: inset 0 2px 6px rgba(0,0,0,0.05); }
div[data-testid="stTextInput"] input:focus { border-color: #a855f7 !important; box-shadow: 0 0 0 4px rgba(168,85,247,0.2) !important; }

/* ══ ANIMATIONS ══ */
@keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
@keyframes wobble { 0%,100%{transform:rotate(0deg)} 15%{transform:rotate(-8deg)} 30%{transform:rotate(6deg)} 45%{transform:rotate(-4deg)} 60%{transform:rotate(2deg)} }
@keyframes popIn { 0%{transform:scale(0.5);opacity:0} 70%{transform:scale(1.05);opacity:1} 100%{transform:scale(1);opacity:1} }
@keyframes shake { 0%,100%{transform:translateX(0)} 10%,30%,50%,70%,90%{transform:translateX(-8px)} 20%,40%,60%,80%{transform:translateX(8px)} }
@keyframes fadeSlideUp { 0%{opacity:0;transform:translateY(30px)} 100%{opacity:1;transform:translateY(0)} }
@keyframes slideDown { 0%{opacity:0;transform:translateY(-20px)} 100%{opacity:1;transform:translateY(0)} }
@keyframes gradShift { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
@keyframes shimmer { 0% { background-position:0% 50%; } 100% { background-position:100% 50%; } }
@keyframes sparkle { 0% { transform: scale(1) rotate(0deg); opacity: 0.8; } 100% { transform: scale(1.3) rotate(20deg); opacity: 1; } }
@keyframes floatMascot { 0%, 100% { transform: translateY(0) rotate(0); } 50% { transform: translateY(-15px) rotate(3deg); } }
@keyframes correctPulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); box-shadow: 0 0 20px #4ade80; } 100% { transform: scale(1); } }
@keyframes rainbowBG { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes pulseBadge { 0% { transform: scale(1); } 50% { transform: scale(1.03); } 100% { transform: scale(1); } }
@keyframes bgFloat { 0% {background-position: 0 0, 0 0, 0 0, 0 0, 25px 25px;} 100% {background-position: 0 0, 0 0, 0 0, 50px 50px, 75px 75px;} }

/* ══ ÂM THANH hidden ══ */
audio { display: none; }
.divider { border:none; border-top: 3px dashed #e9d5ff; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# DỮ LIỆU CÂU HỎI – GIỮ NGUYÊN HOÀN TOÀN
# ══════════════════════════════════════════════════════════════════════════════
SUBJECTS = {
    "math": {
        "label": "Toán", "icon": "🔢", "badge": "badge-math", "q_box_class": "q-box-math",
        "topics": [
            {
                "name": "Phép cộng có nhớ",
                "qs": [
                    {"q":"15 + 7 = ?", "opts":["20","22","23","21"], "ans":1, "explain":"📝 Cách tính: 15 + 7\n→ Lấy 15 + 5 = 20 (tròn chục)\n→ Còn thừa 2, lấy 20 + 2 = 22 ✔"},
                    {"q":"28 + 5 = ?", "opts":["33","31","32","34"], "ans":0, "explain":"📝 Cách tính: 28 + 5\n→ Lấy 28 + 2 = 30 (tròn chục)\n→ Còn thừa 3, lấy 30 + 3 = 33 ✔"},
                    {"q":"36 + 8 = ?", "opts":["44","42","43","45"], "ans":0, "explain":"📝 Cách tính: 36 + 8\n→ Lấy 36 + 4 = 40 (tròn chục)\n→ Còn thừa 4, lấy 40 + 4 = 44 ✔"},
                    {"q":"49 + 6 = ?", "opts":["54","55","53","56"], "ans":1, "explain":"📝 Cách tính: 49 + 6\n→ Lấy 49 + 1 = 50 (tròn chục)\n→ Còn thừa 5, lấy 50 + 5 = 55 ✔"},
                    {"q":"17 + 9 = ?", "opts":["25","27","26","24"], "ans":2, "explain":"📝 Cách tính: 17 + 9\n→ Lấy 17 + 3 = 20 (tròn chục)\n→ Còn thừa 6, lấy 20 + 6 = 26 ✔"},
                    {"q":"38 + 7 = ?", "opts":["44","45","46","43"], "ans":1, "explain":"📝 Cách tính: 38 + 7\n→ Lấy 38 + 2 = 40 (tròn chục)\n→ Còn thừa 5, lấy 40 + 5 = 45 ✔"},
                    {"q":"56 + 8 = ?", "opts":["63","65","64","62"], "ans":2, "explain":"📝 Cách tính: 56 + 8\n→ Lấy 56 + 4 = 60 (tròn chục)\n→ Còn thừa 4, lấy 60 + 4 = 64 ✔"},
                    {"q":"27 + 6 = ?", "opts":["33","34","32","35"], "ans":0, "explain":"📝 Cách tính: 27 + 6\n→ Lấy 27 + 3 = 30 (tròn chục)\n→ Còn thừa 3, lấy 30 + 3 = 33 ✔"},
                    {"q":"45 + 9 = ?", "opts":["53","55","54","52"], "ans":2, "explain":"📝 Cách tính: 45 + 9\n→ Lấy 45 + 5 = 50 (tròn chục)\n→ Còn thừa 4, lấy 50 + 4 = 54 ✔"},
                    {"q":"67 + 8 = ?", "opts":["75","74","76","77"], "ans":0, "explain":"📝 Cách tính: 67 + 8\n→ Lấy 67 + 3 = 70 (tròn chục)\n→ Còn thừa 5, lấy 70 + 5 = 75 ✔"},
                ],
            },
            {
                "name": "Phép trừ có nhớ",
                "qs": [
                    {"q":"23 - 7 = ?", "opts":["16","15","14","17"], "ans":0, "explain":"📝 Cách tính: 23 - 7\n→ Lấy 23 - 3 = 20\n→ Còn trừ 4, lấy 20 - 4 = 16 ✔"},
                    {"q":"41 - 6 = ?", "opts":["34","36","35","33"], "ans":2, "explain":"📝 Cách tính: 41 - 6\n→ Lấy 41 - 1 = 40\n→ Còn trừ 5, lấy 40 - 5 = 35 ✔"},
                    {"q":"52 - 8 = ?", "opts":["44","45","43","42"], "ans":0, "explain":"📝 Cách tính: 52 - 8\n→ Lấy 52 - 2 = 50\n→ Còn trừ 6, lấy 50 - 6 = 44 ✔"},
                    {"q":"30 - 4 = ?", "opts":["26","28","25","27"], "ans":0, "explain":"📝 Cách tính: 30 - 4\n→ 30 bằng 20 + 10\n→ Lấy 10 - 4 = 6\n→ 20 + 6 = 26 ✔"},
                    {"q":"61 - 9 = ?", "opts":["51","53","52","54"], "ans":2, "explain":"📝 Cách tính: 61 - 9\n→ Lấy 61 - 1 = 60\n→ Còn trừ 8, lấy 60 - 8 = 52 ✔"},
                    {"q":"74 - 7 = ?", "opts":["67","65","66","68"], "ans":0, "explain":"📝 Cách tính: 74 - 7\n→ Lấy 74 - 4 = 70\n→ Còn trừ 3, lấy 70 - 3 = 67 ✔"},
                    {"q":"83 - 5 = ?", "opts":["77","79","78","76"], "ans":2, "explain":"📝 Cách tính: 83 - 5\n→ Lấy 83 - 3 = 80\n→ Còn trừ 2, lấy 80 - 2 = 78 ✔"},
                    {"q":"46 - 8 = ?", "opts":["38","37","39","36"], "ans":0, "explain":"📝 Cách tính: 46 - 8\n→ Lấy 46 - 6 = 40\n→ Còn trừ 2, lấy 40 - 2 = 38 ✔"},
                    {"q":"55 - 6 = ?", "opts":["49","48","50","47"], "ans":0, "explain":"📝 Cách tính: 55 - 6\n→ Lấy 55 - 5 = 50\n→ Còn trừ 1, lấy 50 - 1 = 49 ✔"},
                    {"q":"91 - 3 = ?", "opts":["89","87","88","86"], "ans":2, "explain":"📝 Cách tính: 91 - 3\n→ Lấy 91 - 1 = 90\n→ Còn trừ 2, lấy 90 - 2 = 88 ✔"},
                ],
            },
            {
                "name": "So sánh số",
                "qs": [
                    {"q":"Số nào lớn hơn: 45 hay 54?", "opts":["45","54","Bằng nhau","Không biết"], "ans":1, "explain":"📝 So sánh chữ số hàng chục trước:\n→ 45 có hàng chục là 4\n→ 54 có hàng chục là 5\n→ 5 > 4, nên 54 > 45 ✔"},
                    {"q":"Điền dấu: 73 __ 37", "opts":["<",">","=","Không biết"], "ans":1, "explain":"📝 So sánh hàng chục:\n→ 73 có hàng chục là 7\n→ 37 có hàng chục là 3\n→ 7 > 3, nên 73 > 37 ✔"},
                    {"q":"Số liền sau của 99 là?", "opts":["98","100","101","97"], "ans":1, "explain":"📝 Số liền sau = số đó + 1\n→ 99 + 1 = 100 ✔"},
                    {"q":"Số liền trước của 50 là?", "opts":["51","49","48","52"], "ans":1, "explain":"📝 Số liền trước = số đó - 1\n→ 50 - 1 = 49 ✔"},
                    {"q":"Điền dấu: 68 __ 86", "opts":[">","<","=","Không biết"], "ans":1, "explain":"📝 So sánh hàng chục:\n→ 68 có hàng chục là 6\n→ 86 có hàng chục là 8\n→ 6 < 8, nên 68 < 86 ✔"},
                    {"q":"Số nào nhỏ nhất: 25, 52, 22, 55?", "opts":["25","52","22","55"], "ans":2, "explain":"📝 So sánh hàng chục:\n→ 25, 22 cùng hàng chục là 2 (nhỏ nhất)\n→ So tiếp hàng đơn vị: 2 < 5\n→ 22 là số nhỏ nhất ✔"},
                    {"q":"Số nào lớn nhất: 31, 13, 33, 11?", "opts":["31","13","33","11"], "ans":2, "explain":"📝 So sánh hàng chục:\n→ 31, 33 cùng hàng chục là 3 (lớn nhất)\n→ So tiếp hàng đơn vị: 3 > 1\n→ 33 là số lớn nhất ✔"},
                    {"q":"Điền dấu: 40 __ 40", "opts":[">","<","=","Không biết"], "ans":2, "explain":"📝 Hai số giống nhau hoàn toàn\n→ 40 = 40 ✔"},
                    {"q":"Số liền sau của 79 là?", "opts":["78","80","81","77"], "ans":1, "explain":"📝 Số liền sau = số đó + 1\n→ 79 + 1 = 80 ✔"},
                    {"q":"Số liền trước của 100 là?", "opts":["99","101","98","102"], "ans":0, "explain":"📝 Số liền trước = số đó - 1\n→ 100 - 1 = 99 ✔"},
                ],
            },
            {
                "name": "Đo lường",
                "qs": [
                    {"q":"1 dm = ? cm", "opts":["5 cm","10 cm","100 cm","1 cm"], "ans":1, "explain":"📝 Ghi nhớ: 1 dm = 10 cm\n→ dm là đề-xi-mét, lớn hơn cm\n→ 1 dm bằng 10 cm xếp thẳng hàng ✔"},
                    {"q":"1 m = ? dm", "opts":["100 dm","1 dm","10 dm","5 dm"], "ans":2, "explain":"📝 Ghi nhớ: 1 m = 10 dm\n→ Cây thước 1 mét chia thành 10 đoạn, mỗi đoạn là 1 dm ✔"},
                    {"q":"30 cm = ? dm", "opts":["3 dm","30 dm","300 dm","13 dm"], "ans":0, "explain":"📝 Đổi cm → dm: chia cho 10\n→ 30 ÷ 10 = 3\n→ 30 cm = 3 dm ✔"},
                    {"q":"20 dm = ? m", "opts":["20 m","200 m","2 m","0,2 m"], "ans":2, "explain":"📝 Đổi dm → m: chia cho 10\n→ 20 ÷ 10 = 2\n→ 20 dm = 2 m ✔"},
                    {"q":"1 m = ? cm", "opts":["10 cm","1000 cm","100 cm","1 cm"], "ans":2, "explain":"📝 Ghi nhớ: 1 m = 100 cm\n→ 1 m = 10 dm, mà 1 dm = 10 cm\n→ 10 × 10 = 100 cm ✔"},
                    {"q":"5 dm = ? cm", "opts":["5 cm","500 cm","50 cm","15 cm"], "ans":2, "explain":"📝 Đổi dm → cm: nhân với 10\n→ 5 × 10 = 50\n→ 5 dm = 50 cm ✔"},
                    {"q":"2 m = ? dm", "opts":["2 dm","200 dm","20 dm","12 dm"], "ans":2, "explain":"📝 Đổi m → dm: nhân với 10\n→ 2 × 10 = 20\n→ 2 m = 20 dm ✔"},
                    {"q":"40 cm = ? dm", "opts":["40 dm","400 dm","4 dm","14 dm"], "ans":2, "explain":"📝 Đổi cm → dm: chia cho 10\n→ 40 ÷ 10 = 4\n→ 40 cm = 4 dm ✔"},
                    {"q":"3 m = ? cm", "opts":["3 cm","30 cm","300 cm","3000 cm"], "ans":2, "explain":"📝 Đổi m → cm: nhân với 100\n→ 3 × 100 = 300\n→ 3 m = 300 cm ✔"},
                    {"q":"6 dm = ? cm", "opts":["6 cm","600 cm","60 cm","16 cm"], "ans":2, "explain":"📝 Đổi dm → cm: nhân với 10\n→ 6 × 10 = 60\n→ 6 dm = 60 cm ✔"},
                ],
            },
            {
                "name": "Hình học",
                "qs": [
                    {"q":"Hình chữ nhật có bao nhiêu góc vuông?", "opts":["2","3","4","1"], "ans":2, "explain":"📝 Hình chữ nhật có 4 góc\n→ Tất cả 4 góc đều là góc vuông (90°)\n→ Đếm 4 góc bốn cạnh nhé! ✔"},
                    {"q":"Hình vuông có bao nhiêu cạnh bằng nhau?", "opts":["2","3","0","4"], "ans":3, "explain":"📝 Hình vuông đặc biệt: 4 cạnh đều bằng nhau\n→ Khác hình chữ nhật chỉ có 2 cặp cạnh bằng nhau ✔"},
                    {"q":"Hình tam giác có bao nhiêu cạnh?", "opts":["4","2","3","5"], "ans":2, "explain":"📝 'Tam giác' nghĩa là 'ba góc'\n→ Ba góc thì có ba cạnh\n→ Đếm: cạnh 1, cạnh 2, cạnh 3 ✔"},
                    {"q":"Hình nào có tất cả các cạnh bằng nhau?", "opts":["Hình chữ nhật","Hình tam giác","Hình vuông","Hình thang"], "ans":2, "explain":"📝 Hình vuông: 4 cạnh bằng nhau hoàn toàn\n→ Hình chữ nhật: chỉ 2 cặp cạnh bằng nhau\n→ Hình vuông là đặc biệt nhất! ✔"},
                    {"q":"Hình tròn có bao nhiêu góc?", "opts":["1","2","3","0"], "ans":3, "explain":"📝 Hình tròn không có góc, không có cạnh thẳng\n→ Đường tròn cong liền tục, không có điểm gãy ✔"},
                    {"q":"Hình chữ nhật có bao nhiêu cạnh?", "opts":["3","4","5","6"], "ans":1, "explain":"📝 Hình chữ nhật có 4 cạnh\n→ 2 cạnh dài (chiều dài) và 2 cạnh ngắn (chiều rộng) ✔"},
                    {"q":"Hình nào KHÔNG có góc vuông?", "opts":["Hình vuông","Hình chữ nhật","Hình tròn","Tất cả"], "ans":2, "explain":"📝 Hình tròn không có góc nào cả\n→ Hình vuông và chữ nhật đều có 4 góc vuông\n→ Hình tròn trơn tru, không góc cạnh ✔"},
                    {"q":"Hình tam giác có bao nhiêu góc?", "opts":["2","4","3","1"], "ans":2, "explain":"📝 Tam giác = ba + góc\n→ Có 3 cạnh thì có 3 góc\n→ Đếm các điểm nhọn: 3 góc ✔"},
                    {"q":"Hình vuông có bao nhiêu cạnh?", "opts":["3","5","6","4"], "ans":3, "explain":"📝 Hình vuông có 4 cạnh bằng nhau\n→ Giống hình chữ nhật nhưng cả 4 cạnh đều bằng nhau ✔"},
                    {"q":"Hình chữ nhật: cạnh dài gọi là?", "opts":["Chiều rộng","Chiều cao","Chiều dài","Cạnh bên"], "ans":2, "explain":"📝 Hình chữ nhật có 2 loại cạnh:\n→ Cạnh DÀI hơn gọi là chiều dài\n→ Cạnh NGẮN hơn gọi là chiều rộng ✔"},
                ],
            },
        ],
    },
    "viet": {
        "label": "Tiếng Việt", "icon": "📖", "badge": "badge-viet", "q_box_class": "q-box-viet",
        "topics": [
            {
                "name": "Chính tả – âm vần",
                "qs": [
                    {"q":"Chọn từ viết đúng chính tả:", "opts":["giòng sông","dòng sông","giòng xông","dòng xông"], "ans":1, "explain":"📝 Mẹo nhớ: 'dòng sông' viết với 'd'\n→ 'Dòng' chỉ sự chuyển động liên tục của nước\n→ 'Gi' không đứng trước vần 'ong' trong trường hợp này ✔"},
                    {"q":"Từ nào viết đúng?", "opts":["xanh lá cây","sanh lá cây","xanh lá kay","xang lá cây"], "ans":0, "explain":"📝 Mẹo nhớ: 'xanh' viết với 'x'\n→ Các màu sắc thường: xanh, xám, xỉn...\n→ 'Sanh' là một từ khác, không phải màu sắc ✔"},
                    {"q":"Điền vào chỗ trống: con ...ó (c/g)", "opts":["co","gó","có","gò"], "ans":2, "explain":"📝 'Con có' viết với 'c'\n→ Con có là loài chim nhỏ, tiếng kêu 'cú có'\n→ Phân biệt: 'c' đứng trước 'o, a, ô, u' ✔"},
                    {"q":"Chọn từ đúng: trời mưa hay giời mưa?", "opts":["giời mưa","trời mưa","trởi mưa","chời mưa"], "ans":1, "explain":"📝 'Trời' viết với 'tr'\n→ Mẹo nhớ: tr + ời = trời\n→ 'Giời' là cách nói địa phương, không phải chính tả chuẩn ✔"},
                    {"q":"Từ nào viết sai?", "opts":["quả cam","quả xoài","quả dưa","quả khôm"], "ans":3, "explain":"📝 'Quả khôm' viết sai\n→ Viết đúng là 'quả khóm' (dứa/thơm)\n→ Chú ý dấu sắc trên chữ 'o' ✔"},
                    {"q":"Điền vào: bầu ....i (tr/ch)", "opts":["chời","trời","cời","gời"], "ans":1, "explain":"📝 'Bầu trời' viết với 'tr'\n→ Mẹo: tr đứng trước vần 'ời' trong từ 'trời'\n→ Các từ 'tr' khác: trăng, trắng, trong... ✔"},
                    {"q":"Chọn từ đúng:", "opts":["con trâu","con châu","con trau","con chau"], "ans":0, "explain":"📝 'Con trâu' viết với 'tr' và dấu huyền trên 'â'\n→ Mẹo: tr + âu + dấu huyền = trâu\n→ Con trâu là con vật kéo cày ✔"},
                    {"q":"Từ nào viết đúng?", "opts":["buổi sáng","buổi xáng","buỗi sáng","buổi sạng"],"ans":0, "explain":"📝 'Buổi sáng' viết đúng:\n→ 'buổi' dấu hỏi trên 'ô'\n→ 'sáng' dấu sắc trên 'a'\n→ Chú ý đặt đúng vị trí dấu ✔"},
                    {"q":"Điền vào: hoa ...ồng (h/r)", "opts":["rồng","hồng","lồng","đồng"], "ans":1, "explain":"📝 'Hoa hồng' viết với 'h'\n→ Mẹo: hoa + hồng (cùng bắt đầu bằng 'h')\n→ Hoa hồng là loài hoa đẹp, màu hồng ✔"},
                    {"q":"Chọn từ đúng:", "opts":["lá cây","lá kây","la cây","lá cay"], "ans":0, "explain":"📝 'Lá cây' viết đúng:\n→ 'lá' có dấu sắc\n→ 'cây' không dấu\n→ Chú ý: 'cay' (ớt cay) khác 'cây' (cây xanh) ✔"},
                ],
            },
            {
                "name": "Từ loại – danh từ",
                "qs": [
                    {"q":"Từ nào là danh từ?", "opts":["chạy","đẹp","bàn","nhanh"], "ans":2, "explain":"📝 Danh từ là từ chỉ sự vật:\n→ 'chạy' = hành động (động từ)\n→ 'đẹp', 'nhanh' = tính chất (tính từ)\n→ 'bàn' = đồ vật → là danh từ ✔"},
                    {"q":"Chọn danh từ:", "opts":["học","ghế","vui","xanh"], "ans":1, "explain":"📝 Danh từ chỉ sự vật, đồ vật:\n→ 'học' = hành động\n→ 'vui', 'xanh' = tính chất\n→ 'ghế' = đồ vật → là danh từ ✔"},
                    {"q":"Từ nào KHÔNG phải danh từ?", "opts":["sách","vở","đọc","bút"], "ans":2, "explain":"📝 'Đọc' là động từ (hành động)\n→ 'sách, vở, bút' đều là đồ vật = danh từ\n→ 'Đọc' chỉ hành động, không phải vật ✔"},
                    {"q":"Danh từ chỉ người:", "opts":["chạy","thầy giáo","đẹp","vàng"], "ans":1, "explain":"📝 Danh từ chỉ người gồm: tên người, nghề nghiệp...\n→ 'thầy giáo' chỉ một người cụ thể\n→ Các danh từ chỉ người khác: học sinh, bác sĩ, mẹ... ✔"},
                    {"q":"Chọn danh từ chỉ con vật:", "opts":["bay","to","con mèo","nhanh"], "ans":2, "explain":"📝 Danh từ chỉ con vật gồm tên các loài vật:\n→ 'bay', 'nhanh' = hành động, tính chất\n→ 'con mèo' = tên con vật → là danh từ ✔"},
                    {"q":"Từ nào là danh từ?", "opts":["nhảy","hát","trường học","vui vẻ"], "ans":2, "explain":"📝 'Trường học' là nơi chốn = danh từ\n→ 'nhảy, hát' = hành động (động từ)\n→ 'vui vẻ' = tính chất (tính từ) ✔"},
                    {"q":"Danh từ chỉ đồ vật:", "opts":["cái bàn","chạy","đẹp","xanh"], "ans":0, "explain":"📝 'Cái bàn' là đồ vật ta có thể nhìn thấy, sờ được\n→ Danh từ chỉ đồ vật thường đi kèm: cái, con, chiếc...\n→ Ví dụ: cái ghế, cái cặp, cái bút ✔"},
                    {"q":"Chọn danh từ:", "opts":["nhìn","ngủ","ăn","cây bút"], "ans":3, "explain":"📝 'Cây bút' là đồ vật = danh từ\n→ 'nhìn, ngủ, ăn' đều là hành động (động từ)\n→ Danh từ là những gì ta có thể thấy, cầm, nắm ✔"},
                    {"q":"Từ nào là danh từ?", "opts":["vui","buồn","hạnh phúc","ngôi nhà"], "ans":3, "explain":"📝 'Ngôi nhà' là nơi chốn ta ở = danh từ\n→ 'vui, buồn, hạnh phúc' chỉ cảm xúc (tính từ)\n→ Nhà, trường, chợ, sân... đều là danh từ ✔"},
                    {"q":"Danh từ chỉ nơi chốn:", "opts":["đẹp","chơi","trường học","nhanh"], "ans":2, "explain":"📝 Danh từ chỉ nơi chốn: tên địa điểm, nơi ở\n→ 'trường học' là nơi ta đến học mỗi ngày\n→ Các danh từ nơi chốn khác: chợ, bệnh viện, công viên ✔"},
                ],
            },
            {
                "name": "Đặt câu – câu hỏi",
                "qs": [
                    {"q":"Câu hỏi thường dùng từ nào?", "opts":["vì","và","Ai? Cái gì?","nhưng"], "ans":2, "explain":"📝 Câu hỏi dùng các từ để hỏi:\n→ Ai? Cái gì? Ở đâu? Khi nào? Như thế nào?\n→ 'vì, và, nhưng' là từ nối, không phải từ hỏi ✔"},
                    {"q":"Câu 'Con đang làm gì?' hỏi về điều gì?", "opts":["Người","Thời gian","Hành động","Nơi chốn"], "ans":2, "explain":"📝 'Làm gì?' → hỏi về hành động\n→ Ví dụ trả lời: 'Con đang học bài / vẽ tranh'\n→ Từ hỏi hành động: làm gì? đang làm gì? ✔"},
                    {"q":"Chọn câu hỏi đúng:", "opts":["Bạn ăn gì không?","Bạn ăn gì?","Bạn ăn gì nhỉ không?","Bạn ăn gì à không?"],"ans":1, "explain":"📝 Câu hỏi chuẩn: 'Bạn ăn gì?'\n→ Ngắn gọn, rõ ràng, có từ hỏi 'gì'\n→ Kết thúc bằng dấu chấm hỏi ✔"},
                    {"q":"Từ hỏi 'Ở đâu?' hỏi về điều gì?", "opts":["Người","Nơi chốn","Thời gian","Số lượng"], "ans":1, "explain":"📝 'Ở đâu?' hỏi về nơi chốn\n→ Ví dụ: 'Trường học ở đâu?'\n→ Trả lời: 'Trường học ở gần nhà em' ✔"},
                    {"q":"'Ai đang học bài?' — Từ hỏi là?", "opts":["đang","học","Ai","bài"], "ans":2, "explain":"📝 'Ai?' là từ dùng để hỏi về người\n→ Câu này hỏi: Người nào đang học bài?\n→ Trả lời: 'Bạn Nam đang học bài' ✔"},
                    {"q":"Từ hỏi 'Khi nào?' hỏi về điều gì?", "opts":["Người","Nơi chốn","Thời gian","Cách thức"], "ans":2, "explain":"📝 'Khi nào?' hỏi về thời gian\n→ Ví dụ: 'Khi nào bạn đi học?'\n→ Trả lời: 'Mình đi học lúc 7 giờ sáng' ✔"},
                    {"q":"Câu hỏi kết thúc bằng dấu gì?", "opts":["Dấu chấm","Dấu phẩy","Dấu chấm hỏi","Dấu chấm than"], "ans":2, "explain":"📝 Câu hỏi luôn kết thúc bằng dấu chấm hỏi (?)\n→ Câu kể → dấu chấm (.)\n→ Câu cảm → dấu chấm than (!)\n→ Câu hỏi → dấu hỏi (?) ✔"},
                    {"q":"Chọn câu hỏi:", "opts":["Trời mưa to.","Trời có mưa không?","Trời mưa rất to!","Trời mưa, lạnh quá."],"ans":1, "explain":"📝 'Trời có mưa không?' là câu hỏi\n→ Có từ hỏi 'không?' ở cuối\n→ Kết thúc bằng dấu chấm hỏi ✔"},
                    {"q":"'Tại sao bạn khóc?' hỏi về điều gì?", "opts":["Người","Nơi chốn","Thời gian","Lý do"], "ans":3, "explain":"📝 'Tại sao?' hỏi về lý do, nguyên nhân\n→ Trả lời: 'Vì mình bị đau / vì mình buồn'\n→ Từ hỏi lý do: tại sao? vì sao? ✔"},
                    {"q":"Từ hỏi 'Như thế nào?' hỏi về điều gì?", "opts":["Người","Cách thức","Thời gian","Số lượng"], "ans":1, "explain":"📝 'Như thế nào?' hỏi về cách thức, tính chất\n→ Ví dụ: 'Bạn học như thế nào?'\n→ Trả lời: 'Mình học chăm chỉ / học giỏi' ✔"},
                ],
            },
            {
                "name": "Từ đồng nghĩa – trái nghĩa",
                "qs": [
                    {"q":"Từ trái nghĩa với 'to' là?", "opts":["lớn","bé","cao","nặng"], "ans":1, "explain":"📝 Từ trái nghĩa là từ có nghĩa ngược lại:\n→ to ↔ bé (nhỏ)\n→ 'lớn' gần nghĩa với 'to', không phải trái nghĩa ✔"},
                    {"q":"Từ đồng nghĩa với 'vui' là?", "opts":["buồn","tức","vui vẻ","khóc"], "ans":2, "explain":"📝 Từ đồng nghĩa là từ có nghĩa giống nhau:\n→ 'vui' và 'vui vẻ' cùng chỉ cảm xúc tích cực\n→ 'buồn' là trái nghĩa của 'vui' ✔"},
                    {"q":"Từ trái nghĩa với 'ngày' là?", "opts":["sáng","chiều","đêm","tối"], "ans":2, "explain":"📝 Ngày ↔ Đêm\n→ Ban ngày: mặt trời mọc, sáng sủa\n→ Ban đêm: không có mặt trời, tối tăm\n→ 'tối' chỉ trạng thái, 'đêm' là trái nghĩa hoàn toàn ✔"},
                    {"q":"Từ đồng nghĩa với 'nhanh' là?", "opts":["chậm","mau","lâu","trễ"], "ans":1, "explain":"📝 'nhanh' và 'mau' đều chỉ tốc độ cao:\n→ 'Chạy nhanh' = 'Chạy mau'\n→ 'chậm, lâu, trễ' đều là trái nghĩa của 'nhanh' ✔"},
                    {"q":"Từ trái nghĩa với 'đen' là?", "opts":["xanh","vàng","trắng","đỏ"], "ans":2, "explain":"📝 Đen ↔ Trắng\n→ Đây là cặp màu đối lập nhau hoàn toàn\n→ Trong hội họa: đen và trắng là 2 cực của sáng tối ✔"},
                    {"q":"Từ đồng nghĩa với 'đẹp' là?", "opts":["xấu","xinh","to","nhỏ"], "ans":1, "explain":"📝 'đẹp' và 'xinh' cùng nghĩa:\n→ 'Bạn ấy đẹp' = 'Bạn ấy xinh'\n→ 'xấu' là trái nghĩa\n→ Các từ đồng nghĩa khác: dễ nhìn, duyên dáng ✔"},
                    {"q":"Từ trái nghĩa với 'nóng' là?", "opts":["ấm","mát","lạnh","nguội"], "ans":2, "explain":"📝 Nóng ↔ Lạnh\n→ 'ấm' và 'mát' là mức trung gian\n→ 'nguội' chỉ thức ăn/nước mất nhiệt\n→ 'lạnh' là đối lập hoàn toàn với 'nóng' ✔"},
                    {"q":"Từ đồng nghĩa với 'nhà' là?", "opts":["trường","chợ","ngôi nhà","phố"],"ans":2, "explain":"📝 'nhà' và 'ngôi nhà' cùng nghĩa:\n→ Chỉ công trình dùng để ở\n→ 'trường, chợ' là loại nhà khác\n→ 'phố' chỉ con đường có nhiều nhà ✔"},
                    {"q":"Từ trái nghĩa với 'cao' là?", "opts":["to","thấp","lớn","béo"], "ans":1, "explain":"📝 Cao ↔ Thấp\n→ Cao: khoảng cách từ chân đến đầu lớn\n→ Thấp: khoảng cách đó nhỏ\n→ 'to, lớn, béo' nói về kích thước khác ✔"},
                    {"q":"Từ đồng nghĩa với 'nhìn' là?", "opts":["nghe","ngửi","xem","sờ"], "ans":2, "explain":"📝 'nhìn' và 'xem' đều dùng mắt:\n→ 'nhìn' thường ngắn, 'xem' thường lâu hơn\n→ 'nghe' = dùng tai, 'ngửi' = dùng mũi, 'sờ' = dùng tay ✔"},
                ],
            },
            {
                "name": "Đọc hiểu – câu văn",
                "qs": [
                    {"q":"'Mặt trời mọc ở hướng nào?' — Câu trả lời đúng:", "opts":["Hướng Tây","Hướng Bắc","Hướng Đông","Hướng Nam"], "ans":2, "explain":"📝 Mặt trời mọc ở hướng Đông\n→ Buổi sáng: mặt trời xuất hiện ở phía Đông\n→ Buổi chiều: mặt trời lặn ở phía Tây ✔"},
                    {"q":"Câu 'Con mèo đang ngủ.' nói về con vật nào?", "opts":["Con chó","Con mèo","Con gà","Con cá"], "ans":1, "explain":"📝 Đọc kỹ câu văn:\n→ 'Con mèo đang ngủ'\n→ Chủ ngữ (ai/cái gì) = con mèo\n→ Câu văn nói về con mèo ✔"},
                    {"q":"Câu văn nào tả về thời tiết?", "opts":["Em đi học.","Trời hôm nay nắng đẹp.","Con mèo đen.","Bạn Nam chạy nhanh."], "ans":1, "explain":"📝 'Trời hôm nay nắng đẹp' tả thời tiết:\n→ 'Trời' và 'nắng' là từ chỉ thời tiết\n→ Các câu khác tả người và con vật ✔"},
                    {"q":"'Mùa hè, trời ____.' — Điền từ phù hợp:", "opts":["lạnh giá","mưa phùn","nắng nóng","có tuyết"], "ans":2, "explain":"📝 Mùa hè ở Việt Nam:\n→ Thời tiết nóng bức, nhiều nắng\n→ 'lạnh giá, mưa phùn, có tuyết' là thời tiết mùa đông\n→ Mùa hè → nắng nóng ✔"},
                    {"q":"Đoạn văn tả cảnh vườn thường có từ nào?", "opts":["xe cộ","hoa lá","sóng biển","núi cao"], "ans":1, "explain":"📝 Cảnh vườn gồm: cây cối, hoa, lá...\n→ 'hoa lá' phù hợp nhất với cảnh vườn\n→ 'xe cộ' = phố phường, 'sóng biển' = biển, 'núi cao' = rừng núi ✔"},
                    {"q":"'Em thích ăn quả gì?' — Đây là câu gì?", "opts":["Câu kể","Câu cảm","Câu hỏi","Câu cầu khiến"], "ans":2, "explain":"📝 Câu hỏi có từ hỏi 'gì?' và dấu (?)\n→ 'Em thích ăn quả gì?' đang hỏi để biết thông tin\n→ Kết thúc bằng dấu chấm hỏi ✔"},
                    {"q":"Câu 'Ơi, đẹp quá!' là câu gì?", "opts":["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans":2, "explain":"📝 Câu cảm thể hiện cảm xúc mạnh:\n→ Có từ cảm 'Ơi', 'quá'\n→ Kết thúc bằng dấu chấm than (!)\n→ Câu kể dùng dấu chấm, câu hỏi dùng dấu ? ✔"},
                    {"q":"'Hãy giữ gìn sách vở.' là câu gì?", "opts":["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans":3, "explain":"📝 Câu cầu khiến: yêu cầu, đề nghị ai đó làm gì\n→ Có từ 'Hãy' đứng đầu câu\n→ Các từ cầu khiến: hãy, đừng, chớ, xin... ✔"},
                    {"q":"Từ nào chỉ màu sắc?", "opts":["chạy","đỏ","bàn","vui"], "ans":1, "explain":"📝 'Đỏ' là từ chỉ màu sắc\n→ 'chạy' = hành động, 'bàn' = đồ vật, 'vui' = cảm xúc\n→ Các màu sắc: đỏ, xanh, vàng, tím, cam, trắng, đen ✔"},
                    {"q":"Câu 'Bầu trời xanh trong.' tả điều gì?", "opts":["Con vật","Cảnh vật","Người","Đồ vật"], "ans":1, "explain":"📝 'Bầu trời' là cảnh vật thiên nhiên\n→ Câu này tả vẻ đẹp của bầu trời\n→ Cảnh vật: trời, mây, sông, núi, cây, hoa... ✔"},
                ],
            },
        ],
    },
}

# Danh sách lời khen ngợi
PRAISE = [
    "🎉 Tuyệt vời! Thông minh quá!", "⭐ Chính xác! Giỏi lắm!", "🌟 Đúng rồi! Cố lên nhé!",
    "🏆 Xuất sắc! Học rất giỏi!", "🎊 Đúng rồi! Tài năng thật!", "🥳 Chính xác! Thông minh quá!",
    "💫 Hoàn hảo! Làm tiếp nào!", "🚀 Siêu đỉnh! Bạn quá giỏi!",
]

MASCOTS = { "perfect": "👑", "great": "🌟", "good": "👍", "try": "💪" }

# ══════════════════════════════════════════════════════════════════════════════
# KHỞI TẠO SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
def init_state():
    defaults = {
        "screen":      "onboard",
        "username":    "",
        "subject":     None,
        "topic_idx":   None,
        "q_idx":       0,
        "score":       0,
        "answered":    False,
        "selected":    None,
        "shuffled_qs": [],
        "recent":      None,
        "total_pts":   0,
        "streak":      0,
        "best_streak": 0,
        "bonus_msg":   "",
        "badge_history": [],
        "result_saved": False
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ══════════════════════════════════════════════════════════════════════════════
# HÀM TIỆN ÍCH – LOGIC
# ══════════════════════════════════════════════════════════════════════════════
def go_home(): st.session_state.screen = "home"
def go_topics(subj): st.session_state.subject = subj; st.session_state.screen = "topics"
def go_quiz(topic_idx):
    qs = SUBJECTS[st.session_state.subject]["topics"][topic_idx]["qs"]
    shuffled = qs.copy()
    random.shuffle(shuffled)
    st.session_state.topic_idx   = topic_idx
    st.session_state.shuffled_qs = shuffled
    st.session_state.q_idx       = 0
    st.session_state.score       = 0
    st.session_state.answered    = False
    st.session_state.selected    = None
    st.session_state.streak      = 0
    st.session_state.best_streak = 0
    st.session_state.bonus_msg   = ""
    st.session_state.result_saved = False
    st.session_state.screen      = "quiz"

def answer(i):
    if st.session_state.answered: return
    st.session_state.selected = i
    st.session_state.answered = True
    q = st.session_state.shuffled_qs[st.session_state.q_idx]
    
    if i == q["ans"]:
        st.session_state.score     += 1
        st.session_state.total_pts += 10
        st.session_state.streak    += 1
        
        # Gamification: Streak Bonus
        if st.session_state.streak == 3:
            st.session_state.total_pts += 5
            st.session_state.bonus_msg = "🔥 Chuỗi 3: +5 điểm thưởng!"
        elif st.session_state.streak == 5:
            st.session_state.total_pts += 10
            st.session_state.bonus_msg = "🔥🔥 Chuỗi 5: +10 điểm thưởng!"
        elif st.session_state.streak > 5:
            st.session_state.bonus_msg = f"🔥 Chuỗi {st.session_state.streak}: Siêu cháy!"
        else:
            st.session_state.bonus_msg = ""
            
        if st.session_state.streak > st.session_state.best_streak:
            st.session_state.best_streak = st.session_state.streak
    else:
        st.session_state.streak = 0
        st.session_state.bonus_msg = ""

def next_q():
    st.session_state.q_idx   += 1
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.bonus_msg = ""
    total = len(st.session_state.shuffled_qs)
    if st.session_state.q_idx >= total:
        subj_label = SUBJECTS[st.session_state.subject]["label"]
        topic_name = SUBJECTS[st.session_state.subject]["topics"][st.session_state.topic_idx]["name"]
        st.session_state.recent = {
            "name":  topic_name,
            "subj":  subj_label,
            "badge": SUBJECTS[st.session_state.subject]["badge"],
            "score": st.session_state.score,
            "total": total,
        }
        st.session_state.screen = "result"

def get_level(pts): return max(1, pts // 50 + 1)

def render_sound(snd_type):
    if snd_type == "correct":
        js = """<script>(function(){var ctx = new (window.AudioContext || window.webkitAudioContext)();var o = ctx.createOscillator();var g = ctx.createGain();o.connect(g); g.connect(ctx.destination);o.type = 'sine'; o.frequency.value = 880;g.gain.setValueAtTime(0.3, ctx.currentTime);g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);o.start(ctx.currentTime); o.stop(ctx.currentTime + 0.5);})();</script>"""
    elif snd_type == "wrong":
        js = """<script>(function(){var ctx = new (window.AudioContext || window.webkitAudioContext)();var o = ctx.createOscillator();var g = ctx.createGain();o.connect(g); g.connect(ctx.destination);o.type = 'sawtooth'; o.frequency.value = 200;g.gain.setValueAtTime(0.2, ctx.currentTime);g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.4);o.start(ctx.currentTime); o.stop(ctx.currentTime + 0.4);})();</script>"""
    elif snd_type == "win":
        js = """<script>(function(){var ctx = new (window.AudioContext || window.webkitAudioContext)();var o1 = ctx.createOscillator();var g1 = ctx.createGain();o1.connect(g1);g1.connect(ctx.destination);o1.type='sine';o1.frequency.setValueAtTime(523.25, ctx.currentTime);o1.frequency.setValueAtTime(659.25, ctx.currentTime + 0.15);o1.frequency.setValueAtTime(783.99, ctx.currentTime + 0.3);o1.frequency.setValueAtTime(1046.50, ctx.currentTime + 0.45);g1.gain.setValueAtTime(0.3, ctx.currentTime);g1.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.5);o1.start(ctx.currentTime);o1.stop(ctx.currentTime + 1.5);})();</script>"""
    st.markdown(js, unsafe_allow_html=True)

def render_hud():
    name = st.session_state.username or "Bạn"
    pts = st.session_state.total_pts
    lv = get_level(pts)
    streak = st.session_state.streak
    streak_s = f"🔥×{streak}" if streak >= 3 else "—"
    st.markdown(f"""
    <div class="hud-bar">
        <div class="hud-item"><div class="hud-val">⭐ {pts}</div><div class="hud-lbl">Điểm</div></div>
        <div class="hud-sep"></div>
        <div class="hud-item"><div class="hud-val">Lv.{lv}</div><div class="hud-lbl">Cấp độ</div></div>
        <div class="hud-sep"></div>
        <div class="hud-item"><div class="hud-val">{streak_s}</div><div class="hud-lbl">Chuỗi</div></div>
        <div class="hud-sep"></div>
        <div class="hud-name">👋 {name}</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MÀN 0 — ONBOARDING
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == "onboard":
    st.markdown("""
    <div class="onboard-wrap">
        <span class="onboard-mascot">🦁</span>
        <div class="onboard-title">Trạm Học Tập<br>Siêu Sao!</div>
        <div class="onboard-sub">Vừa học vừa chơi – Nhận ngay huy hiệu ✨</div>
    </div>
    """, unsafe_allow_html=True)

    name_input = st.text_input("🎮 Nhập tên người hùng của bạn:", placeholder="Ví dụ: Nam Ngầu, An Siêu Sao...", max_chars=20)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Bắt đầu phiêu lưu!", key="btn_start", type="primary", use_container_width=True):
        name = name_input.strip()
        if not name:
            st.warning("⚠️ Nhập tên để bắt đầu nhé bạn ơi! 😊")
        else:
            st.session_state.username = name
            st.session_state.screen = "home"
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# MÀN 1 — TRANG CHỦ
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "home":
    render_hud()
    st.markdown(f"""<div class="greeting-box"><p class="greeting-text">Sẵn sàng chinh phục thử thách chưa, {st.session_state.username}? 🚀</p></div>""", unsafe_allow_html=True)
    st.markdown('<div class="home-title">🌟 Chọn Nhiệm Vụ</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="subject-card-math"><span class="subject-icon">🔢</span><div class="subject-name">Toán Học</div><div class="subject-count">5 chủ đề</div><span class="badge badge-math">Luyện Trí Não</span></div>""", unsafe_allow_html=True)
        if st.button("➕ Vào Học Toán", key="btn_math", type="primary", use_container_width=True):
            go_topics("math"); st.rerun()
    with col2:
        st.markdown("""<div class="subject-card-viet"><span class="subject-icon">📖</span><div class="subject-name">Tiếng Việt</div><div class="subject-count">5 chủ đề</div><span class="badge badge-viet">Luyện Ngôn Từ</span></div>""", unsafe_allow_html=True)
        if st.button("✏️ Vào Tiếng Việt", key="btn_viet", type="primary", use_container_width=True):
            go_topics("viet"); st.rerun()

    # Bảng điều khiển thu nhỏ
    st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)
    
    # Kết quả gần đây
    if st.session_state.recent:
        r = st.session_state.recent
        sc_col = "#16a34a" if r["score"] >= 7 else "#f59e0b" if r["score"] >= 5 else "#ef4444"
        st.markdown(f"""
        <div class="recent-box">
            <p class="box-title">🕐 Gần đây</p>
            <div style="font-weight:800;font-size:15px;color:#1a1a2e;">{r['name']}</div>
            <div style="margin-top:8px;display:flex;justify-content:space-between;align-items:center;">
                <span class="badge {r['badge']}" style="margin:0;">{r['subj']}</span>
                <span style="color:{sc_col};font-weight:900;font-size:18px;">{r['score']}/{r['total']} ✅</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tủ huy hiệu
    history = st.session_state.badge_history[-3:] # Show top 3 recent
    badges_html = " ".join([b["icon"] for b in history]) if history else "Chưa có huy hiệu nào. Hãy hoàn thành bài tập!"
    st.markdown(f"""
        <div class="badge-box">
            <p class="box-title">🏆 Tủ Huy Hiệu</p>
            <div style="font-size:28px;letter-spacing:4px;text-align:center;">{badges_html}</div>
        </div>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MÀN 2 — CHỌN CHỦ ĐỀ
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "topics":
    render_hud()
    sub = SUBJECTS[st.session_state.subject]
    
    col_back, _ = st.columns([1, 2])
    with col_back:
        if st.button("⬅️ Quay lại", key="back_home", type="secondary"):
            go_home(); st.rerun()

    st.markdown(f"<p style='font-size:16px;font-weight:900;color:#7c3aed;text-transform:uppercase;letter-spacing:.06em;margin:10px 0 16px;text-align:center;'>{sub['icon']} BẢN ĐỒ {sub['label'].upper()} {sub['icon']}</p>", unsafe_allow_html=True)

    for i, topic in enumerate(sub["topics"]):
        c1, c2 = st.columns([5, 2])
        with c1: st.markdown(f"<div class='topic-item'>🎯 {topic['name']}</div>", unsafe_allow_html=True)
        with c2:
            if st.button("🚀 GO!", key=f"topic_{i}", type="primary", use_container_width=True):
                go_quiz(i); st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# MÀN 3 — CÂU HỎI
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "quiz":
    render_hud()
    subj = st.session_state.subject
    sub = SUBJECTS[subj]
    qs = st.session_state.shuffled_qs
    q_idx = st.session_state.q_idx
    total = len(qs)
    q = qs[q_idx]

    c1, c2 = st.columns([2, 3])
    with c1:
        if st.button("🚪 Thoát", key="back_topics", type="secondary"): go_topics(subj); st.rerun()
    with c2:
        st.markdown(f"<div class='q-counter'>Tiến độ: {q_idx + 1} / {total}</div>", unsafe_allow_html=True)

    pct = int((q_idx / total) * 100)
    st.markdown(f"""<div class="progress-outer"><div class="progress-inner" style="width:{pct}%;"></div></div>""", unsafe_allow_html=True)

    # Streak banner
    if not st.session_state.answered and st.session_state.streak >= 3:
        fire = "🔥🔥🔥" if st.session_state.streak >= 5 else "🔥"
        st.markdown(f'<div class="streak-banner">{fire} Đang vào đà! Chuỗi {st.session_state.streak} câu đúng!</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="{sub["q_box_class"]}"><p class="q-text">{q["q"]}</p></div>', unsafe_allow_html=True)

    for i, opt in enumerate(q["opts"]):
        if not st.session_state.answered:
            st.button(opt, key=f"opt_{q_idx}_{i}", use_container_width=True, type="secondary", on_click=answer, args=(i,))
        else:
            if i == q["ans"]:
                st.markdown(f'<div class="opt-correct">{opt}</div>', unsafe_allow_html=True)
            elif i == st.session_state.selected:
                st.markdown(f'<div class="opt-wrong">{opt}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="opt-dim">{opt}</div>', unsafe_allow_html=True)

    if st.session_state.answered:
        if st.session_state.selected == q["ans"]:
            render_sound("correct")
            if "🔥" in st.session_state.bonus_msg: st.balloons()
            
            bonus_html = f'<div class="bonus-badge">{st.session_state.bonus_msg}</div>' if st.session_state.bonus_msg else ''
            st.markdown(f"""
            <div class="feedback-box feedback-correct">
                <div class="feedback-title txt-correct">🎉 Giỏi quá! +10 điểm ⭐</div>
                <div class="feedback-msg txt-correct">{random.choice(PRAISE)}</div>
                {bonus_html}
            </div>""", unsafe_allow_html=True)
        else:
            render_sound("wrong")
            st.markdown(f"""
            <div class="feedback-box feedback-wrong">
                <div class="feedback-title txt-wrong">😅 Oops! Thử lại ở câu sau nhé!</div>
                <div class="feedback-answer">💡 Đáp án đúng: {q["opts"][q["ans"]]}</div>
                <div class="explain-title">📚 Tại sao nhỉ?</div>
                <div class="feedback-explain">{q.get("explain", "")}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        btn_label = "Tiếp tục thôi ➡️" if q_idx < total - 1 else "🏁 Xem Thành Tích"
        st.button(btn_label, key="next_q", type="primary", use_container_width=True, on_click=next_q)

# ══════════════════════════════════════════════════════════════════════════════
# MÀN 4 — KẾT QUẢ
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "result":
    score = st.session_state.score
    total = len(st.session_state.shuffled_qs)
    name = st.session_state.username
    topic_name = SUBJECTS[st.session_state.subject]["topics"][st.session_state.topic_idx]["name"]
    subj_label = SUBJECTS[st.session_state.subject]["label"]
    
    is_superstar = (score == total) and (st.session_state.best_streak >= 5)

    if is_superstar:
        icon, badge_class, badge_text, badge_name = "🌟", "badge-superstar", "🌟 SIÊU SAO 🌟", "Siêu Sao"
        title = "Đỉnh Của Đỉnh!"
        msg = f"Không thể tin được {name}! Bạn đã trả lời đúng {total}/{total} và có chuỗi siêu dài!"
        mascot = MASCOTS["perfect"]
        if not st.session_state.result_saved: st.balloons()
    elif score >= 9:
        icon, badge_class, badge_text, badge_name = "🥇", "badge-gold", "🥇 HUY HIỆU VÀNG", "Vàng"
        title = "Quá Xuất Sắc!"
        msg = f"Tuyệt vời {name}! Bạn gần như hoàn hảo với {score}/{total} câu đúng!"
        mascot = MASCOTS["perfect"]
        if not st.session_state.result_saved: st.balloons()
    elif score >= 7:
        icon, badge_class, badge_text, badge_name = "🥈", "badge-silver", "🥈 HUY HIỆU BẠC", "Bạc"
        title = "Rất Tốt!"
        msg = f"Giỏi lắm {name}! Bạn đạt được {score}/{total} câu đúng."
        mascot = MASCOTS["great"]
    elif score >= 5:
        icon, badge_class, badge_text, badge_name = "🥉", "badge-bronze", "🥉 HUY HIỆU ĐỒNG", "Đồng"
        title = "Khá Lắm!"
        msg = f"Cố lên xíu nữa {name}! Bạn đã đúng {score}/{total} câu."
        mascot = MASCOTS["good"]
    else:
        icon, badge_class, badge_text, badge_name = "💪", "badge-try", "💪 CỐ GẮNG", "Cố Gắng"
        title = "Đừng Bỏ Cuộc!"
        msg = f"Sai một ly, đi học lại {name} nhé! {score}/{total} câu đúng."
        mascot = MASCOTS["try"]

    # Lưu kết quả & Google Sheets (Chỉ chạy 1 lần khi vào màn hình)
    if not st.session_state.result_saved:
        render_sound("win")
        st.session_state.badge_history.append({"badge": badge_name, "icon": icon, "topic": topic_name})
        record = {
            "name": name,
            "subject": subj_label,
            "topic": topic_name,
            "score": score,
            "total": total,
            "points": st.session_state.total_pts,
            "level": get_level(st.session_state.total_pts),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_to_google_sheet(record)
        st.session_state.result_saved = True

    st.markdown(f"""
    <div class="result-wrap">
        <span class="result-trophy">{mascot}</span>
        <div class="result-title">{title}</div>
        <div class="result-msg">{msg}</div>
        <div class="badge-earned {badge_class}">{badge_text}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="score-grid">
        <div class="score-box-correct"><div class="score-num" style="color:#16a34a;">{score}</div><div class="score-lbl" style="color:#166534;">Câu đúng ✅</div></div>
        <div class="score-box-wrong"><div class="score-num" style="color:#dc2626;">{total - score}</div><div class="score-lbl" style="color:#7f1d1d;">Câu sai ❌</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="total-pts-box">
        <span class="total-pts-icon">⭐</span>
        <div><div class="total-pts-val">{st.session_state.total_pts} Điểm</div><div class="total-pts-lbl">Tổng điểm hiện tại · Level {get_level(st.session_state.total_pts)}</div></div>
        <span class="total-pts-icon">🎮</span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔄 Chơi Lại", key="retry", type="secondary", use_container_width=True):
            go_quiz(st.session_state.topic_idx); st.rerun()
    with c2:
        if st.button("📚 Nhiệm Vụ Mới", key="other_topic", type="primary", use_container_width=True):
            go_topics(st.session_state.subject); st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Về Trang Chủ", key="home_result", type="secondary", use_container_width=True):
        go_home(); st.rerun()