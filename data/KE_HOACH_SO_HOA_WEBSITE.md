# KẾ HOẠCH SỐ HÓA WEBSITE (HỆ THỐNG TỰ HỌC OFFLINE)

**1. Cấu trúc hệ thống và Giải pháp công nghệ (Phù hợp trường công lập)**
- **Nền tảng:** Web tĩnh (HTML/CSS/JS thuần hoặc sử dụng Hugo/Jekyll) để chạy trực tiếp trên máy tính phòng tin học không cần cài đặt máy chủ (Local Server/Offline 100%).
- **Lưu trữ tiến độ:** Sử dụng `localStorage` của trình duyệt web.
- **Tài nguyên:** Tích hợp file âm thanh (MP3) cho môn Tiếng Anh và hình ảnh nén (WebP) để tối ưu dung lượng.

**2. Tổ chức cấu trúc trang học tập**
- **Trang chủ:** Phân chia rõ 3 phân hệ (Toán 3, Tiếng Việt 3, Tiếng Anh 3).
- **Trang Bài học (Micro-learning):** Khám phá (Lý thuyết) -> Luyện tập (Tương tác nhanh) -> Vận dụng (Trò chơi hóa bài tập).

**3. Số hóa hoạt động tương tác theo môn học**
- **Toán 3:** Form nhập số liệu kiểm tra tức thời (Instant feedback), Game trắc nghiệm.
- **Tiếng Việt 3:** Văn bản có tooltip giải nghĩa từ khó, Dropdown bài tập chính tả.
- **Tiếng Anh 3:** Gắn audio vào các nút bấm hội thoại, bài tập click hình ảnh, thu âm phát âm cơ bản.

**4. Nội dung cần giáo viên kiểm duyệt**
- Đáp án bài toán mở/Tập làm văn.
- Quy tắc quy đổi điểm số trên phần mềm thành điểm thi đua/khen thưởng trên lớp.