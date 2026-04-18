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
# GOOGLE SHEETS INTEGRATION
# ══════════════════════════════════════════════════════════════════════════════
def save_to_google_sheet(data):
    """Lưu dữ liệu kết quả học tập vào Google Sheets"""
    try:
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
        pass

# ══════════════════════════════════════════════════════════════════════════════
# CSS TOÀN CỤC
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Baloo 2', cursive !important; }
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

/* Các style giữ nguyên bản nâng cấp trước */
.onboard-wrap { text-align: center; padding: 20px 0 10px; animation: fadeSlideUp 0.6s ease both; }
.onboard-mascot { font-size: 120px; line-height: 1; margin-bottom: 10px; display: block; animation: floatMascot 3s ease-in-out infinite; }
.onboard-title { font-family: 'Nunito', sans-serif; font-size: 40px; font-weight: 900; background: linear-gradient(135deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF); background-size: 300%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradShift 4s ease infinite; margin: 0 0 6px; line-height: 1.2; }
.onboard-sub { font-size: 18px; color: #7c3aed; font-weight: 700; margin: 0 0 28px; }

.hud-bar { display: flex; align-items: center; justify-content: space-between; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 20px; padding: 10px 18px; margin-bottom: 16px; box-shadow: 0 4px 18px rgba(26,26,46,0.25); gap: 8px; flex-wrap: wrap; border: 2px solid #FFD93D; }
.hud-item { display: flex; flex-direction: column; align-items: center; gap: 1px; min-width: 60px; }
.hud-val { font-size: 20px; font-weight: 800; color: #FFD93D; line-height: 1; }
.hud-lbl { font-size: 10px; font-weight: 700; color: #9ca3af; text-transform: uppercase; letter-spacing: .06em; }
.hud-sep { width: 2px; height: 32px; background: #ffffff33; flex-shrink: 0; }
.hud-name { font-size: 14px; font-weight: 800; color: #ffffff; background: linear-gradient(135deg, #FF6B6B, #FF9A3C); padding: 4px 12px; border-radius: 99px; white-space: nowrap; box-shadow: 0 2px 10px rgba(255,107,107,0.4); }

.home-title { text-align: center; font-family: 'Nunito', sans-serif; font-size: 42px; font-weight: 900; color: #1a1a2e; margin: 4px 0 4px; animation: bounce 2s infinite; }
.greeting-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 18px; padding: 14px 20px; margin-bottom: 18px; text-align: center; box-shadow: 0 6px 20px rgba(102,126,234,0.35); position: relative; overflow: hidden; }
.greeting-box::after { content: '✨'; position: absolute; right: 10px; top: 10px; opacity: 0.5; animation: sparkle 2s infinite; }
.greeting-text { font-size: 22px; font-weight: 800; color: #fff; margin: 0; }

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

.dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 10px; }
.recent-box, .badge-box { background: #ffffff; border: 2.5px solid #e9d5ff; border-radius: 20px; padding: 14px 18px; box-shadow: 0 3px 12px rgba(124,58,237,0.1); }
.box-title { font-size: 14px; font-weight: 900; color: #7c3aed; text-transform: uppercase; letter-spacing: .06em; margin: 0 0 12px; display: flex; align-items: center; gap: 6px; }

.topic-item { background: #fff; border: 3px solid #e9d5ff; border-radius: 18px; padding: 16px 20px; font-size: 18px; font-weight: 800; color: #1a1a2e; margin-bottom: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: all 0.2s; display: flex; align-items: center; }
.topic-item:hover { border-color: #a855f7; transform: translateX(5px); }

.progress-outer { background: #e9d5ff; border-radius: 99px; height: 22px; margin-bottom: 16px; overflow: hidden; border: 3px solid #c4b5fd; position: relative; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1); }
.progress-inner { height: 100%; background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD93D, #6BCB77, #4D96FF, #a855f7); background-size: 400% 100%; border-radius: 99px; animation: shimmer 3s linear infinite; transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); position: relative; }
.progress-inner::after { content: '⭐'; position: absolute; right: -10px; top: -5px; font-size: 24px; animation: sparkle 0.8s ease infinite alternate; filter: drop-shadow(0 2px 2px rgba(0,0,0,0.2)); }
.q-counter { font-size: 16px; font-weight: 900; color: #7c3aed; text-align: right; margin-bottom: 6px; }

.q-box { border-radius: 26px; padding: 35px 24px; text-align: center; margin-bottom: 24px; position: relative; overflow: hidden; animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.q-box-math { background: linear-gradient(135deg, #FF9A3C 0%, #FF6B6B 50%, #c2410c 100%); box-shadow: 0 8px 28px rgba(255,107,107,0.4); border: 4px solid #ffedd5; }
.q-box-viet { background: linear-gradient(135deg, #22c55e 0%, #16a34a 50%, #166534 100%); box-shadow: 0 8px 28px rgba(34,197,94,0.4); border: 4px solid #dcfce7; }
.q-box::before { content: '✨'; position: absolute; top: 12px; right: 18px; font-size: 32px; animation: sparkle 1s ease infinite alternate; }
.q-text { font-size: 28px; font-weight: 900; color: #fff; margin: 0; line-height: 1.4; text-shadow: 0 3px 8px rgba(0,0,0,0.3); }

.opt-btn { background: #fff; border: 3px solid #e5e7eb; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 800; color: #374151; width: 100%; text-align: left; margin-bottom: 12px; display: block; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: all 0.2s; }
.opt-correct { background: linear-gradient(135deg, #DCFCE7, #BBF7D0); border: 4px solid #22c55e; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 900; color: #14532d; width: 100%; text-align: left; margin-bottom: 12px; display: block; box-shadow: 0 6px 16px rgba(34,197,94,0.3); animation: correctPulse 0.5s ease; position: relative; }
.opt-correct::after { content: '✅'; position: absolute; right: 20px; font-size: 24px; }
.opt-wrong { background: linear-gradient(135deg, #FEE2E2, #fca5a5); border: 4px solid #ef4444; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 900; color: #7f1d1d; width: 100%; text-align: left; margin-bottom: 12px; display: block; animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both; position: relative; }
.opt-wrong::after { content: '❌'; position: absolute; right: 20px; font-size: 24px; }
.opt-dim { background: #f3f4f6; border: 3px solid #e5e7eb; border-radius: 20px; padding: 18px 20px; font-size: 20px; font-weight: 700; color: #9ca3af; width: 100%; text-align: left; margin-bottom: 12px; display: block; opacity: 0.6; }

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

.streak-banner { background: linear-gradient(135deg, #ff007f, #ff8c00); border-radius: 20px; padding: 12px 20px; text-align: center; font-size: 20px; font-weight: 900; color: #fff; margin-bottom: 16px; animation: slideDown 0.4s cubic-bezier(0.34,1.56,0.64,1); box-shadow: 0 6px 20px rgba(255,140,0,0.4); border: 3px solid #ffd700; }

.result-wrap { text-align: center; padding: 10px 0 20px; animation: popIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.result-trophy { font-size: 100px; margin-bottom: 10px; display: block; animation: floatMascot 2.5s infinite ease-in-out; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.2)); }
.result-title { font-family: 'Nunito', sans-serif; font-size: 42px; font-weight: 900; color: #1a1a2e; margin: 0 0 10px; }
.result-msg { font-size: 18px; color: #4b5563; font-weight: 700; margin: 0 0 24px; padding: 0 20px; }

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

.total-pts-box { background: linear-gradient(135deg, #1a1a2e, #16213e); border-radius: 24px; padding: 20px; margin-bottom: 24px; display: flex; align-items: center; justify-content: center; gap: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.3); border: 3px solid #FFD93D; animation: popIn 1s; }
.total-pts-icon { font-size: 40px; animation: wobble 2s infinite; }
.total-pts-val { font-size: 32px; font-weight: 900; color: #FFD93D; line-height: 1.1; }
.total-pts-lbl { font-size: 14px; font-weight: 800; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.05em; }

div.stButton > button { font-family: 'Baloo 2', cursive !important; font-weight: 900 !important; font-size: 18px !important; height: 60px !important; border-radius: 20px !important; transition: transform 0.2s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s !important; letter-spacing: .02em !important; }
div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #FF6B6B, #FF9A3C) !important; border: none !important; color: #fff !important; box-shadow: 0 8px 20px rgba(255,107,107,0.4) !important; }
div.stButton > button[kind="primary"]:hover { transform: translateY(-4px) scale(1.02) !important; box-shadow: 0 12px 28px rgba(255,107,107,0.5) !important; }
div.stButton > button[kind="primary"]:active { transform: scale(0.95) !important; }
div.stButton > button[kind="secondary"] { background: #fff !important; border: 3px solid #e9d5ff !important; color: #7c3aed !important; box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important; }
div.stButton > button[kind="secondary"]:hover { border-color: #a855f7 !important; background: #faf5ff !important; transform: translateY(-3px) !important; box-shadow: 0 8px 16px rgba(168,85,247,0.2) !important; }

div[data-testid="stTextInput"] input { font-family: 'Baloo 2', cursive !important; font-size: 20px !important; font-weight: 800 !important; border-radius: 20px !important; border: 3px solid #e9d5ff !important; padding: 14px 20px !important; background: #fff !important; color: #1a1a2e !important; text-align: center; box-shadow: inset 0 2px 6px rgba(0,0,0,0.05); }
div[data-testid="stTextInput"] input:focus { border-color: #a855f7 !important; box-shadow: 0 0 0 4px rgba(168,85,247,0.2) !important; }

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

audio { display: none; }
.divider { border:none; border-top: 3px dashed #e9d5ff; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# DỮ LIỆU TĨNH (Tiếng Việt & Hình học được mở rộng để lấy ngẫu nhiên)
# ══════════════════════════════════════════════════════════════════════════════
SUBJECTS = {
    "math": {
        "label": "Toán", "icon": "🔢", "badge": "badge-math", "q_box_class": "q-box-math",
        "topics": [
            {"name": "Phép cộng có nhớ", "qs": []}, # Sẽ tạo tự động 100%
            {"name": "Phép trừ có nhớ", "qs": []},  # Sẽ tạo tự động 100%
            {"name": "So sánh số", "qs": []},       # Sẽ tạo tự động 100%
            {"name": "Đo lường", "qs": []},         # Sẽ tạo tự động 100%
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
                    {"q":"Hình khối rubik có dạng hình gì?", "opts":["Hình hộp chữ nhật", "Khối cầu", "Khối lập phương", "Khối trụ"], "ans":2, "explain":"📝 Khối rubik có các mặt đều là hình vuông, nên nó là khối lập phương ✔"},
                    {"q":"Quả bóng có dạng hình gì?", "opts":["Khối cầu", "Hình tròn", "Khối trụ", "Khối lập phương"], "ans":0, "explain":"📝 Quả bóng là vật thể 3 chiều lăn được mọi hướng, nên gọi là khối cầu (không gọi là hình tròn) ✔"},
                    {"q":"Lon nước ngọt có dạng khối gì?", "opts":["Khối lập phương", "Khối cầu", "Khối hộp", "Khối trụ"], "ans":3, "explain":"📝 Lon nước có 2 mặt đáy tròn và thân đứng, là khối trụ ✔"}
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
                    {"q":"Chọn từ viết đúng chính tả:", "opts":["giòng sông","dòng sông","giòng xông","dòng xông"], "ans":1, "explain":"📝 Mẹo nhớ: 'dòng sông' viết với 'd' ✔"},
                    {"q":"Từ nào viết đúng?", "opts":["xanh lá cây","sanh lá cây","xanh lá kay","xang lá cây"], "ans":0, "explain":"📝 Mẹo nhớ: 'xanh' viết với 'x' ✔"},
                    {"q":"Điền vào chỗ trống: con ...ó (c/g)", "opts":["co","gó","có","gò"], "ans":2, "explain":"📝 'Con có' viết với 'c' ✔"},
                    {"q":"Chọn từ đúng: trời mưa hay giời mưa?", "opts":["giời mưa","trời mưa","trởi mưa","chời mưa"], "ans":1, "explain":"📝 'Trời' viết với 'tr' ✔"},
                    {"q":"Từ nào viết sai?", "opts":["quả cam","quả xoài","quả dưa","quả khôm"], "ans":3, "explain":"📝 'Quả khôm' viết sai, đúng là 'quả khóm' ✔"},
                    {"q":"Điền vào: bầu ....i (tr/ch)", "opts":["chời","trời","cời","gời"], "ans":1, "explain":"📝 'Bầu trời' viết với 'tr' ✔"},
                    {"q":"Chọn từ đúng:", "opts":["con trâu","con châu","con trau","con chau"], "ans":0, "explain":"📝 'Con trâu' viết với 'tr' ✔"},
                    {"q":"Từ nào viết đúng?", "opts":["buổi sáng","buổi xáng","buỗi sáng","buổi sạng"],"ans":0, "explain":"📝 'Buổi sáng' viết đúng dấu hỏi và sắc ✔"},
                    {"q":"Điền vào: hoa ...ồng (h/r)", "opts":["rồng","hồng","lồng","đồng"], "ans":1, "explain":"📝 'Hoa hồng' viết với 'h' ✔"},
                    {"q":"Chọn từ đúng:", "opts":["lá cây","lá kây","la cây","lá cay"], "ans":0, "explain":"📝 'Lá cây' viết đúng dấu ✔"},
                    {"q":"Từ nào viết ĐÚNG?", "opts":["sắp xếp", "xắp xếp", "sắp sếp", "xắp sếp"], "ans":0, "explain":"📝 'Sắp xếp' viết đúng (sắp - s, xếp - x) ✔"},
                    {"q":"Điền: ...inh viên (s/x)", "opts":["X", "S", "Ch", "Tr"], "ans":1, "explain":"📝 'Sinh viên' dùng chữ 'S' ✔"},
                    {"q":"Chọn từ viết đúng:", "opts":["chung thực", "trung thực", "chun thục", "trung thục"], "ans":1, "explain":"📝 'Trung thực' dùng 'Tr' ✔"}
                ],
            },
            {
                "name": "Từ loại – danh từ",
                "qs": [
                    {"q":"Từ nào là danh từ?", "opts":["chạy","đẹp","bàn","nhanh"], "ans":2, "explain":"📝 'bàn' = đồ vật → là danh từ ✔"},
                    {"q":"Chọn danh từ:", "opts":["học","ghế","vui","xanh"], "ans":1, "explain":"📝 'ghế' = đồ vật → là danh từ ✔"},
                    {"q":"Từ nào KHÔNG phải danh từ?", "opts":["sách","vở","đọc","bút"], "ans":2, "explain":"📝 'Đọc' là động từ (hành động) ✔"},
                    {"q":"Danh từ chỉ người:", "opts":["chạy","thầy giáo","đẹp","vàng"], "ans":1, "explain":"📝 'thầy giáo' chỉ người cụ thể ✔"},
                    {"q":"Chọn danh từ chỉ con vật:", "opts":["bay","to","con mèo","nhanh"], "ans":2, "explain":"📝 'con mèo' = tên con vật → là danh từ ✔"},
                    {"q":"Từ nào là danh từ?", "opts":["nhảy","hát","trường học","vui vẻ"], "ans":2, "explain":"📝 'Trường học' là nơi chốn = danh từ ✔"},
                    {"q":"Danh từ chỉ đồ vật:", "opts":["cái bàn","chạy","đẹp","xanh"], "ans":0, "explain":"📝 'Cái bàn' là đồ vật ✔"},
                    {"q":"Chọn danh từ:", "opts":["nhìn","ngủ","ăn","cây bút"], "ans":3, "explain":"📝 'Cây bút' là đồ vật = danh từ ✔"},
                    {"q":"Từ nào là danh từ?", "opts":["vui","buồn","hạnh phúc","ngôi nhà"], "ans":3, "explain":"📝 'Ngôi nhà' là nơi chốn = danh từ ✔"},
                    {"q":"Danh từ chỉ nơi chốn:", "opts":["đẹp","chơi","trường học","nhanh"], "ans":2, "explain":"📝 'trường học' là nơi chốn ✔"},
                    {"q":"Từ nào là danh từ chỉ hiện tượng tự nhiên?", "opts":["mưa", "hát", "buồn", "đỏ"], "ans":0, "explain":"📝 'Mưa' là hiện tượng thiên nhiên, là danh từ ✔"},
                    {"q":"Chọn danh từ chỉ đồ vật:", "opts":["bay", "nhảy", "quyển sách", "cao"], "ans":2, "explain":"📝 'Quyển sách' là đồ dùng học tập ✔"}
                ],
            },
            {
                "name": "Đặt câu – câu hỏi",
                "qs": [
                    {"q":"Câu hỏi thường dùng từ nào?", "opts":["vì","và","Ai? Cái gì?","nhưng"], "ans":2, "explain":"📝 Câu hỏi dùng: Ai? Cái gì? Ở đâu? ✔"},
                    {"q":"Câu 'Con đang làm gì?' hỏi về điều gì?", "opts":["Người","Thời gian","Hành động","Nơi chốn"], "ans":2, "explain":"📝 'Làm gì?' → hỏi về hành động ✔"},
                    {"q":"Chọn câu hỏi đúng:", "opts":["Bạn ăn gì không?","Bạn ăn gì?","Bạn ăn gì nhỉ không?","Bạn ăn gì à không?"],"ans":1, "explain":"📝 Câu hỏi chuẩn: 'Bạn ăn gì?' ✔"},
                    {"q":"Từ hỏi 'Ở đâu?' hỏi về điều gì?", "opts":["Người","Nơi chốn","Thời gian","Số lượng"], "ans":1, "explain":"📝 'Ở đâu?' hỏi về nơi chốn ✔"},
                    {"q":"'Ai đang học bài?' — Từ hỏi là?", "opts":["đang","học","Ai","bài"], "ans":2, "explain":"📝 'Ai?' là từ hỏi về người ✔"},
                    {"q":"Từ hỏi 'Khi nào?' hỏi về điều gì?", "opts":["Người","Nơi chốn","Thời gian","Cách thức"], "ans":2, "explain":"📝 'Khi nào?' hỏi về thời gian ✔"},
                    {"q":"Câu hỏi kết thúc bằng dấu gì?", "opts":["Dấu chấm","Dấu phẩy","Dấu chấm hỏi","Dấu chấm than"], "ans":2, "explain":"📝 Câu hỏi luôn kết thúc bằng dấu chấm hỏi (?) ✔"},
                    {"q":"Chọn câu hỏi:", "opts":["Trời mưa to.","Trời có mưa không?","Trời mưa rất to!","Trời mưa, lạnh quá."],"ans":1, "explain":"📝 'Trời có mưa không?' là câu hỏi ✔"},
                    {"q":"'Tại sao bạn khóc?' hỏi về điều gì?", "opts":["Người","Nơi chốn","Thời gian","Lý do"], "ans":3, "explain":"📝 'Tại sao?' hỏi về lý do ✔"},
                    {"q":"Từ hỏi 'Như thế nào?' hỏi về điều gì?", "opts":["Người","Cách thức","Thời gian","Số lượng"], "ans":1, "explain":"📝 'Như thế nào?' hỏi về cách thức, tính chất ✔"},
                    {"q":"Câu 'Bao giờ lớp mình đi dã ngoại?' hỏi về?", "opts":["Thời gian", "Nơi chốn", "Con người", "Lý do"], "ans":0, "explain":"📝 'Bao giờ' tương đương 'Khi nào', hỏi thời gian ✔"}
                ],
            },
            {
                "name": "Từ đồng nghĩa – trái nghĩa",
                "qs": [
                    {"q":"Từ trái nghĩa với 'to' là?", "opts":["lớn","bé","cao","nặng"], "ans":1, "explain":"📝 to ↔ bé (nhỏ) ✔"},
                    {"q":"Từ đồng nghĩa với 'vui' là?", "opts":["buồn","tức","vui vẻ","khóc"], "ans":2, "explain":"📝 'vui' và 'vui vẻ' cùng nghĩa ✔"},
                    {"q":"Từ trái nghĩa với 'ngày' là?", "opts":["sáng","chiều","đêm","tối"], "ans":2, "explain":"📝 Ngày ↔ Đêm ✔"},
                    {"q":"Từ đồng nghĩa với 'nhanh' là?", "opts":["chậm","mau","lâu","trễ"], "ans":1, "explain":"📝 'nhanh' và 'mau' đều chỉ tốc độ cao ✔"},
                    {"q":"Từ trái nghĩa với 'đen' là?", "opts":["xanh","vàng","trắng","đỏ"], "ans":2, "explain":"📝 Đen ↔ Trắng ✔"},
                    {"q":"Từ đồng nghĩa với 'đẹp' là?", "opts":["xấu","xinh","to","nhỏ"], "ans":1, "explain":"📝 'đẹp' và 'xinh' cùng nghĩa ✔"},
                    {"q":"Từ trái nghĩa với 'nóng' là?", "opts":["ấm","mát","lạnh","nguội"], "ans":2, "explain":"📝 Nóng ↔ Lạnh ✔"},
                    {"q":"Từ đồng nghĩa với 'nhà' là?", "opts":["trường","chợ","ngôi nhà","phố"],"ans":2, "explain":"📝 'nhà' và 'ngôi nhà' cùng nghĩa ✔"},
                    {"q":"Từ trái nghĩa với 'cao' là?", "opts":["to","thấp","lớn","béo"], "ans":1, "explain":"📝 Cao ↔ Thấp ✔"},
                    {"q":"Từ đồng nghĩa với 'nhìn' là?", "opts":["nghe","ngửi","xem","sờ"], "ans":2, "explain":"📝 'nhìn' và 'xem' cùng dùng mắt ✔"},
                    {"q":"Từ trái nghĩa với 'chăm chỉ' là?", "opts":["thông minh", "lười biếng", "ngoan ngoãn", "học giỏi"], "ans":1, "explain":"📝 Chăm chỉ ↔ Lười biếng ✔"},
                    {"q":"Từ trái nghĩa với 'rộng' là?", "opts":["to", "hẹp", "dài", "ngắn"], "ans":1, "explain":"📝 Rộng ↔ Hẹp ✔"}
                ],
            },
            {
                "name": "Đọc hiểu – câu văn",
                "qs": [
                    {"q":"'Mặt trời mọc ở hướng nào?'", "opts":["Hướng Tây","Hướng Bắc","Hướng Đông","Hướng Nam"], "ans":2, "explain":"📝 Mặt trời mọc ở hướng Đông ✔"},
                    {"q":"Câu 'Con mèo đang ngủ.' nói về con vật nào?", "opts":["Con chó","Con mèo","Con gà","Con cá"], "ans":1, "explain":"📝 Chủ ngữ là con mèo ✔"},
                    {"q":"Câu văn nào tả về thời tiết?", "opts":["Em đi học.","Trời hôm nay nắng đẹp.","Con mèo đen.","Bạn Nam chạy nhanh."], "ans":1, "explain":"📝 'Trời nắng đẹp' tả thời tiết ✔"},
                    {"q":"'Mùa hè, trời ____.' — Điền từ phù hợp:", "opts":["lạnh giá","mưa phùn","nắng nóng","có tuyết"], "ans":2, "explain":"📝 Mùa hè → nắng nóng ✔"},
                    {"q":"Đoạn văn tả cảnh vườn thường có từ nào?", "opts":["xe cộ","hoa lá","sóng biển","núi cao"], "ans":1, "explain":"📝 Vườn thường có 'hoa lá' ✔"},
                    {"q":"'Em thích ăn quả gì?' — Đây là câu gì?", "opts":["Câu kể","Câu cảm","Câu hỏi","Câu cầu khiến"], "ans":2, "explain":"📝 Câu hỏi vì có từ 'gì?' và dấu ? ✔"},
                    {"q":"Câu 'Ơi, đẹp quá!' là câu gì?", "opts":["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans":2, "explain":"📝 Câu cảm thể hiện cảm xúc mạnh ✔"},
                    {"q":"'Hãy giữ gìn sách vở.' là câu gì?", "opts":["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans":3, "explain":"📝 Câu cầu khiến có từ 'Hãy' ✔"},
                    {"q":"Từ nào chỉ màu sắc?", "opts":["chạy","đỏ","bàn","vui"], "ans":1, "explain":"📝 'Đỏ' là từ chỉ màu sắc ✔"},
                    {"q":"Câu 'Bầu trời xanh trong.' tả điều gì?", "opts":["Con vật","Cảnh vật","Người","Đồ vật"], "ans":1, "explain":"📝 'Bầu trời' là cảnh vật thiên nhiên ✔"}
                ],
            },
        ],
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# HÀM TẠO CÂU HỎI ĐỘNG (Toán học - Vô hạn câu hỏi khác nhau)
# ══════════════════════════════════════════════════════════════════════════════
def generate_math_addition():
    qs = []
    while len(qs) < 10:
        a = random.randint(11, 89)
        b = random.randint(2, 99 - a)
        if (a % 10) + (b % 10) >= 10:  # Đảm bảo là phép cộng có nhớ
            ans = a + b
            opts = list(set([ans, ans + 10, ans - 10, ans + 1, ans - 1, ans + 2]))
            random.shuffle(opts)
            opts = opts[:4]
            if ans not in opts: opts[0] = ans
            random.shuffle(opts)
            qs.append({
                "q": f"{a} + {b} = ?",
                "opts": [str(x) for x in opts],
                "ans": opts.index(ans),
                "explain": f"📝 Lấy {a} + {10 - (a%10)} = {a + 10 - (a%10)} (tròn chục), còn thừa lại cộng tiếp. Kết quả là {ans} ✔"
            })
    return qs

def generate_math_subtraction():
    qs = []
    while len(qs) < 10:
        a = random.randint(21, 99)
        b = random.randint(2, a - 1)
        if (a % 10) < (b % 10):  # Đảm bảo là phép trừ có nhớ
            ans = a - b
            opts = list(set([ans, ans + 10, ans - 10, ans + 1, ans - 1, ans + 2]))
            opts = [x for x in opts if x > 0]
            random.shuffle(opts)
            opts = opts[:4]
            if ans not in opts: opts[0] = ans
            random.shuffle(opts)
            qs.append({
                "q": f"{a} - {b} = ?",
                "opts": [str(x) for x in opts],
                "ans": opts.index(ans),
                "explain": f"📝 Phép tính trừ có nhớ, mượn 1 chục: {a} - {b} = {ans} ✔"
            })
    return qs

def generate_math_compare():
    qs = []
    for _ in range(10):
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        if a > b: ans_str, exp = ">", f"{a} lớn hơn {b}"
        elif a < b: ans_str, exp = "<", f"{a} bé hơn {b}"
        else: ans_str, exp = "=", f"{a} bằng {b}"
        
        opts = [">", "<", "=", "Không rõ"]
        qs.append({
            "q": f"Điền dấu: {a} ___ {b}",
            "opts": opts,
            "ans": opts.index(ans_str),
            "explain": f"📝 {exp} ✔"
        })
    return qs

def generate_math_measure():
    qs = []
    units = [("m", "dm", 10), ("dm", "cm", 10), ("m", "cm", 100)]
    for _ in range(10):
        u1, u2, factor = random.choice(units)
        val = random.randint(1, 9)
        ans = val * factor
        opts = list(set([ans, ans * 10, ans // 10 if ans>=10 else ans+5, ans + 10, val]))
        opts = [x for x in opts if x > 0]
        random.shuffle(opts)
        opts = opts[:4]
        if ans not in opts: opts[0] = ans
        random.shuffle(opts)
        qs.append({
            "q": f"{val} {u1} = ? {u2}",
            "opts": [f"{x} {u2}" for x in opts],
            "ans": opts.index(ans),
            "explain": f"📝 Ghi nhớ: 1 {u1} = {factor} {u2}. Vậy {val} {u1} = {ans} {u2} ✔"
        })
    return qs

# Danh sách lời khen ngợi
PRAISE = ["🎉 Tuyệt vời!", "⭐ Giỏi lắm!", "🌟 Đúng rồi!", "🏆 Xuất sắc!", "🎊 Tài năng thật!", "🥳 Thông minh quá!", "💫 Hoàn hảo!", "🚀 Siêu đỉnh!"]
MASCOTS = { "perfect": "👑", "great": "🌟", "good": "👍", "try": "💪" }

# ══════════════════════════════════════════════════════════════════════════════
# KHỞI TẠO SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
def init_state():
    defaults = {
        "screen": "onboard", "username": "", "subject": None, "topic_idx": None,
        "q_idx": 0, "score": 0, "answered": False, "selected": None,
        "shuffled_qs": [], "recent": None, "total_pts": 0, "streak": 0,
        "best_streak": 0, "bonus_msg": "", "badge_history": [], "result_saved": False
    }
    for k, v in defaults.items():
        if k not in st.session_state: st.session_state[k] = v

init_state()

# ══════════════════════════════════════════════════════════════════════════════
# HÀM TIỆN ÍCH – LOGIC
# ══════════════════════════════════════════════════════════════════════════════
def go_home(): st.session_state.screen = "home"
def go_topics(subj): st.session_state.subject = subj; st.session_state.screen = "topics"

def go_quiz(topic_idx):
    subj = st.session_state.subject
    
    # Sinh bộ câu hỏi KHÁC NHAU mỗi lần chạy
    if subj == "math" and topic_idx == 0: qs = generate_math_addition()
    elif subj == "math" and topic_idx == 1: qs = generate_math_subtraction()
    elif subj == "math" and topic_idx == 2: qs = generate_math_compare()
    elif subj == "math" and topic_idx == 3: qs = generate_math_measure()
    else:
        # Lấy ngẫu nhiên 10 câu từ ngân hàng (Hình học & Tiếng Việt)
        pool = SUBJECTS[subj]["topics"][topic_idx]["qs"].copy()
        random.shuffle(pool)
        qs = pool[:10]
        
    st.session_state.topic_idx   = topic_idx
    st.session_state.shuffled_qs = qs
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
        if st.session_state.streak == 3:
            st.session_state.total_pts += 5; st.session_state.bonus_msg = "🔥 Chuỗi 3: +5 điểm thưởng!"
        elif st.session_state.streak == 5:
            st.session_state.total_pts += 10; st.session_state.bonus_msg = "🔥🔥 Chuỗi 5: +10 điểm thưởng!"
        elif st.session_state.streak > 5:
            st.session_state.bonus_msg = f"🔥 Chuỗi {st.session_state.streak}: Siêu cháy!"
        else: st.session_state.bonus_msg = ""
        if st.session_state.streak > st.session_state.best_streak: st.session_state.best_streak = st.session_state.streak
    else:
        st.session_state.streak = 0; st.session_state.bonus_msg = ""

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
            "name": topic_name, "subj": subj_label, "badge": SUBJECTS[st.session_state.subject]["badge"],
            "score": st.session_state.score, "total": total
        }
        st.session_state.screen = "result"

def get_level(pts): return max(1, pts // 50 + 1)

def render_sound(snd_type):
    if snd_type == "correct": js = """<script>(function(){var ctx = new (window.AudioContext || window.webkitAudioContext)();var o = ctx.createOscillator();var g = ctx.createGain();o.connect(g); g.connect(ctx.destination);o.type = 'sine'; o.frequency.value = 880;g.gain.setValueAtTime(0.3, ctx.currentTime);g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);o.start(ctx.currentTime); o.stop(ctx.currentTime + 0.5);})();</script>"""
    elif snd_type == "wrong": js = """<script>(function(){var ctx = new (window.AudioContext || window.webkitAudioContext)();var o = ctx.createOscillator();var g = ctx.createGain();o.connect(g); g.connect(ctx.destination);o.type = 'sawtooth'; o.frequency.value = 200;g.gain.setValueAtTime(0.2, ctx.currentTime);g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.4);o.start(ctx.currentTime); o.stop(ctx.currentTime + 0.4);})();</script>"""
    elif snd_type == "win": js = """<script>(function(){var ctx = new (window.AudioContext || window.webkitAudioContext)();var o1 = ctx.createOscillator();var g1 = ctx.createGain();o1.connect(g1);g1.connect(ctx.destination);o1.type='sine';o1.frequency.setValueAtTime(523.25, ctx.currentTime);o1.frequency.setValueAtTime(659.25, ctx.currentTime + 0.15);o1.frequency.setValueAtTime(783.99, ctx.currentTime + 0.3);o1.frequency.setValueAtTime(1046.50, ctx.currentTime + 0.45);g1.gain.setValueAtTime(0.3, ctx.currentTime);g1.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.5);o1.start(ctx.currentTime);o1.stop(ctx.currentTime + 1.5);})();</script>"""
    st.markdown(js, unsafe_allow_html=True)

def render_hud():
    name = st.session_state.username or "Bạn"
    pts = st.session_state.total_pts
    lv = get_level(pts)
    streak_s = f"🔥×{st.session_state.streak}" if st.session_state.streak >= 3 else "—"
    st.markdown(f"""
    <div class="hud-bar">
        <div class="hud-item"><div class="hud-val">⭐ {pts}</div><div class="hud-lbl">Điểm</div></div><div class="hud-sep"></div>
        <div class="hud-item"><div class="hud-val">Lv.{lv}</div><div class="hud-lbl">Cấp độ</div></div><div class="hud-sep"></div>
        <div class="hud-item"><div class="hud-val">{streak_s}</div><div class="hud-lbl">Chuỗi</div></div><div class="hud-sep"></div>
        <div class="hud-name">👋 {name}</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# GIAO DIỆN CÁC MÀN HÌNH
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == "onboard":
    st.markdown('<div class="onboard-wrap"><span class="onboard-mascot">🦁</span><div class="onboard-title">Trạm Học Tập<br>Siêu Sao!</div><div class="onboard-sub">Mỗi lần chơi là một bộ câu hỏi mới ✨</div></div>', unsafe_allow_html=True)
    name_input = st.text_input("🎮 Nhập tên người hùng của bạn:", placeholder="Ví dụ: Nam Ngầu, An Siêu Sao...", max_chars=20)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Bắt đầu phiêu lưu!", key="btn_start", type="primary", use_container_width=True):
        if not name_input.strip(): st.warning("⚠️ Nhập tên để bắt đầu nhé bạn ơi! 😊")
        else: st.session_state.username = name_input.strip(); st.session_state.screen = "home"; st.rerun()

elif st.session_state.screen == "home":
    render_hud()
    st.markdown(f"""<div class="greeting-box"><p class="greeting-text">Sẵn sàng chinh phục thử thách chưa, {st.session_state.username}? 🚀</p></div>""", unsafe_allow_html=True)
    st.markdown('<div class="home-title">🌟 Chọn Nhiệm Vụ</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="subject-card-math"><span class="subject-icon">🔢</span><div class="subject-name">Toán Học</div><div class="subject-count">5 chủ đề</div><span class="badge badge-math">Luyện Trí Não</span></div>""", unsafe_allow_html=True)
        if st.button("➕ Vào Học Toán", key="btn_math", type="primary", use_container_width=True): go_topics("math"); st.rerun()
    with col2:
        st.markdown("""<div class="subject-card-viet"><span class="subject-icon">📖</span><div class="subject-name">Tiếng Việt</div><div class="subject-count">5 chủ đề</div><span class="badge badge-viet">Luyện Ngôn Từ</span></div>""", unsafe_allow_html=True)
        if st.button("✏️ Vào Tiếng Việt", key="btn_viet", type="primary", use_container_width=True): go_topics("viet"); st.rerun()

    st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)
    if st.session_state.recent:
        r = st.session_state.recent
        sc_col = "#16a34a" if r["score"] >= 7 else "#f59e0b" if r["score"] >= 5 else "#ef4444"
        st.markdown(f"""<div class="recent-box"><p class="box-title">🕐 Gần đây</p><div style="font-weight:800;font-size:15px;color:#1a1a2e;">{r['name']}</div><div style="margin-top:8px;display:flex;justify-content:space-between;align-items:center;"><span class="badge {r['badge']}" style="margin:0;">{r['subj']}</span><span style="color:{sc_col};font-weight:900;font-size:18px;">{r['score']}/{r['total']} ✅</span></div></div>""", unsafe_allow_html=True)
    
    history = st.session_state.badge_history[-3:]
    badges_html = " ".join([b["icon"] for b in history]) if history else "Chưa có huy hiệu nào."
    st.markdown(f'<div class="badge-box"><p class="box-title">🏆 Tủ Huy Hiệu</p><div style="font-size:28px;letter-spacing:4px;text-align:center;">{badges_html}</div></div></div>', unsafe_allow_html=True)

elif st.session_state.screen == "topics":
    render_hud()
    sub = SUBJECTS[st.session_state.subject]
    
    col_back, _ = st.columns([1, 2])
    with col_back:
        if st.button("⬅️ Quay lại", key="back_home", type="secondary"): go_home(); st.rerun()

    st.markdown(f"<p style='font-size:16px;font-weight:900;color:#7c3aed;text-transform:uppercase;letter-spacing:.06em;margin:10px 0 16px;text-align:center;'>{sub['icon']} BẢN ĐỒ {sub['label'].upper()} {sub['icon']}</p>", unsafe_allow_html=True)

    for i, topic in enumerate(sub["topics"]):
        c1, c2 = st.columns([5, 2])
        with c1: st.markdown(f"<div class='topic-item'>🎯 {topic['name']}</div>", unsafe_allow_html=True)
        with c2:
            if st.button("🚀 GO!", key=f"topic_{i}", type="primary", use_container_width=True): go_quiz(i); st.rerun()

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
    with c2: st.markdown(f"<div class='q-counter'>Tiến độ: {q_idx + 1} / {total}</div>", unsafe_allow_html=True)

    pct = int((q_idx / total) * 100)
    st.markdown(f"""<div class="progress-outer"><div class="progress-inner" style="width:{pct}%;"></div></div>""", unsafe_allow_html=True)

    if not st.session_state.answered and st.session_state.streak >= 3:
        fire = "🔥🔥🔥" if st.session_state.streak >= 5 else "🔥"
        st.markdown(f'<div class="streak-banner">{fire} Đang vào đà! Chuỗi {st.session_state.streak} câu đúng!</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="{sub["q_box_class"]}"><p class="q-text">{q["q"]}</p></div>', unsafe_allow_html=True)

    for i, opt in enumerate(q["opts"]):
        if not st.session_state.answered:
            st.button(opt, key=f"opt_{q_idx}_{i}", use_container_width=True, type="secondary", on_click=answer, args=(i,))
        else:
            if i == q["ans"]: st.markdown(f'<div class="opt-correct">{opt}</div>', unsafe_allow_html=True)
            elif i == st.session_state.selected: st.markdown(f'<div class="opt-wrong">{opt}</div>', unsafe_allow_html=True)
            else: st.markdown(f'<div class="opt-dim">{opt}</div>', unsafe_allow_html=True)

    if st.session_state.answered:
        if st.session_state.selected == q["ans"]:
            render_sound("correct")
            if "🔥" in st.session_state.bonus_msg: st.balloons()
            bonus_html = f'<div class="bonus-badge">{st.session_state.bonus_msg}</div>' if st.session_state.bonus_msg else ''
            st.markdown(f"""<div class="feedback-box feedback-correct"><div class="feedback-title txt-correct">🎉 Giỏi quá! +10 điểm ⭐</div><div class="feedback-msg txt-correct">{random.choice(PRAISE)}</div>{bonus_html}</div>""", unsafe_allow_html=True)
        else:
            render_sound("wrong")
            st.markdown(f"""<div class="feedback-box feedback-wrong"><div class="feedback-title txt-wrong">😅 Oops! Thử lại ở câu sau nhé!</div><div class="feedback-answer">💡 Đáp án đúng: {q["opts"][q["ans"]]}</div><div class="explain-title">📚 Tại sao nhỉ?</div><div class="feedback-explain">{q.get("explain", "")}</div></div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        btn_label = "Tiếp tục thôi ➡️" if q_idx < total - 1 else "🏁 Xem Thành Tích"
        st.button(btn_label, key="next_q", type="primary", use_container_width=True, on_click=next_q)

elif st.session_state.screen == "result":
    score = st.session_state.score
    total = len(st.session_state.shuffled_qs)
    name = st.session_state.username
    topic_name = SUBJECTS[st.session_state.subject]["topics"][st.session_state.topic_idx]["name"]
    subj_label = SUBJECTS[st.session_state.subject]["label"]
    
    if score == total and st.session_state.best_streak >= 5:
        icon, badge_class, badge_text, badge_name, title, mascot = "🌟", "badge-superstar", "🌟 SIÊU SAO 🌟", "Siêu Sao", "Đỉnh Của Đỉnh!", MASCOTS["perfect"]
        msg = f"Không thể tin được {name}! Đúng {total}/{total} và chuỗi siêu dài!"
        if not st.session_state.result_saved: st.balloons()
    elif score >= 9:
        icon, badge_class, badge_text, badge_name, title, mascot = "🥇", "badge-gold", "🥇 HUY HIỆU VÀNG", "Vàng", "Quá Xuất Sắc!", MASCOTS["perfect"]
        msg = f"Tuyệt vời {name}! Bạn gần như hoàn hảo với {score}/{total} câu đúng!"
        if not st.session_state.result_saved: st.balloons()
    elif score >= 7:
        icon, badge_class, badge_text, badge_name, title, mascot = "🥈", "badge-silver", "🥈 HUY HIỆU BẠC", "Bạc", "Rất Tốt!", MASCOTS["great"]
        msg = f"Giỏi lắm {name}! Bạn đạt được {score}/{total} câu đúng."
    elif score >= 5:
        icon, badge_class, badge_text, badge_name, title, mascot = "🥉", "badge-bronze", "🥉 HUY HIỆU ĐỒNG", "Đồng", "Khá Lắm!", MASCOTS["good"]
        msg = f"Cố lên xíu nữa {name}! Bạn đã đúng {score}/{total} câu."
    else:
        icon, badge_class, badge_text, badge_name, title, mascot = "💪", "badge-try", "💪 CỐ GẮNG", "Cố Gắng", "Đừng Bỏ Cuộc!", MASCOTS["try"]
        msg = f"Sai một ly, đi học lại {name} nhé! {score}/{total} câu đúng."

    if not st.session_state.result_saved:
        render_sound("win")
        st.session_state.badge_history.append({"badge": badge_name, "icon": icon, "topic": topic_name})
        record = {"name": name, "subject": subj_label, "topic": topic_name, "score": score, "total": total, "points": st.session_state.total_pts, "level": get_level(st.session_state.total_pts), "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        save_to_google_sheet(record)
        st.session_state.result_saved = True

    st.markdown(f'<div class="result-wrap"><span class="result-trophy">{mascot}</span><div class="result-title">{title}</div><div class="result-msg">{msg}</div><div class="badge-earned {badge_class}">{badge_text}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="score-grid"><div class="score-box-correct"><div class="score-num" style="color:#16a34a;">{score}</div><div class="score-lbl" style="color:#166534;">Câu đúng ✅</div></div><div class="score-box-wrong"><div class="score-num" style="color:#dc2626;">{total - score}</div><div class="score-lbl" style="color:#7f1d1d;">Câu sai ❌</div></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="total-pts-box"><span class="total-pts-icon">⭐</span><div><div class="total-pts-val">{st.session_state.total_pts} Điểm</div><div class="total-pts-lbl">Tổng điểm hiện tại · Level {get_level(st.session_state.total_pts)}</div></div><span class="total-pts-icon">🎮</span></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔄 Chơi Lại Màn Này", key="retry", type="secondary", use_container_width=True): go_quiz(st.session_state.topic_idx); st.rerun()
    with c2:
        if st.button("📚 Nhiệm Vụ Mới", key="other_topic", type="primary", use_container_width=True): go_topics(st.session_state.subject); st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Về Trang Chủ", key="home_result", type="secondary", use_container_width=True): go_home(); st.rerun()