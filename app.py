import streamlit as st
import random

# ── 1. CẤU HÌNH TRANG ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Học Vui Cùng Bé",
    page_icon="🎈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── 2. CSS UI/UX CHO TRẺ EM (DUOLINGO/KHAN ACADEMY STYLE) ───────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Baloo 2', cursive !important;
}

/* Nền chấm bi pastel */
.stApp {
    background-color: #FAFAFA;
    background-image: radial-gradient(#FFD93D 1.5px, transparent 1.5px);
    background-size: 30px 30px;
}

/* Ẩn header */
header[data-testid="stHeader"] { display: none; }
.block-container { padding-top: 1.5rem !important; max-width: 680px !important; }

/* ── Hiệu ứng ── */
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}
.bouncy { animation: bounce 2s infinite ease-in-out; display: inline-block; }

@keyframes pulse-star {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.1); opacity: 0.8; }
    100% { transform: scale(1); opacity: 1; }
}
.star-blink { animation: pulse-star 1.5s infinite; display: inline-block; color: #FFD93D; }

/* ── Tiêu đề ── */
.home-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #4D96FF;
    margin: 0 0 10px;
    text-shadow: 2px 2px 0px #FFF, 4px 4px 0px rgba(77, 150, 255, 0.2);
}
.home-sub {
    text-align: center;
    font-size: 20px;
    color: #6BCB77;
    font-weight: 600;
    margin: 0 0 30px;
}

/* ── Card Môn Học ── */
.subject-card {
    background: #ffffff;
    border: 4px solid;
    border-radius: 24px;
    padding: 30px 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    box-shadow: 0 8px 0px rgba(0,0,0,0.05);
}
.subject-card:hover { transform: translateY(-5px); }
.subject-card:active { transform: translateY(2px); box-shadow: 0 3px 0px rgba(0,0,0,0.05); }

