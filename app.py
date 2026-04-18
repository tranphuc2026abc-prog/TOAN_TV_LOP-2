import streamlit as st
import random

# 1. Cấu hình trang
st.set_page_config(page_title="Học Vui Cùng Bé", page_icon="🎈", layout="centered")

st.title("🌟 Ứng dụng Học Toán & Tiếng Việt Lớp 2")
st.markdown("---")

# 2. Tạo 2 không gian học tập riêng biệt
tab_toan, tab_tv = st.tabs(["🧮 Thử tài Học Toán", "📖 Luyện Tiếng Việt"])

# --- PHÂN HỆ TOÁN LỚP 2 ---
with tab_toan:
    st.header("Phép cộng có nhớ trong phạm vi 100")
    
    # Sinh số ngẫu nhiên để bé làm không bị chán
    if 'so_a' not in st.session_state:
        st.session_state.so_a = random.randint(15, 89)
        st.session_state.so_b = random.randint(5, 99 - st.session_state.so_a)

    a = st.session_state.so_a
    b = st.session_state.so_b
    
    st.write(f"**Con hãy tính kết quả của phép toán sau:**")
    st.subheader(f"{a} + {b} = ?")
    
    cau_tra_loi = st.number_input("Nhập đáp án của con vào đây:", min_value=0, step=1, key="toan_input")
    
    if st.button("Kiểm tra Toán", type="primary"):
        if cau_tra_loi == (a + b):
            st.success("Tuyệt vời! Con làm đúng rồi! 🎉")
            st.balloons()
            # Nút tạo phép tính mới
            st.session_state.so_a = random.randint(15, 89)
            st.session_state.so_b = random.randint(5, 99 - st.session_state.so_a)
            st.rerun()
        else:
            st.error("Gần đúng rồi, con thử tính lại xem sao nhé! 💪")

# --- PHÂN HỆ TIẾNG VIỆT LỚP 2 ---
with tab_tv:
    st.header("Luyện từ vựng & Chính tả (tr/ch)")
    
    st.write("**Con hãy chọn từ viết đúng chính tả nhé:**")
    tu_chon = st.radio(
        "Lựa chọn của con là:",
        ("Chường học", "Trường học", "Trường hộc"),
        index=None
    )
    
    if st.button("Kiểm tra Tiếng Việt", type="primary"):
        if tu_chon == "Trường học":
            st.success("Chính xác! Con nhớ mặt chữ rất tốt! 🌟")
        elif tu_chon is None:
            st.warning("Con hãy chọn một đáp án trước khi kiểm tra nhé.")
        else:
            st.warning("Chú ý phân biệt âm 'tr' và 'ch' con nhé. Thử lại nào!")