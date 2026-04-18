import streamlit as st
import random

# ── Cấu hình trang ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ôn Luyện Lớp 2",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS toàn cục ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
}
.stApp { background-color: #f0f4ff; }

/* Ẩn header mặc định của Streamlit */
header[data-testid="stHeader"] { display: none; }
.block-container { padding-top: 2rem !important; max-width: 680px !important; }

/* ── Card chung ── */
.card {
    background: #ffffff;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.07);
    margin-bottom: 16px;
}

/* ── Tiêu đề trang chủ ── */
.home-title {
    text-align: center;
    font-size: 30px;
    font-weight: 900;
    color: #1e1b4b;
    margin: 0 0 4px;
}
.home-sub {
    text-align: center;
    font-size: 15px;
    color: #6b7280;
    margin: 0 0 28px;
}

/* ── Card môn học ── */
.subject-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 20px;
}
.subject-card {
    background: #ffffff;
    border: 1.5px solid #e5e7eb;
    border-radius: 18px;
    padding: 22px 16px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
}
.subject-card:hover { border-color: #a5b4fc; box-shadow: 0 4px 14px rgba(99,102,241,0.12); }
.subject-icon { font-size: 36px; margin-bottom: 8px; }
.subject-name { font-size: 18px; font-weight: 800; color: #1e1b4b; margin: 0 0 4px; }
.subject-count { font-size: 13px; color: #9ca3af; }
.badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 99px;
    margin-top: 10px;
}
.badge-math { background: #dbeafe; color: #1d4ed8; }
.badge-viet { background: #ede9fe; color: #6d28d9; }

/* ── Recent box ── */
.recent-box {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px 16px;
}
.recent-label { font-size: 11px; font-weight: 700; color: #9ca3af; text-transform: uppercase; letter-spacing: .04em; margin: 0 0 8px; }
.recent-row { display: flex; align-items: center; gap: 8px; font-size: 14px; color: #374151; }
.recent-score { margin-left: auto; font-size: 13px; color: #6b7280; font-weight: 600; }

/* ── Topic list ── */
.topic-btn-wrap { display: flex; flex-direction: column; gap: 10px; }
.topic-item {
    background: #fff;
    border: 1.5px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
    font-size: 15px;
    font-weight: 700;
    color: #1e1b4b;
    transition: all 0.15s;
}
.topic-item:hover { border-color: #a5b4fc; background: #f5f3ff; }
.topic-item span { font-size: 13px; font-weight: 600; color: #9ca3af; }

/* ── Progress bar ── */
.progress-track {
    height: 8px;
    background: #e5e7eb;
    border-radius: 99px;
    margin-bottom: 16px;
    overflow: hidden;
}
.progress-fill {
    height: 8px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    border-radius: 99px;
    transition: width 0.4s ease;
}
.q-counter { font-size: 13px; font-weight: 600; color: #6b7280; text-align: right; margin-bottom: 6px; }

/* ── Câu hỏi ── */
.q-box {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    border-radius: 18px;
    padding: 24px 22px;
    text-align: center;
    margin-bottom: 18px;
}
.q-text { font-size: 22px; font-weight: 800; color: #ffffff; margin: 0; line-height: 1.4; }

/* ── Đáp án ── */
.opt-btn-custom {
    background: #fff;
    border: 2px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px 18px;
    font-size: 16px;
    font-weight: 700;
    color: #1f2937;
    width: 100%;
    text-align: left;
    cursor: pointer;
    margin-bottom: 10px;
    transition: all 0.15s;
    display: block;
}
.opt-btn-custom:hover { border-color: #a5b4fc; background: #f5f3ff; }
.opt-correct { background: #ecfdf5 !important; border-color: #22c55e !important; color: #14532d !important; }
.opt-wrong   { background: #fef2f2 !important; border-color: #ef4444 !important; color: #7f1d1d !important; }

/* ── Feedback ── */
.feedback-correct {
    background: #ecfdf5;
    border: 1.5px solid #86efac;
    border-radius: 14px;
    padding: 14px 18px;
    font-size: 15px;
    font-weight: 700;
    color: #14532d;
    margin-top: 12px;
}
.feedback-wrong {
    background: #fef2f2;
    border: 1.5px solid #fca5a5;
    border-radius: 14px;
    padding: 14px 18px;
    font-size: 15px;
    font-weight: 700;
    color: #7f1d1d;
    margin-top: 12px;
}

/* ── Nút điều hướng ── */
div.stButton > button {
    border-radius: 14px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    height: 52px !important;
    transition: all 0.2s !important;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    border: none !important;
    color: white !important;
    box-shadow: 0 4px 14px rgba(99,102,241,0.35) !important;
}
div.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(99,102,241,0.4) !important;
}
div.stButton > button[kind="secondary"] {
    background: #fff !important;
    border: 2px solid #e5e7eb !important;
    color: #374151 !important;
}
div.stButton > button[kind="secondary"]:hover {
    border-color: #a5b4fc !important;
    background: #f5f3ff !important;
}

/* ── Màn kết quả ── */
.result-center { text-align: center; }
.result-icon { font-size: 56px; margin-bottom: 8px; }
.result-title { font-size: 28px; font-weight: 900; color: #1e1b4b; margin: 0 0 6px; }
.result-msg { font-size: 15px; color: #6b7280; margin: 0 0 24px; }
.score-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 24px;
}
.score-box {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 16px;
    text-align: center;
}
.score-num { font-size: 32px; font-weight: 900; color: #1e1b4b; }
.score-lbl { font-size: 13px; color: #9ca3af; font-weight: 600; margin-top: 2px; }
</style>
""", unsafe_allow_html=True)

# ── Dữ liệu câu hỏi ──────────────────────────────────────────────────────────
SUBJECTS = {
    "math": {
        "label": "Toán",
        "icon": "➕",
        "badge": "badge-math",
        "topics": [
            {
                "name": "Phép cộng có nhớ",
                "qs": [
                    {"q": "15 + 7 = ?",  "opts": ["20","22","23","21"], "ans": 1},
                    {"q": "28 + 5 = ?",  "opts": ["33","31","32","34"], "ans": 0},
                    {"q": "36 + 8 = ?",  "opts": ["44","42","43","45"], "ans": 0},
                    {"q": "49 + 6 = ?",  "opts": ["54","55","53","56"], "ans": 1},
                    {"q": "17 + 9 = ?",  "opts": ["25","27","26","24"], "ans": 2},
                    {"q": "38 + 7 = ?",  "opts": ["44","45","46","43"], "ans": 1},
                    {"q": "56 + 8 = ?",  "opts": ["63","65","64","62"], "ans": 2},
                    {"q": "27 + 6 = ?",  "opts": ["33","34","32","35"], "ans": 0},
                    {"q": "45 + 9 = ?",  "opts": ["53","55","54","52"], "ans": 2},
                    {"q": "67 + 8 = ?",  "opts": ["75","74","76","77"], "ans": 0},
                ],
            },
            {
                "name": "Phép trừ có nhớ",
                "qs": [
                    {"q": "23 - 7 = ?",  "opts": ["16","15","14","17"], "ans": 0},
                    {"q": "41 - 6 = ?",  "opts": ["34","36","35","33"], "ans": 2},
                    {"q": "52 - 8 = ?",  "opts": ["44","45","43","42"], "ans": 0},
                    {"q": "30 - 4 = ?",  "opts": ["26","28","25","27"], "ans": 0},
                    {"q": "61 - 9 = ?",  "opts": ["51","53","52","54"], "ans": 2},
                    {"q": "74 - 7 = ?",  "opts": ["67","65","66","68"], "ans": 0},
                    {"q": "83 - 5 = ?",  "opts": ["77","79","78","76"], "ans": 2},
                    {"q": "46 - 8 = ?",  "opts": ["38","37","39","36"], "ans": 0},
                    {"q": "55 - 6 = ?",  "opts": ["49","48","50","47"], "ans": 0},
                    {"q": "91 - 3 = ?",  "opts": ["89","87","88","86"], "ans": 2},
                ],
            },
            {
                "name": "So sánh số",
                "qs": [
                    {"q": "Số nào lớn hơn: 45 hay 54?",          "opts": ["45","54","Bằng nhau","Không biết"],   "ans": 1},
                    {"q": "Điền dấu: 73 __ 37",                   "opts": ["<",">","=","Không biết"],             "ans": 1},
                    {"q": "Số liền sau của 99 là?",               "opts": ["98","100","101","97"],                 "ans": 1},
                    {"q": "Số liền trước của 50 là?",             "opts": ["51","49","48","52"],                   "ans": 1},
                    {"q": "Điền dấu: 68 __ 86",                   "opts": [">","<","=","Không biết"],             "ans": 1},
                    {"q": "Số nào nhỏ nhất: 25, 52, 22, 55?",    "opts": ["25","52","22","55"],                   "ans": 2},
                    {"q": "Số nào lớn nhất: 31, 13, 33, 11?",    "opts": ["31","13","33","11"],                   "ans": 2},
                    {"q": "Điền dấu: 40 __ 40",                   "opts": [">","<","=","Không biết"],             "ans": 2},
                    {"q": "Số liền sau của 79 là?",               "opts": ["78","80","81","77"],                   "ans": 1},
                    {"q": "Số liền trước của 100 là?",            "opts": ["99","101","98","102"],                 "ans": 0},
                ],
            },
            {
                "name": "Đo lường",
                "qs": [
                    {"q": "1 dm = ? cm",   "opts": ["5 cm","10 cm","100 cm","1 cm"],     "ans": 1},
                    {"q": "1 m = ? dm",    "opts": ["100 dm","1 dm","10 dm","5 dm"],     "ans": 2},
                    {"q": "30 cm = ? dm",  "opts": ["3 dm","30 dm","300 dm","13 dm"],    "ans": 0},
                    {"q": "20 dm = ? m",   "opts": ["20 m","200 m","2 m","0,2 m"],       "ans": 2},
                    {"q": "1 m = ? cm",    "opts": ["10 cm","1000 cm","100 cm","1 cm"],  "ans": 2},
                    {"q": "5 dm = ? cm",   "opts": ["5 cm","500 cm","50 cm","15 cm"],    "ans": 2},
                    {"q": "2 m = ? dm",    "opts": ["2 dm","200 dm","20 dm","12 dm"],    "ans": 2},
                    {"q": "40 cm = ? dm",  "opts": ["40 dm","400 dm","4 dm","14 dm"],    "ans": 2},
                    {"q": "3 m = ? cm",    "opts": ["3 cm","30 cm","300 cm","3000 cm"],  "ans": 2},
                    {"q": "6 dm = ? cm",   "opts": ["6 cm","600 cm","60 cm","16 cm"],    "ans": 2},
                ],
            },
            {
                "name": "Hình học",
                "qs": [
                    {"q": "Hình chữ nhật có bao nhiêu góc vuông?",           "opts": ["2","3","4","1"],                                         "ans": 2},
                    {"q": "Hình vuông có bao nhiêu cạnh bằng nhau?",         "opts": ["2","3","0","4"],                                         "ans": 3},
                    {"q": "Hình tam giác có bao nhiêu cạnh?",                 "opts": ["4","2","3","5"],                                         "ans": 2},
                    {"q": "Hình nào có tất cả các cạnh bằng nhau?",          "opts": ["Hình chữ nhật","Hình tam giác","Hình vuông","Hình thang"],"ans": 2},
                    {"q": "Hình tròn có bao nhiêu góc?",                      "opts": ["1","2","3","0"],                                         "ans": 3},
                    {"q": "Hình chữ nhật có bao nhiêu cạnh?",                "opts": ["3","4","5","6"],                                         "ans": 1},
                    {"q": "Hình nào KHÔNG có góc vuông?",                     "opts": ["Hình vuông","Hình chữ nhật","Hình tròn","Tất cả"],       "ans": 2},
                    {"q": "Hình tam giác có bao nhiêu góc?",                  "opts": ["2","4","3","1"],                                         "ans": 2},
                    {"q": "Hình vuông có bao nhiêu cạnh?",                    "opts": ["3","5","6","4"],                                         "ans": 3},
                    {"q": "Hình chữ nhật: cạnh dài gọi là?",                 "opts": ["Chiều rộng","Chiều cao","Chiều dài","Cạnh bên"],         "ans": 2},
                ],
            },
        ],
    },
    "viet": {
        "label": "Tiếng Việt",
        "icon": "✏️",
        "badge": "badge-viet",
        "topics": [
            {
                "name": "Chính tả – âm vần",
                "qs": [
                    {"q": "Chọn từ viết đúng chính tả:",              "opts": ["giòng sông","dòng sông","giòng xông","dòng xông"],        "ans": 1},
                    {"q": "Từ nào viết đúng?",                          "opts": ["xanh lá cây","sanh lá cây","xanh lá kay","xang lá cây"], "ans": 0},
                    {"q": "Điền vào chỗ trống: con ...ó (c/g)",        "opts": ["co","gó","có","gò"],                                     "ans": 2},
                    {"q": "Chọn từ đúng: trời mưa hay giời mưa?",      "opts": ["giời mưa","trời mưa","trởi mưa","chời mưa"],            "ans": 1},
                    {"q": "Từ nào viết sai?",                           "opts": ["quả cam","quả xoài","quả dưa","quả khôm"],              "ans": 3},
                    {"q": "Điền vào: bầu ....i (tr/ch)",               "opts": ["chời","trời","cời","gời"],                              "ans": 1},
                    {"q": "Chọn từ đúng:",                              "opts": ["con trâu","con châu","con trau","con chau"],            "ans": 0},
                    {"q": "Từ nào viết đúng?",                          "opts": ["buổi sáng","buổi xáng","buỗi sáng","buổi sạng"],       "ans": 0},
                    {"q": "Điền vào: hoa ...ồng (h/r)",                "opts": ["rồng","hồng","lồng","đồng"],                           "ans": 1},
                    {"q": "Chọn từ đúng:",                              "opts": ["lá cây","lá kây","la cây","lá cay"],                   "ans": 0},
                ],
            },
            {
                "name": "Từ loại – danh từ",
                "qs": [
                    {"q": "Từ nào là danh từ?",              "opts": ["chạy","đẹp","bàn","nhanh"],                    "ans": 2},
                    {"q": "Chọn danh từ:",                    "opts": ["học","ghế","vui","xanh"],                     "ans": 1},
                    {"q": "Từ nào KHÔNG phải danh từ?",      "opts": ["sách","vở","đọc","bút"],                      "ans": 2},
                    {"q": "Danh từ chỉ người:",               "opts": ["chạy","thầy giáo","đẹp","vàng"],             "ans": 1},
                    {"q": "Chọn danh từ chỉ con vật:",        "opts": ["bay","to","con mèo","nhanh"],                 "ans": 2},
                    {"q": "Từ nào là danh từ?",              "opts": ["nhảy","hát","trường học","vui vẻ"],            "ans": 2},
                    {"q": "Danh từ chỉ đồ vật:",             "opts": ["cái bàn","chạy","đẹp","xanh"],               "ans": 0},
                    {"q": "Chọn danh từ:",                    "opts": ["nhìn","ngủ","ăn","cây bút"],                  "ans": 3},
                    {"q": "Từ nào là danh từ?",              "opts": ["vui","buồn","hạnh phúc","ngôi nhà"],          "ans": 3},
                    {"q": "Danh từ chỉ nơi chốn:",           "opts": ["đẹp","chơi","trường học","nhanh"],            "ans": 2},
                ],
            },
            {
                "name": "Đặt câu – câu hỏi",
                "qs": [
                    {"q": "Câu hỏi thường dùng từ nào?",                      "opts": ["vì","và","Ai? Cái gì?","nhưng"],                                              "ans": 2},
                    {"q": "Câu 'Con đang làm gì?' hỏi về điều gì?",           "opts": ["Người","Thời gian","Hành động","Nơi chốn"],                                   "ans": 2},
                    {"q": "Chọn câu hỏi đúng:",                                "opts": ["Bạn ăn gì không?","Bạn ăn gì?","Bạn ăn gì nhỉ không?","Bạn ăn gì à không?"],"ans": 1},
                    {"q": "Từ hỏi 'Ở đâu?' hỏi về điều gì?",                 "opts": ["Người","Nơi chốn","Thời gian","Số lượng"],                                    "ans": 1},
                    {"q": "'Ai đang học bài?' — Từ hỏi là?",                  "opts": ["đang","học","Ai","bài"],                                                      "ans": 2},
                    {"q": "Từ hỏi 'Khi nào?' hỏi về điều gì?",               "opts": ["Người","Nơi chốn","Thời gian","Cách thức"],                                   "ans": 2},
                    {"q": "Câu hỏi kết thúc bằng dấu gì?",                    "opts": ["Dấu chấm","Dấu phẩy","Dấu chấm hỏi","Dấu chấm than"],                       "ans": 2},
                    {"q": "Chọn câu hỏi:",                                     "opts": ["Trời mưa to.","Trời có mưa không?","Trời mưa rất to!","Trời mưa, lạnh quá."],"ans": 1},
                    {"q": "'Tại sao bạn khóc?' hỏi về điều gì?",              "opts": ["Người","Nơi chốn","Thời gian","Lý do"],                                       "ans": 3},
                    {"q": "Từ hỏi 'Như thế nào?' hỏi về điều gì?",           "opts": ["Người","Cách thức","Thời gian","Số lượng"],                                   "ans": 1},
                ],
            },
            {
                "name": "Từ đồng nghĩa – trái nghĩa",
                "qs": [
                    {"q": "Từ trái nghĩa với 'to' là?",       "opts": ["lớn","bé","cao","nặng"],           "ans": 1},
                    {"q": "Từ đồng nghĩa với 'vui' là?",      "opts": ["buồn","tức","vui vẻ","khóc"],     "ans": 2},
                    {"q": "Từ trái nghĩa với 'ngày' là?",     "opts": ["sáng","chiều","đêm","tối"],        "ans": 2},
                    {"q": "Từ đồng nghĩa với 'nhanh' là?",    "opts": ["chậm","mau","lâu","trễ"],         "ans": 1},
                    {"q": "Từ trái nghĩa với 'đen' là?",      "opts": ["xanh","vàng","trắng","đỏ"],       "ans": 2},
                    {"q": "Từ đồng nghĩa với 'đẹp' là?",      "opts": ["xấu","xinh","to","nhỏ"],          "ans": 1},
                    {"q": "Từ trái nghĩa với 'nóng' là?",     "opts": ["ấm","mát","lạnh","nguội"],        "ans": 2},
                    {"q": "Từ đồng nghĩa với 'nhà' là?",      "opts": ["trường","chợ","ngôi nhà","phố"],  "ans": 2},
                    {"q": "Từ trái nghĩa với 'cao' là?",      "opts": ["to","thấp","lớn","béo"],          "ans": 1},
                    {"q": "Từ đồng nghĩa với 'nhìn' là?",     "opts": ["nghe","ngửi","xem","sờ"],         "ans": 2},
                ],
            },
            {
                "name": "Đọc hiểu – câu văn",
                "qs": [
                    {"q": "'Mặt trời mọc ở hướng nào?' — Câu trả lời đúng:",  "opts": ["Hướng Tây","Hướng Bắc","Hướng Đông","Hướng Nam"],                                           "ans": 2},
                    {"q": "Câu 'Con mèo đang ngủ.' nói về con vật nào?",       "opts": ["Con chó","Con mèo","Con gà","Con cá"],                                                      "ans": 1},
                    {"q": "Câu văn nào tả về thời tiết?",                       "opts": ["Em đi học.","Trời hôm nay nắng đẹp.","Con mèo đen.","Bạn Nam chạy nhanh."],               "ans": 1},
                    {"q": "'Mùa hè, trời ____.' — Điền từ phù hợp:",           "opts": ["lạnh giá","mưa phùn","nắng nóng","có tuyết"],                                              "ans": 2},
                    {"q": "Đoạn văn tả cảnh vườn thường có từ nào?",           "opts": ["xe cộ","hoa lá","sóng biển","núi cao"],                                                    "ans": 1},
                    {"q": "'Em thích ăn quả gì?' — Đây là câu gì?",            "opts": ["Câu kể","Câu cảm","Câu hỏi","Câu cầu khiến"],                                             "ans": 2},
                    {"q": "Câu 'Ơi, đẹp quá!' là câu gì?",                     "opts": ["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"],                                             "ans": 2},
                    {"q": "'Hãy giữ gìn sách vở.' là câu gì?",                 "opts": ["Câu hỏi","Câu kể","Câu cảm","Câu cầu khiến"],                                             "ans": 3},
                    {"q": "Từ nào chỉ màu sắc?",                                "opts": ["chạy","đỏ","bàn","vui"],                                                                   "ans": 1},
                    {"q": "Câu 'Bầu trời xanh trong.' tả điều gì?",            "opts": ["Con vật","Cảnh vật","Người","Đồ vật"],                                                     "ans": 1},
                ],
            },
        ],
    },
}

PRAISE = [
    "🎉 Tuyệt vời! Bạn thật thông minh!",
    "⭐ Chính xác! Giỏi lắm!",
    "🌟 Đúng rồi! Cố lên nhé!",
    "🏆 Xuất sắc! Bạn học rất giỏi!",
    "🎊 Đúng rồi! Bạn thật tài năng!",
]

# ── Khởi tạo session_state ───────────────────────────────────────────────────
def init_state():
    defaults = {
        "screen": "home",          # home | topics | quiz | result
        "subject": None,
        "topic_idx": None,
        "q_idx": 0,
        "score": 0,
        "answered": False,
        "selected": None,
        "shuffled_qs": [],
        "recent": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ── Hàm điều hướng ───────────────────────────────────────────────────────────
def go_home():
    st.session_state.screen = "home"

def go_topics(subj):
    st.session_state.subject = subj
    st.session_state.screen = "topics"

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
    st.session_state.screen      = "quiz"

def answer(i):
    if st.session_state.answered:
        return
    st.session_state.selected = i
    st.session_state.answered = True
    q = st.session_state.shuffled_qs[st.session_state.q_idx]
    if i == q["ans"]:
        st.session_state.score += 1

def next_q():
    st.session_state.q_idx  += 1
    st.session_state.answered = False
    st.session_state.selected = None
    total = len(st.session_state.shuffled_qs)
    if st.session_state.q_idx >= total:
        # lưu recent
        subj_label  = SUBJECTS[st.session_state.subject]["label"]
        topic_name  = SUBJECTS[st.session_state.subject]["topics"][st.session_state.topic_idx]["name"]
        st.session_state.recent = {
            "name": topic_name,
            "subj": subj_label,
            "badge": SUBJECTS[st.session_state.subject]["badge"],
            "score": st.session_state.score,
            "total": total,
        }
        st.session_state.screen = "result"

# ── Render từng màn ──────────────────────────────────────────────────────────

# ── MÀN 1: TRANG CHỦ ────────────────────────────────────────────────────────
if st.session_state.screen == "home":
    st.markdown('<div class="home-title">🌟 Ôn Luyện Lớp 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="home-sub">Chọn môn học để bắt đầu luyện tập</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="subject-card">
            <div class="subject-icon">➕</div>
            <div class="subject-name">Toán</div>
            <div class="subject-count">5 chủ đề · 10 câu/bài</div>
            <span class="badge badge-math">Toán học</span>
        </div>""", unsafe_allow_html=True)
        if st.button("Học Toán", key="btn_math", type="primary", use_container_width=True):
            go_topics("math")
            st.rerun()

    with col2:
        st.markdown("""
        <div class="subject-card">
            <div class="subject-icon">✏️</div>
            <div class="subject-name">Tiếng Việt</div>
            <div class="subject-count">5 chủ đề · 10 câu/bài</div>
            <span class="badge badge-viet">Tiếng Việt</span>
        </div>""", unsafe_allow_html=True)
        if st.button("Học Tiếng Việt", key="btn_viet", type="primary", use_container_width=True):
            go_topics("viet")
            st.rerun()

    # Recent
    if st.session_state.recent:
        r = st.session_state.recent
        st.markdown(f"""
        <div class="recent-box">
            <p class="recent-label">Kết quả gần đây</p>
            <div class="recent-row">
                <span>{r['name']}</span>
                <span class="badge {r['badge']}">{r['subj']}</span>
                <span class="recent-score">{r['score']}/{r['total']} đúng</span>
            </div>
        </div>""", unsafe_allow_html=True)

# ── MÀN 2: CHỌN CHỦ ĐỀ ──────────────────────────────────────────────────────
elif st.session_state.screen == "topics":
    subj = st.session_state.subject
    sub  = SUBJECTS[subj]
    if st.button("← Trang chủ", key="back_home", type="secondary"):
        go_home(); st.rerun()

    st.markdown(f"<p style='font-size:12px;font-weight:700;color:#9ca3af;text-transform:uppercase;letter-spacing:.04em;margin:12px 0 10px;'>{sub['label']} — Chọn chủ đề</p>", unsafe_allow_html=True)

    for i, topic in enumerate(sub["topics"]):
        col_a, col_b = st.columns([5, 1])
        with col_a:
            st.markdown(f"<div style='font-size:15px;font-weight:700;color:#1e1b4b;padding:4px 0;'>{topic['name']}</div>", unsafe_allow_html=True)
        with col_b:
            st.markdown("<div style='font-size:13px;color:#9ca3af;padding:4px 0;text-align:right;'>10 câu</div>", unsafe_allow_html=True)
        if st.button(f"Bắt đầu →", key=f"topic_{i}", type="primary", use_container_width=True):
            go_quiz(i); st.rerun()
        st.markdown("<hr style='border:none;border-top:1px solid #f3f4f6;margin:4px 0 10px;'>", unsafe_allow_html=True)

# ── MÀN 3: CÂU HỎI ──────────────────────────────────────────────────────────
elif st.session_state.screen == "quiz":
    subj      = st.session_state.subject
    qs        = st.session_state.shuffled_qs
    q_idx     = st.session_state.q_idx
    total     = len(qs)
    answered  = st.session_state.answered
    selected  = st.session_state.selected
    q         = qs[q_idx]

    col_back, col_cnt = st.columns([3, 1])
    with col_back:
        if st.button("← Chủ đề", key="back_topics", type="secondary"):
            go_topics(subj); st.rerun()
    with col_cnt:
        st.markdown(f"<div class='q-counter'>Câu {q_idx + 1} / {total}</div>", unsafe_allow_html=True)

    pct = int((q_idx / total) * 100)
    st.markdown(f"""
    <div class="progress-track">
        <div class="progress-fill" style="width:{pct}%"></div>
    </div>""", unsafe_allow_html=True)

    st.markdown(f'<div class="q-box"><p class="q-text">{q["q"]}</p></div>', unsafe_allow_html=True)

    # Đáp án
    for i, opt in enumerate(q["opts"]):
        is_correct = (i == q["ans"])
        is_selected = (i == selected)

        if not answered:
            if st.button(opt, key=f"opt_{q_idx}_{i}", use_container_width=True, type="secondary"):
                answer(i); st.rerun()
        else:
            # Sau khi trả lời: tô màu
            if is_correct:
                st.markdown(f'<div class="opt-btn-custom opt-correct">✔ {opt}</div>', unsafe_allow_html=True)
            elif is_selected and not is_correct:
                st.markdown(f'<div class="opt-btn-custom opt-wrong">✘ {opt}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="opt-btn-custom" style="opacity:.55">{opt}</div>', unsafe_allow_html=True)

    # Feedback
    if answered:
        if selected == q["ans"]:
            msg = random.choice(PRAISE)
            st.markdown(f'<div class="feedback-correct">{msg}</div>', unsafe_allow_html=True)
        else:
            correct_text = q["opts"][q["ans"]]
            st.markdown(f'<div class="feedback-wrong">✘ Chưa đúng rồi. Đáp án đúng là <strong>{correct_text}</strong>. Hãy đọc lại và ghi nhớ nhé!</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        label = "Câu tiếp theo →" if q_idx < total - 1 else "Xem kết quả →"
        if st.button(label, key="next_q", type="primary", use_container_width=True):
            next_q(); st.rerun()

# ── MÀN 4: KẾT QUẢ ──────────────────────────────────────────────────────────
elif st.session_state.screen == "result":
    score = st.session_state.score
    total = len(st.session_state.shuffled_qs)
    pct   = score / total

    if pct == 1.0:
        icon, title, msg = "🏆", "Hoàn hảo!", f"Bạn đã trả lời đúng tất cả {total} câu. Giỏi lắm!"
    elif pct >= 0.8:
        icon, title, msg = "⭐", "Xuất sắc!", f"Bạn đã trả lời đúng {score}/{total} câu. Tiếp tục cố gắng nhé!"
    elif pct >= 0.6:
        icon, title, msg = "👍", "Khá tốt!", f"Bạn đã trả lời đúng {score}/{total} câu. Ôn lại một chút nữa nhé!"
    else:
        icon, title, msg = "💪", "Cố lên nào!", f"Bạn đã trả lời đúng {score}/{total} câu. Hãy luyện tập thêm nhé!"

    st.markdown(f"""
    <div class="result-center">
        <div class="result-icon">{icon}</div>
        <div class="result-title">{title}</div>
        <div class="result-msg">{msg}</div>
        <div class="score-grid">
            <div class="score-box">
                <div class="score-num" style="color:#22c55e;">{score}</div>
                <div class="score-lbl">Câu đúng</div>
            </div>
            <div class="score-box">
                <div class="score-num" style="color:#ef4444;">{total - score}</div>
                <div class="score-lbl">Câu sai</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Luyện lại", key="retry", type="secondary", use_container_width=True):
            go_quiz(st.session_state.topic_idx); st.rerun()
    with col2:
        if st.button("📚 Chủ đề khác →", key="other", type="primary", use_container_width=True):
            go_topics(st.session_state.subject); st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Trang chủ", key="home_from_result", type="secondary", use_container_width=True):
        go_home(); st.rerun()
