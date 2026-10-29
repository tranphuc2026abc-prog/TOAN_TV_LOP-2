# Tự học lớp 3 – Hành trình tri thức

Website lớp 3 được xuất bản từ nhánh main. Trang lớp 2 cũ được lưu trữ riêng tại archive/index-lop2-backup.html.

## Chức năng
- Giao diện dành cho học sinh tiểu học, gồm Toán 3, Tiếng Việt 3 và Tiếng Anh 3.
- Hồ sơ học sinh, câu hỏi luyện tập, thử thách, sao, XP và huy hiệu.
- Lưu tiến độ trên trình duyệt bằng localStorage.
- Sao lưu tiến độ ra JSON và khôi phục từ JSON trong mục Hồ sơ & tiến độ.
- Danh mục bài học được đối chiếu từ OCR của 6 tệp PDF trong PDF_KNOWLEDGE/.

## Phạm vi danh mục đã đối chiếu
- **Toán 3 Kết nối tri thức:** 81 bài (Tập 1–2).
- **Tiếng Việt 3 Kết nối tri thức:** 62 bài đọc (Tập 1–2; số lượng được xác định lại từ mục lục OCR, thay cho ước tính 56 trước đây).
- **Tiếng Anh 3 Global Success:** 20 Unit, Starter và 4 bài Review.
- **Tổng danh mục:** 168 mục, gồm bài học, Starter và các bài ôn tập.

Danh mục đầy đủ và trang nguồn: data/CHUONG_TRINH_LOP_3_FULL.json.

## Lưu ý về chất lượng nội dung
Danh mục tên bài và trang đã được trích xuất/đối chiếu bằng OCR từ sáu PDF. Các bài bổ sung trong giao diện hiện có **bản nháp tóm tắt và câu hỏi luyện tập gợi ý**, không phải bản số hóa hoàn chỉnh từng trang SGK. Giáo viên cần rà soát độ chính xác và đáp án trước khi sử dụng chính thức. Website không đăng lại nguyên văn toàn bộ nội dung sách.

## Kiểm kê và lưu tiến độ
- Báo cáo kiểm kê: KIEM_KE_DU_LIEU_LOP_3.md.
- Tiến độ hiện lưu trên trình duyệt/thiết bị đang dùng, chưa đồng bộ đám mây. Hãy sao lưu JSON trước khi đổi thiết bị hoặc xóa dữ liệu trình duyệt.
