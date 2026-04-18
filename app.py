import streamlit as st
import random

# 1. Cấu hình trang (Giao diện rộng rãi hơn)
st.set_page_config(page_title="Toán & Tiếng Việt Lớp 2", page_icon="🌟", layout="centered")

# 2. Bơm CSS tùy chỉnh (Mang thiết kế từ index.html sang Streamlit)
st.markdown("""
<style>
    /* Đổi màu nền ứng dụng giống file HTML */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }
    
    /* Tùy chỉnh giao diện Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: 600;
        color: #6b7280;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.02);
    }
    .stTabs [aria-selected="true"] {
        color: #6366f1 !important;
        border-bottom: 4px solid #6366f1 !important;
    }
    
    /* Tùy chỉnh nút bấm (Button) to, tròn, dễ nhấn cho bé */
    div.stButton > button:first-child {
        background-color: #6366f1;
        color: white;
        border-radius: 12px;
        padding: 10px 30px;
        font-size: 20px;
        font-weight: bold;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(99, 102, 241, 0.3);
    }
    div.stButton > button:first-child:hover {
        background-color: #4f46e5;
        transform: translateY(-2px);
    }
    
    /* Tiêu đề chính */
    .main-title {
        text-align: center;
        color: #111827;
        font-size: 36px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 16px;
        margin-bottom: 30px;
    }
    
    /* Phông chữ bài toán to, rõ, màu nổi bật */
    .math-problem {
        text-align: center;
        font-size: 55px;
        font-weight: 800;
        color: #e63946;
        letter-spacing: 3px;
        margin: 20px 0;
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #c7d2fe;
    }
    
    /* Khung nhập liệu (Input) */
    .stNumberInput input {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        height: 60px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Giao diện Tiêu đề (Giống hệt phần Header của index.html)
st.markdown('<div class="main-title">★ ★ ★<br>Toán & Tiếng Việt Lớp 2</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Kết nối tri thức với cuộc sống • Ôn tập cuối năm</div>', unsafe_allow_html=True)

# 4. Tạo 2 không gian học tập
tab_toan, tab_tv = st.tabs(["🧮 Thử tài Học Toán", "📖 Luyện Tiếng Việt"])

# --- PHÂN HỆ TOÁN LỚP 2 ---
with tab_toan:
    st.markdown("<h3 style='text-align: center; color: #1f2937;'>Phép cộng có nhớ trong phạm vi 100</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6b7280;'>Con hãy nhẩm tính và điền kết quả đúng nhé!</p>", unsafe_allow_html=True)
    
    # Khởi tạo số ngẫu nhiên
    if 'so_a' not in st.session_state:
        st.session_state.so_a = random.randint(15, 89)
        st.session_state.so_b = random.randint(5, 99 - st.session_state.so_a)

    a = st.session_state.so_a
    b = st.session_state.so_b
    
    # Hiển thị phép toán cực to và rõ ràng
    st.markdown(f'<div class="math-problem">{a} + {b} = ?</div>', unsafe_allow_html=True)
    
    # Layout 3 cột để căn giữa ô nhập liệu
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        cau_tra_loi = st.number_input("Nhập đáp án:", min_value=0, step=1, key="toan_input", label_visibility="collapsed")
        
        if st.button("Kiểm tra ngay 🚀", type="primary"):
            if cau_tra_loi == (a + b):
                st.success("🎉 TUYỆT VỜI! Con làm đúng rồi!")
                st.balloons()
                # Nút tạo phép tính mới
                st.session_state.so_a = random.randint(15, 89)
                st.session_state.so_b = random.randint(5, 99 - st.session_state.so_a)
            else:
                st.error("💡 Gần đúng rồi, con thử tính lại xem sao nhé!")

# --- PHÂN HỆ TIẾNG VIỆT LỚP 2 ---
with tab_tv:
    st.markdown("<h3 style='text-align: center; color: #1f2937;'>Luyện từ vựng & Chính tả (tr/ch)</h3>", unsafe_allow_html=True)
    
    st.info("📌 **Yêu cầu:** Con hãy chọn từ viết đúng chính tả dưới đây:")
    
    tu_chon = st.radio(
        "Lựa chọn của con là:",
        ("Chường học", "Trường học", "Trường hộc"),
        index=None,
        label_visibility="collapsed"
    )
    
    st.write("") # Tạo khoảng trống
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Nộp bài Tiếng Việt ✍️", type="primary"):
            if tu_chon == "Trường học":
                st.success("🌟 CHÍNH XÁC! Con nhớ mặt chữ rất tốt!")
            elif tu_chon is None:
                st.warning("⚠️ Con hãy nhấp chọn một đáp án trước khi nộp bài nhé.")
            else:
                st.error("💡 Chú ý phân biệt âm 'tr' và 'ch' con nhé. Thử lại nào!")