import streamlit as st
import random

# --- 1. Cấu hình & CSS (Giữ phong cách kid-friendly) ---
st.set_page_config(page_title="Học Vui Cùng Bé", page_icon="🎈", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #f0f2f6; font-family: 'Inter', sans-serif; }
    
    /* Card chọn chủ đề */
    .topic-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        text-align: center;
        transition: 0.3s;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Câu hỏi & Gợi ý */
    .question-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
        border: 2px solid #6366f1;
    }
    .hint-box {
        background-color: #fff4e5;
        border-left: 5px solid #ff9800;
        padding: 15px;
        margin-top: 15px;
        border-radius: 8px;
        color: #663c00;
        font-weight: 500;
    }
    
    /* Nút bấm */
    div.stButton > button {
        border-radius: 12px !important;
        font-weight: bold !important;
        height: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. Khởi tạo Trạng thái (Session State) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None
if 'question_idx' not in st.session_state:
    st.session_state.question_idx = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False

# Giả lập dữ liệu câu hỏi (Thầy có thể thay bằng dữ liệu từ Google Sheets sau này)
DATA = {
    "Phép cộng, trừ phạm vi 1000": [
        {"q": "350 + 120 = ?", "a": "470", "hint": "Con hãy cộng hàng đơn vị trước (0+0), rồi đến hàng chục (5+2) và hàng trăm (3+1) nhé!"},
        {"q": "500 - 200 = ?", "a": "300", "hint": "5 trăm trừ đi 2 trăm còn mấy trăm hả con?"}
    ],
    "Hình học & Đo lường": [
        {"q": "Hình có 3 cạnh là hình gì?", "a": "Hình tam giác", "hint": "Con hãy nhớ lại các hình đã học: tròn, vuông, tam giác..."},
        {"q": "1 mét bằng bao nhiêu xăng-ti-mét (cm)?", "a": "100", "hint": "Cứ 10 decimet là 1 mét, mà 1 decimet là 10 cm. Vậy là...?"}
    ]
}

# --- 3. Điều hướng Giao diện ---

# MÀN HÌNH CHÍNH: Chọn chủ đề
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center;'>🌟 Chào con yêu!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Hôm nay con muốn thử tài với chủ đề nào?</p>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    topics = list(DATA.keys())
    
    for i, topic in enumerate(topics):
        with cols[i % 2]:
            st.markdown(f"""<div class='topic-card'><h3>{topic}</h3></div>""", unsafe_allow_html=True)
            if st.button(f"Chọn {i+1}", key=f"btn_{i}"):
                st.session_state.selected_topic = topic
                st.session_state.page = 'quiz'
                st.session_state.question_idx = 0
                st.rerun()

# MÀN HÌNH LÀM BÀI
elif st.session_state.page == 'quiz':
    topic = st.session_state.selected_topic
    questions = DATA[topic]
    
    if st.session_state.question_idx < len(questions):
        q_item = questions[st.session_state.question_idx]
        
        st.button("⬅️ Quay lại menu", on_click=lambda: st.session_state.update(page='home'))
        st.markdown(f"### Chủ đề: {topic}")
        st.progress((st.session_state.question_idx + 1) / len(questions))
        
        # Hiển thị câu hỏi
        st.markdown(f"""<div class='question-box'><h2>{q_item['q']}</h2></div>""", unsafe_allow_html=True)
        
        # Nhập câu trả lời
        user_ans = st.text_input("Đáp án của con:", key=f"ans_{st.session_state.question_idx}").strip()
        
        col1, col2 = st.columns(2)
        with col1:
            check_btn = st.button("Kiểm tra 🚀", use_container_width=True)
        
        if check_btn:
            if user_ans.lower() == q_item['a'].lower():
                st.success("🎉 Giỏi quá! Con làm đúng rồi.")
                st.balloons()
                st.session_state.show_hint = False
                # Hiện nút tiếp tục
                if st.button("Tiếp tục câu tiếp theo ➡️", type="primary", use_container_width=True):
                    st.session_state.question_idx += 1
                    st.rerun()
            else:
                st.error("💡 Chưa đúng rồi, con thử lại nhé!")
                st.session_state.show_hint = True
        
        # Hiển thị gợi ý nếu trả lời sai
        if st.session_state.show_hint:
            st.markdown(f"""<div class='hint-box'><b>Gợi ý cho con:</b><br>{q_item['hint']}</div>""", unsafe_allow_html=True)
            if st.button("Con muốn bỏ qua câu này ⏭️"):
                st.session_state.question_idx += 1
                st.session_state.show_hint = False
                st.rerun()
                
    else:
        # Màn hình hoàn thành
        st.success("🎊 Chúc mừng con đã hoàn thành tất cả bài tập!")
        if st.button("Quay về trang chủ"):
            st.session_state.page = 'home'
            st.rerun()