.card-math { border-color: #FFD93D; }
.card-viet { border-color: #6BCB77; }

.subject-icon { font-size: 64px; margin-bottom: 10px; }
.subject-name { font-size: 28px; font-weight: 800; margin: 0; }
.math-text { color: #FF9A3C; }
.viet-text { color: #1DB954; }

/* ── Thanh tiến trình cầu vồng ── */
.progress-track {
    height: 16px;
    background: #E0E0E0;
    border-radius: 99px;
    margin-bottom: 20px;
    overflow: hidden;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}
.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #FF6B6B, #FFD93D, #6BCB77, #4D96FF);
    border-radius: 99px;
    transition: width 0.5s bounciness;
}

/* ── Hộp câu hỏi ── */
.q-box {
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 6px 0px rgba(0,0,0,0.05);
    border: 4px solid #FFF;
}
.q-box-math { background-color: #FFF4CB; border-color: #FFD93D; }
.q-box-viet { background-color: #E2F6E5; border-color: #6BCB77; }
.q-text { font-size: 26px; font-weight: 800; color: #333; margin: 0; line-height: 1.5; }

/* ── Nút đáp án ── */
.opt-btn-custom {
    background: #ffffff;
    border: 3px solid #E0E0E0;
    border-radius: 20px;
    padding: 16px 20px;
    font-size: 22px;
    font-weight: 700;
    color: #444;
    width: 100%;
    text-align: center;
    cursor: pointer;
    margin-bottom: 12px;
    transition: all 0.2s;
    box-shadow: 0 4px 0px #E0E0E0;
}
.opt-btn-custom:hover { transform: scale(1.02); border-color: #4D96FF; box-shadow: 0 4px 0px #4D96FF; color: #4D96FF; }
.opt-btn-custom:active { transform: scale(0.98) translateY(4px); box-shadow: 0 0px 0px #4D96FF; }

.opt-correct { background: #6BCB77 !important; border-color: #4CAF50 !important; color: white !important; box-shadow: 0 4px 0px #4CAF50 !important; }
.opt-wrong   { background: #FF6B6B !important; border-color: #E53935 !important; color: white !important; box-shadow: 0 4px 0px #E53935 !important; opacity: 0.8; }

/* ── Feedback Đúng/Sai ── */
.fb-correct-box {
    background: #FFF4CB;
    border: 4px dashed #FFD93D;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    font-size: 24px;
    font-weight: 800;
    color: #FF9A3C;
    margin-top: 20px;
    animation: bounce 1s ease;
}

.fb-wrong-box {
    background: #FFEBEB;
    border: 4px dashed #FF9A3C;
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
}
.fb-w-msg { font-size: 20px; font-weight: 700; color: #FF6B6B; margin-bottom: 10px; text-align: center; }
.fb-w-correct { font-size: 24px; font-weight: 800; color: #1DB954; background: #E2F6E5; padding: 10px; border-radius: 12px; text-align: center; margin-bottom: 15px; border: 2px solid #6BCB77; }
.fb-w-explain { font-size: 18px; font-weight: 600; color: #555; background: #FFF; padding: 15px; border-radius: 12px; line-height: 1.5; border: 2px solid #EEE; }

/* ── Nút Streamlit mặc định ── */
div.stButton > button {
    border-radius: 20px !important;
    font-weight: 800 !important;
    font-size: 20px !important;
    height: 60px !important;
    transition: all 0.2s !important;
    border: 3px solid transparent !important;
}
div.stButton > button[kind="primary"] {
    background: #4D96FF !important;
    color: white !important;
    box-shadow: 0 6px 0px #2A75E6 !important;
}
div.stButton > button[kind="primary"]:hover { transform: scale(1.03); }
div.stButton > button[kind="primary"]:active { transform: scale(0.97) translateY(6px); box-shadow: 0 0px 0px #2A75E6 !important; }

/* ── Kết quả ── */
.res-icon { font-size: 80px; text-align: center; margin-bottom: 10px; animation: bounce 2s infinite; }
.res-title { font-size: 36px; font-weight: 800; color: #4D96FF; text-align: center; }
.res-msg { font-size: 20px; color: #666; text-align: center; font-weight: 600; margin-bottom: 30px; }
.score-big { font-size: 48px; font-weight: 900; color: #6BCB77; text-align: center; background: #FFF; border: 4px solid #6BCB77; border-radius: 50%; width: 120px; height: 120px; line-height: 110px; margin: 0 auto 30px; box-shadow: 0 8px 0px rgba(107,203,119,0.3); }
</style>
""", unsafe_allow_html=True)

# ── 3. DỮ LIỆU CÂU HỎI (ĐÃ THÊM PHẦN EXPLAIN) ────────────────────────────────
SUBJECTS = {
    "math": {
        "label": "Toán", "icon": "🧮", "color_class": "math",
        "topics": [
            {"name": "Phép cộng có nhớ", "qs": [
                {"q": "15 + 7 = ?", "opts": ["20","22","23","21"], "ans": 1, "explain": "Lấy 15 + 5 = 20 (cho tròn chục). Số 7 tách thành 5 và 2. Lấy 20 + 2 = 22."},
                {"q": "28 + 5 = ?", "opts": ["33","31","32","34"], "ans": 0, "explain": "Lấy 28 + 2 = 30. Số 5 tách thành 2 và 3. Lấy 30 + 3 = 33."},
                {"q": "36 + 8 = ?", "opts": ["44","42","43","45"], "ans": 0, "explain": "Lấy 36 + 4 = 40. Số 8 tách thành 4 và 4. Lấy 40 + 4 = 44."},
                {"q": "49 + 6 = ?", "opts": ["54","55","53","56"], "ans": 1, "explain": "Lấy 49 + 1 = 50. Số 6 tách thành 1 và 5. Lấy 50 + 5 = 55."},
                {"q": "17 + 9 = ?", "opts": ["25","27","26","24"], "ans": 2, "explain": "Lấy 17 + 3 = 20. Số 9 tách thành 3 và 6. Lấy 20 + 6 = 26."},
                {"q": "38 + 7 = ?", "opts": ["44","45","46","43"], "ans": 1, "explain": "Lấy 38 + 2 = 40. Số 7 tách thành 2 và 5. Lấy 40 + 5 = 45."},
                {"q": "56 + 8 = ?", "opts": ["63","65","64","62"], "ans": 2, "explain": "Lấy 56 + 4 = 60. Số 8 tách thành 4 và 4. Lấy 60 + 4 = 64."},
                {"q": "27 + 6 = ?", "opts": ["33","34","32","35"], "ans": 0, "explain": "Lấy 27 + 3 = 30. Số 6 tách thành 3 và 3. Lấy 30 + 3 = 33."},
                {"q": "45 + 9 = ?", "opts": ["53","55","54","52"], "ans": 2, "explain": "Lấy 45 + 5 = 50. Số 9 tách thành 5 và 4. Lấy 50 + 4 = 54."},
                {"q": "67 + 8 = ?", "opts": ["75","74","76","77"], "ans": 0, "explain": "Lấy 67 + 3 = 70. Số 8 tách thành 3 và 5. Lấy 70 + 5 = 75."},
            ]},
            {"name": "Phép trừ có nhớ", "qs": [
                {"q": "23 - 7 = ?", "opts": ["16","15","14","17"], "ans": 0, "explain": "Lấy 23 - 3 = 20. Số 7 tách thành 3 và 4. Lấy 20 - 4 = 16."},
                {"q": "41 - 6 = ?", "opts": ["34","36","35","33"], "ans": 2, "explain": "Lấy 41 - 1 = 40. Số 6 tách thành 1 và 5. Lấy 40 - 5 = 35."},
                {"q": "52 - 8 = ?", "opts": ["44","45","43","42"], "ans": 0, "explain": "Lấy 52 - 2 = 50. Số 8 tách thành 2 và 6. Lấy 50 - 6 = 44."},
                {"q": "30 - 4 = ?", "opts": ["26","28","25","27"], "ans": 0, "explain": "3 chục trừ đi 4 đơn vị thì còn 2 chục và 6 đơn vị (26)."},
                {"q": "61 - 9 = ?", "opts": ["51","53","52","54"], "ans": 2, "explain": "Lấy 61 - 1 = 60. Số 9 tách thành 1 và 8. Lấy 60 - 8 = 52."},
                {"q": "74 - 7 = ?", "opts": ["67","65","66","68"], "ans": 0, "explain": "Lấy 74 - 4 = 70. Số 7 tách thành 4 và 3. Lấy 70 - 3 = 67."},
                {"q": "83 - 5 = ?", "opts": ["77","79","78","76"], "ans": 2, "explain": "Lấy 83 - 3 = 80. Số 5 tách thành 3 và 2. Lấy 80 - 2 = 78."},
                {"q": "46 - 8 = ?", "opts": ["38","37","39","36"], "ans": 0, "explain": "Lấy 46 - 6 = 40. Số 8 tách thành 6 và 2. Lấy 40 - 2 = 38."},
                {"q": "55 - 6 = ?", "opts": ["49","48","50","47"], "ans": 0, "explain": "Lấy 55 - 5 = 50. Số 6 tách thành 5 và 1. Lấy 50 - 1 = 49."},
                {"q": "91 - 3 = ?", "opts": ["89","87","88","86"], "ans": 2, "explain": "Lấy 91 - 1 = 90. Số 3 tách thành 1 và 2. Lấy 90 - 2 = 88."},
            ]},
            {"name": "So sánh số", "qs": [
                {"q": "Số nào lớn hơn: 45 hay 54?", "opts": ["45","54","Bằng nhau","Không biết"], "ans": 1, "explain": "Số 54 có chữ số hàng chục là 5, lớn hơn chữ số hàng chục của 45 (là 4)."},
                {"q": "Điền dấu: 73 __ 37", "opts": ["<",">","=","Không biết"], "ans": 1, "explain": "73 có hàng chục là 7, lớn hơn hàng chục của 37 (là 3). Vậy 73 > 37."},
                {"q": "Số liền sau của 99 là?", "opts": ["98","100","101","97"], "ans": 1, "explain": "Số liền sau thì cộng thêm 1. 99 + 1 = 100."},
                {"q": "Số liền trước của 50 là?", "opts": ["51","49","48","52"], "ans": 1, "explain": "Số liền trước thì bớt đi 1. 50 - 1 = 49."},
                {"q": "Điền dấu: 68 __ 86", "opts": [">","<","=","Không biết"], "ans": 1, "explain": "68 có hàng chục là 6, nhỏ hơn hàng chục của 86 (là 8). Vậy 68 < 86."},
                {"q": "Số nào nhỏ nhất: 25, 52, 22, 55?", "opts": ["25","52","22","55"], "ans": 2, "explain": "Số 22 và 25 có hàng chục nhỏ nhất (là 2). So sánh hàng đơn vị thì 2 < 5 nên 22 là số nhỏ nhất."},
                {"q": "Số nào lớn nhất: 31, 13, 33, 11?", "opts": ["31","13","33","11"], "ans": 2, "explain": "Số 31 và 33 có hàng chục lớn nhất (là 3). So sánh hàng đơn vị thì 3 > 1 nên 33 là số lớn nhất."},
                {"q": "Điền dấu: 40 __ 40", "opts": [">","<","=","Không biết"], "ans": 2, "explain": "Hai số giống hệt nhau thì bằng nhau. 40 = 40."},
                {"q": "Số liền sau của 79 là?", "opts": ["78","80","81","77"], "ans": 1, "explain": "Số liền sau thì đếm thêm 1. 79 rồi đến 80."},
                {"q": "Số liền trước của 100 là?", "opts": ["99","101","98","102"], "ans": 0, "explain": "Đếm ngược lại 1 bước từ 100 ta được 99."},
            ]},
            {"name": "Đo lường", "qs": [
                {"q": "1 dm = ? cm", "opts": ["5 cm","10 cm","100 cm","1 cm"], "ans": 1, "explain": "Ghi nhớ: 1 đề-xi-mét (dm) bằng 10 xăng-ti-mét (cm)."},
                {"q": "1 m = ? dm", "opts": ["100 dm","1 dm","10 dm","5 dm"], "ans": 2, "explain": "Ghi nhớ: 1 mét (m) bằng 10 đề-xi-mét (dm)."},
                {"q": "30 cm = ? dm", "opts": ["3 dm","30 dm","300 dm","13 dm"], "ans": 0, "explain": "Vì 10 cm = 1 dm, nên 30 cm = 3 dm (bỏ đi 1 số 0 ở cuối)."},
                {"q": "20 dm = ? m", "opts": ["20 m","200 m","2 m","0,2 m"], "ans": 2, "explain": "Vì 10 dm = 1 m, nên 20 dm = 2 m."},
                {"q": "1 m = ? cm", "opts": ["10 cm","1000 cm","100 cm","1 cm"], "ans": 2, "explain": "Ghi nhớ: 1 mét (m) bằng 100 xăng-ti-mét (cm). Bằng đúng độ dài sải tay của con đó!"},
                {"q": "5 dm = ? cm", "opts": ["5 cm","500 cm","50 cm","15 cm"], "ans": 2, "explain": "1 dm = 10 cm, nên 5 dm = 50 cm (thêm 1 số 0 vào sau)."},
                {"q": "2 m = ? dm", "opts": ["2 dm","200 dm","20 dm","12 dm"], "ans": 2, "explain": "1 m = 10 dm, nên 2 m = 20 dm."},
                {"q": "40 cm = ? dm", "opts": ["40 dm","400 dm","4 dm","14 dm"], "ans": 2, "explain": "10 cm = 1 dm, nên 40 cm = 4 dm."},
                {"q": "3 m = ? cm", "opts": ["3 cm","30 cm","300 cm","3000 cm"], "ans": 2, "explain": "1 m = 100 cm, nên 3 m = 300 cm."},
                {"q": "6 dm = ? cm", "opts": ["6 cm","600 cm","60 cm","16 cm"], "ans": 2, "explain": "1 dm = 10 cm, nên 6 dm = 60 cm."},
            ]},
            {"name": "Hình học", "qs": [
                {"q": "Hình chữ nhật có bao nhiêu góc vuông?", "opts": ["2","3","4","1"], "ans": 2, "explain": "Hình chữ nhật giống như cái bảng hay quyển vở, nó có đúng 4 góc vuông con nhé!"},
                {"q": "Hình vuông có bao nhiêu cạnh bằng nhau?", "opts": ["2","3","0","4"], "ans": 3, "explain": "Hình vuông có 4 cạnh và tất cả 4 cạnh đều dài bằng nhau."},
                {"q": "Hình tam giác có bao nhiêu cạnh?", "opts": ["4","2","3","5"], "ans": 2, "explain": "Chữ 'tam' nghĩa là 3. Hình tam giác luôn có 3 cạnh."},
                {"q": "Hình nào có tất cả các cạnh bằng nhau?", "opts": ["Hình chữ nhật","Hình tam giác","Hình vuông","Hình thang"], "ans": 2, "explain": "Đặc điểm nổi bật nhất của hình vuông là có 4 cạnh đều dài bằng nhau."},
                {"q": "Hình tròn có bao nhiêu góc?", "opts": ["1","2","3","0"], "ans": 3, "explain": "Hình tròn cong đều như bánh xe lăn, nó không có góc nào cả (0 góc)."},
                {"q": "Hình chữ nhật có bao nhiêu cạnh?", "opts": ["3","4","5","6"], "ans": 1, "explain": "Hình chữ nhật gồm 2 cạnh dài và 2 cạnh ngắn. Tổng cộng là 4 cạnh."},
                {"q": "Hình nào KHÔNG có góc vuông?", "opts": ["Hình vuông","Hình chữ nhật","Hình tròn","Tất cả"], "ans": 2, "explain": "Hình tròn cong tròn xoe, nên nó không có góc vuông nào cả."},
                {"q": "Hình tam giác có bao nhiêu góc?", "opts": ["2","4","3","1"], "ans": 2, "explain": "Có 3 cạnh thì sẽ tạo thành 3 góc con nhé!"},
                {"q": "Hình vuông có bao nhiêu cạnh?", "opts": ["3","5","6","4"], "ans": 3, "explain": "Hình vuông có 4 cạnh (bằng nhau)."},
                {"q": "Hình chữ nhật: cạnh dài gọi là?", "opts": ["Chiều rộng","Chiều cao","Chiều dài","Cạnh bên"], "ans": 2, "explain": "Cạnh dài hơn gọi là 'Chiều dài', cạnh ngắn hơn gọi là 'Chiều rộng'."},
            ]},
        ]
    },
    "viet": {
        "label": "Tiếng Việt", "icon": "📚", "color_class": "viet",
        "topics": [
            {"name": "Chính tả – âm vần", "qs": [
                {"q": "Chọn từ viết đúng chính tả:", "opts": ["giòng sông","dòng sông","giòng xông","dòng xông"], "ans": 1, "explain": "Phải viết là 'dòng sông' (âm d). Nước chảy thành dòng chứ không phải 'giòng'."},
                {"q": "Từ nào viết đúng?", "opts": ["xanh lá cây","sanh lá cây","xanh lá kay","xang lá cây"], "ans": 0, "explain": "Màu sắc phải viết là 'xanh' (âm x), không phải 'sanh'."},
                {"q": "Điền vào chỗ trống: con ...ó (c/g)", "opts": ["co","gó","có","gò"], "ans": 2, "explain": "Đó là 'con chó', con vật giữ nhà quen thuộc của chúng ta."},
                {"q": "Chọn từ đúng: trời mưa hay giời mưa?", "opts": ["giời mưa","trời mưa","trởi mưa","chời mưa"], "ans": 1, "explain": "Ông 'trời' viết bằng âm 'tr'. Mặc dù khi nói mình hay gọi 'giời ơi' nhưng viết chuẩn phải là 'trời'."},
                {"q": "Từ nào viết sai?", "opts": ["quả cam","quả xoài","quả dưa","quả khôm"], "ans": 3, "explain": "Phải viết là 'quả khóm' (hoặc quả dứa), không có từ nào là 'quả khôm' cả."},
                {"q": "Điền vào: bầu ....i (tr/ch)", "opts": ["chời","trời","cời","gời"], "ans": 1, "explain": "Bầu 'trời' rộng lớn bao la, từ 'trời' luôn đi với âm 'tr'."},
                {"q": "Chọn từ đúng:", "opts": ["con trâu","con châu","con trau","con chau"], "ans": 0, "explain": "Con vật đi cày ruộng là 'con trâu' (âm tr). Chữ 'châu' chỉ dùng cho 'châu báu' thôi."},
                {"q": "Từ nào viết đúng?", "opts": ["buổi sáng","buổi xáng","buỗi sáng","buổi sạng"], "ans": 0, "explain": "Thời gian buổi sáng sớm viết bằng âm 's' (sáng)."},
                {"q": "Điền vào: hoa ...ồng (h/r)", "opts": ["rồng","hồng","lồng","đồng"], "ans": 1, "explain": "Đó là bông 'hoa hồng', loài hoa có màu đỏ và có gai."},
                {"q": "Chọn từ đúng:", "opts": ["lá cây","lá kây","la cây","lá cay"], "ans": 0, "explain": "Từ 'cây' viết với âm 'c', không bao giờ đi với âm 'k'."},
            ]},
            {"name": "Từ loại – danh từ", "qs": [
                {"q": "Từ nào là danh từ?", "opts": ["chạy","đẹp","bàn","nhanh"], "ans": 2, "explain": "Danh từ là từ chỉ người, vật, con vật. 'Bàn' là đồ vật nên nó là danh từ."},
                {"q": "Chọn danh từ:", "opts": ["học","ghế","vui","xanh"], "ans": 1, "explain": "Cái 'ghế' là đồ vật con ngồi học, nên nó là danh từ."},
                {"q": "Từ nào KHÔNG phải danh từ?", "opts": ["sách","vở","đọc","bút"], "ans": 2, "explain": "'Đọc' là hành động (động từ), không phải tên đồ vật nên nó KHÔNG phải danh từ."},
                {"q": "Danh từ chỉ người:", "opts": ["chạy","thầy giáo","đẹp","vàng"], "ans": 1, "explain": "'Thầy giáo' là người dạy học con mỗi ngày, nên là danh từ chỉ người."},
                {"q": "Chọn danh từ chỉ con vật:", "opts": ["bay","to","con mèo","nhanh"], "ans": 2, "explain": "'Con mèo' là tên của một loài vật, nên nó là danh từ."},
                {"q": "Từ nào là danh từ?", "opts": ["nhảy","hát","trường học","vui vẻ"], "ans": 2, "explain": "'Trường học' là nơi chốn (địa điểm), nên nó là danh từ."},
                {"q": "Danh từ chỉ đồ vật:", "opts": ["cái bàn","chạy","đẹp","xanh"], "ans": 0, "explain": "'Cái bàn' là vật dụng bằng gỗ hoặc nhựa, dùng để học tập."},
                {"q": "Chọn danh từ:", "opts": ["nhìn","ngủ","ăn","cây bút"], "ans": 3, "explain": "'Cây bút' là đồ vật dùng để viết chữ. Các từ kia là hành động."},
                {"q": "Từ nào là danh từ?", "opts": ["vui","buồn","hạnh phúc","ngôi nhà"], "ans": 3, "explain": "'Ngôi nhà' là sự vật, nơi con ở. Các từ kia chỉ cảm xúc."},
                {"q": "Danh từ chỉ nơi chốn:", "opts": ["đẹp","chơi","trường học","nhanh"], "ans": 2, "explain": "'Trường học' là địa điểm con đến mỗi sáng."},
            ]},
            {"name": "Đặt câu – câu hỏi", "qs": [
                {"q": "Câu hỏi thường dùng từ nào?", "opts": ["vì","và","Ai? Cái gì?","nhưng"], "ans": 2, "explain": "Để hỏi người ta thường dùng: Ai (hỏi người), Cái gì (hỏi vật)."},
                {"q": "Câu 'Con đang làm gì?' hỏi về điều gì?", "opts": ["Người","Thời gian","Hành động","Nơi chốn"], "ans": 2, "explain": "Từ 'làm gì' dùng để hỏi xem bạn ấy đang thực hiện hành động nào (như học bài, ăn cơm...)."},
                {"q": "Chọn câu hỏi đúng:", "opts": ["Bạn ăn gì không?","Bạn ăn gì?","Bạn ăn gì nhỉ không?","Bạn ăn gì à không?"], "ans": 1, "explain": "Câu 'Bạn ăn gì?' là câu hỏi tự nhiên và đúng ngữ pháp nhất."},
                {"q": "Từ hỏi 'Ở đâu?' hỏi về điều gì?", "opts": ["Người","Nơi chốn","Thời gian","Số lượng"], "ans": 1, "explain": "'Ở đâu' dùng để hỏi về vị trí, địa điểm (như ở nhà, ở trường)."},
                {"q": "'Ai đang học bài?' — Từ hỏi là?", "opts": ["đang","học","Ai","bài"], "ans": 2, "explain": "Từ 'Ai' đứng đầu câu dùng để hỏi xem người đó là bạn nào."},
                {"q": "Từ hỏi 'Khi nào?' hỏi về điều gì?", "opts": ["Người","Nơi chốn","Thời gian","Cách thức"], "ans": 2, "explain": "'Khi nào' dùng để hỏi về giờ giấc, ngày tháng, sáng hay chiều (Thời gian)."},
                {"q": "Câu hỏi kết thúc bằng dấu gì?", "opts": ["Dấu chấm","Dấu phẩy","Dấu chấm hỏi","Dấu chấm than"], "ans": 2, "explain": "Đã là câu hỏi thì cuối câu bắt buộc phải có dấu chấm hỏi (?) con nhé!"},
                {"q": "Chọn câu hỏi:", "opts": ["Trời mưa to.","Trời có mưa không?","Trời mưa rất to!","Trời mưa, lạnh quá."], "ans": 1, "explain": "Câu có chứa từ 'không?' và kết thúc bằng dấu chấm hỏi (?) chính là câu hỏi."},
                {"q": "'Tại sao bạn khóc?' hỏi về điều gì?", "opts": ["Người","Nơi chốn","Thời gian","Lý do"], "ans": 3, "explain": "Từ 'Tại sao' (hoặc Vì sao) dùng để hỏi nguyên nhân/lý do của một sự việc."},
                {"q": "Từ hỏi 'Như thế nào?' hỏi về điều gì?", "opts": ["Người","Cách thức","Thời gian","Số lượng"], "ans": 1, "explain": "'Như thế nào' dùng để hỏi xem sự việc đó diễn ra ra sao, đặc điểm thế nào (Cách thức)."},
            ]},
            {"name": "Từ đồng nghĩa – trái nghĩa", "qs": [
                {"q": "Từ trái nghĩa với 'to' là?", "opts": ["lớn","bé","cao","nặng"], "ans": 1, "explain": "Trái ngược với con voi 'to' là con kiến 'bé' xíu."},
                {"q": "Từ đồng nghĩa với 'vui' là?", "opts": ["buồn","tức","vui vẻ","khóc"], "ans": 2, "explain": "Đồng nghĩa là có nghĩa giống nhau. 'Vui' cũng giống như 'vui vẻ', mừng rỡ."},
                {"q": "Từ trái nghĩa với 'ngày' là?", "opts": ["sáng","chiều","đêm","tối"], "ans": 2, "explain": "Ban 'ngày' có mặt trời chiếu sáng, trái ngược với ban 'đêm' tối thui có mặt trăng."},
                {"q": "Từ đồng nghĩa với 'nhanh' là?", "opts": ["chậm","mau","lâu","trễ"], "ans": 1, "explain": "Mẹ hay bảo 'Làm mau lên' cũng có nghĩa là 'Làm nhanh lên' đó con."},
                {"q": "Từ trái nghĩa với 'đen' là?", "opts": ["xanh","vàng","trắng","đỏ"], "ans": 2, "explain": "Màu 'đen' (như than) trái ngược hoàn toàn với màu 'trắng' (như tuyết)."},
                {"q": "Từ đồng nghĩa với 'đẹp' là?", "opts": ["xấu","xinh","to","nhỏ"], "ans": 1, "explain": "Bạn gái 'đẹp' cũng có nghĩa là bạn gái rất 'xinh' xắn."},
                {"q": "Từ trái nghĩa với 'nóng' là?", "opts": ["ấm","mát","lạnh","nguội"], "ans": 2, "explain": "Nước sôi rất 'nóng', trái ngược với nước đá rất 'lạnh'."},
                {"q": "Từ đồng nghĩa với 'nhà' là?", "opts": ["trường","chợ","ngôi nhà","phố"], "ans": 2, "explain": "Nhà còn được gọi đầy đủ là 'ngôi nhà' hoặc căn nhà."},
                {"q": "Từ trái nghĩa với 'cao' là?", "opts": ["to","thấp","lớn","béo"], "ans": 1, "explain": "Anh trai 'cao' kều, trái ngược với em bé 'thấp' bé."},
                {"q": "Từ đồng nghĩa với 'nhìn' là?", "opts": ["nghe","ngửi","xem","sờ"], "ans": 2, "explain": "Dùng mắt để 'nhìn' cũng giống như dùng mắt để 'xem' tivi vậy."},
            ]},
            {"name": "Đọc hiểu – câu văn", "qs": [
                {"q": "'Mặt trời mọc ở hướng nào?' — Câu trả lời đúng:", "opts": ["Hướng Tây","Hướng Bắc","Hướng Đông","Hướng Nam"], "ans": 2, "explain": "Mặt trời luôn mọc lên vào buổi sáng ở hướng Đông và lặn vào buổi chiều ở hướng Tây."},
                {"q": "Câu 'Con mèo đang ngủ.' nói về con vật nào?", "opts": ["Con chó","Con mèo","Con gà","Con cá"], "ans": 1, "explain": "Trong câu có nhắc đến từ 'Con mèo', nên câu này viết về con mèo."},
                {"q": "Câu văn nào tả về thời tiết?", "opts": ["Em đi học.","Trời hôm nay nắng đẹp.","Con mèo đen.","Bạn Nam chạy nhanh."], "ans": 1, "explain": "'Nắng đẹp' là từ chỉ đặc điểm của thời tiết bên ngoài."},
                {"q": "'Mùa hè, trời ____.' — Điền từ phù hợp:", "opts": ["lạnh giá","mưa phùn","nắng nóng","có tuyết"], "ans": 2, "explain": "Mùa hè (mùa hạ) thì có ông mặt trời chiếu rất gắt nên thời tiết 'nắng nóng'."},
                {"q": "Đoạn văn tả cảnh vườn thường có từ nào?", "opts": ["xe cộ","hoa lá","sóng biển","núi cao"], "ans": 1, "explain": "Trong khu vườn thì sẽ có rất nhiều cây xanh và 'hoa lá'."},
                {"q": "'Em thích ăn quả gì?' — Đây là câu gì?", "opts": ["Câu kể","Câu cảm","Câu hỏi","Câu cầu khiến"], "ans": 2, "explain": "Câu có từ 'gì' và kết thúc bằng dấu chấm hỏi (?) là câu hỏi."},
                {"q": "Câu 'Ơi, đẹp quá!' là câu gì?", "opts": ["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans": 2, "explain": "Câu bộc lộ cảm xúc khen ngợi (đẹp quá) và có dấu chấm than (!) là câu cảm (cảm thán)."},
                {"q": "'Hãy giữ gìn sách vở.' là câu gì?", "opts": ["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"], "ans": 3, "explain": "Câu yêu cầu, nhắc nhở người khác làm việc gì đó (có từ Hãy) là câu cầu khiến."},
                {"q": "Từ nào chỉ màu sắc?", "opts": ["chạy","đỏ","bàn","vui"], "ans": 1, "explain": "Màu 'đỏ' là màu của hoa hồng, mặt trời. Nó là từ chỉ màu sắc."},
                {"q": "Câu 'Bầu trời xanh trong.' tả điều gì?", "opts": ["Con vật","Cảnh vật","Người","Đồ vật"], "ans": 1, "explain": "Bầu trời là thiên nhiên, phong cảnh xung quanh chúng ta nên được gọi là Cảnh vật."},
            ]},
        ]
    },
}

# ── 4. QUẢN LÝ TRẠNG THÁI (STATE) ───────────────────────────────────────────
def init_state():
    if "screen" not in st.session_state: st.session_state.screen = "home"
    if "subject" not in st.session_state: st.session_state.subject = None
    if "topic_idx" not in st.session_state: st.session_state.topic_idx = None
    if "q_idx" not in st.session_state: st.session_state.q_idx = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "answered" not in st.session_state: st.session_state.answered = False
    if "selected" not in st.session_state: st.session_state.selected = None
    if "shuffled_qs" not in st.session_state: st.session_state.shuffled_qs = []

init_state()

def go_home(): st.session_state.screen = "home"

def go_topics(subj):
    st.session_state.subject = subj
    st.session_state.screen = "topics"

def go_quiz(topic_idx):
    qs = SUBJECTS[st.session_state.subject]["topics"][topic_idx]["qs"]
    shuffled = qs.copy()
    random.shuffle(shuffled)
    st.session_state.topic_idx = topic_idx
    st.session_state.shuffled_qs = shuffled
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.screen = "quiz"

def answer(i):
    if st.session_state.answered: return
    st.session_state.selected = i
    st.session_state.answered = True
    q = st.session_state.shuffled_qs[st.session_state.q_idx]
    if i == q["ans"]:
        st.session_state.score += 1

def next_q():
    st.session_state.q_idx += 1
    st.session_state.answered = False
    st.session_state.selected = None
    if st.session_state.q_idx >= len(st.session_state.shuffled_qs):
        st.session_state.screen = "result"

# ── 5. HIỂN THỊ GIAO DIỆN ────────────────────────────────────────────────────

if st.session_state.screen == "home":
    st.markdown('<div class="home-title bouncy">🌟 Học Vui Lớp 2 🌟</div>', unsafe_allow_html=True)
    st.markdown('<div class="home-sub">Con muốn chơi môn nào hôm nay?</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="subject-card card-math">
            <div class="subject-icon">🧮</div>
            <h2 class="subject-name math-text">TOÁN</h2>
        </div>""", unsafe_allow_html=True)
        if st.button("Chơi Toán", key="btn_math", type="primary", use_container_width=True):
            go_topics("math"); st.rerun()

    with col2:
        st.markdown("""
        <div class="subject-card card-viet">
            <div class="subject-icon">📚</div>
            <h2 class="subject-name viet-text">TIẾNG VIỆT</h2>
        </div>""", unsafe_allow_html=True)
        if st.button("Chơi Tiếng Việt", key="btn_viet", type="primary", use_container_width=True):
            go_topics("viet"); st.rerun()

elif st.session_state.screen == "topics":
    subj = st.session_state.subject
    sub = SUBJECTS[subj]
    
    st.markdown(f'<div class="home-title">{sub["icon"]} {sub["label"]}</div>', unsafe_allow_html=True)
    if st.button("⬅️ Quay lại", key="back_home"):
        go_home(); st.rerun()
    st.markdown("<br>", unsafe_allow_html=True)

    for i, topic in enumerate(sub["topics"]):
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"<h3 style='color: #444;'>{i+1}. {topic['name']}</h3>", unsafe_allow_html=True)
            with col2:
                if st.button("Vào chơi 🚀", key=f"topic_{i}", type="primary", use_container_width=True):
                    go_quiz(i); st.rerun()
            st.markdown("<hr style='border:1px dashed #CCC; margin: 10px 0;'>", unsafe_allow_html=True)

elif st.session_state.screen == "quiz":
    subj = st.session_state.subject
    qs = st.session_state.shuffled_qs
    q_idx = st.session_state.q_idx
    q = qs[q_idx]
    box_class = f"q-box-{SUBJECTS[subj]['color_class']}"

    # Progress bar cầu vồng
    pct = int(((q_idx) / len(qs)) * 100)
    st.markdown(f'<div style="text-align:right; font-weight:bold; color:#888;">Câu {q_idx + 1}/{len(qs)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="progress-track"><div class="progress-fill" style="width:{pct}%"></div></div>', unsafe_allow_html=True)

    # Câu hỏi
    st.markdown(f'<div class="q-box {box_class}"><p class="q-text">{q["q"]}</p></div>', unsafe_allow_html=True)

    # Nút đáp án
    for i, opt in enumerate(q["opts"]):
        is_correct = (i == q["ans"])
        is_selected = (i == st.session_state.selected)

        if not st.session_state.answered:
            if st.button(opt, key=f"opt_{q_idx}_{i}", use_container_width=True):
                answer(i); st.rerun()
        else:
            if is_correct:
                st.markdown(f'<div class="opt-btn-custom opt-correct">✅ {opt}</div>', unsafe_allow_html=True)
            elif is_selected:
                st.markdown(f'<div class="opt-btn-custom opt-wrong">❌ {opt}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="opt-btn-custom" style="opacity:0.5">{opt}</div>', unsafe_allow_html=True)

    # Feedback Đúng/Sai 
    if st.session_state.answered:
        if st.session_state.selected == q["ans"]:
            # Bé chọn ĐÚNG
            st.balloons()
            st.markdown('<div class="fb-correct-box"><span class="star-blink">⭐</span> ĐÚNG RỒI! BẠN GIỎI QUÁ! <span class="star-blink">⭐</span></div>', unsafe_allow_html=True)
        else:
            # Bé chọn SAI -> Hiển thị 3 phần: Động viên, Đáp án, Giải thích
            correct_text = q["opts"][q["ans"]]
            st.markdown(f"""
            <div class="fb-wrong-box">
                <div class="fb-w-msg">Ồ, chưa đúng rồi! Không sao, thử lại lần sau nhé! 💪</div>
                <div class="fb-w-correct">✅ Đáp án đúng là: <strong>{correct_text}</strong></div>
                <div class="fb-w-explain">💡 <strong>Thầy Khanh giải thích:</strong><br>{q['explain']}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        btn_label = "Câu tiếp theo ➡️" if q_idx < len(qs) - 1 else "Xem kết quả 🏆"
        if st.button(btn_label, key="next_q", type="primary", use_container_width=True):
            next_q(); st.rerun()

elif st.session_state.screen == "result":
    score = st.session_state.score
    total = len(st.session_state.shuffled_qs)
    
    if score == total:
        st.balloons()
        icon, title, msg = "🏆", "HOÀN HẢO!", "Đỉnh quá! Bé đạt điểm tuyệt đối luôn!"
    elif score >= 7:
        icon, title, msg = "⭐", "GIỎI LẮM!", "Bé làm rất tốt. Cố lên một chút nữa là đạt điểm tối đa!"
    elif score >= 5:
        icon, title, msg = "👍", "KHÁ TỐT!", "Bé đã rất cố gắng. Ôn lại bài một chút nhé!"
    else:
        icon, title, msg = "💪", "CỐ LÊN NÀO!", "Không sao đâu, bé hãy đọc lại giải thích và thử lại nhé!"

    st.markdown(f"""
    <div class="res-icon">{icon}</div>
    <div class="res-title">{title}</div>
    <div class="res-msg">{msg}</div>
    <div class="score-big">{score}</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Chơi lại bài này", key="retry", type="primary", use_container_width=True):
            go_quiz(st.session_state.topic_idx); st.rerun()
    with col2:
        if st.button("🏠 Về màn hình chính", key="home", use_container_width=True):
            go_home(); st.rerun()