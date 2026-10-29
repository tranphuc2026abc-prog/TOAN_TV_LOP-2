# Kiểm kê dữ liệu và trạng thái website tự học lớp 3

## Trạng thái hiện tại
Website lớp 3 được xuất bản từ nhánh main. Bản lớp 2 cũ được lưu tại archive/index-lop2-backup.html.

## Nguồn và kết quả OCR
Thư mục PDF_KNOWLEDGE có 6 sách nguồn:
- Toán 3 Kết nối tri thức, Tập 1 và Tập 2.
- Tiếng Việt 3 Kết nối tri thức, Tập 1 và Tập 2.
- Tiếng Anh 3 Global Success, Tập 1 và Tập 2.

Các PDF là ảnh quét nên đã chạy OCR tiếng Việt/tiếng Anh trên tổng cộng **716 trang PDF**. Kết quả OCR có văn bản cho cả 716 trang; nội dung toàn văn OCR chỉ được giữ trong artifact xử lý tạm, không được sao chép nguyên văn vào website công khai.

## Phạm vi danh mục đã đối chiếu từ mục lục và trang nguồn
| Môn học | Số mục | Phạm vi |
|---|---:|---|
| Toán 3 Kết nối tri thức | 81 bài | Bài 1–81, Tập 1–2 |
| Tiếng Việt 3 Kết nối tri thức | 62 bài đọc | 32 bài Tập 1 và 30 bài Tập 2 |
| Tiếng Anh 3 Global Success | 20 Unit | Unit 1–20 |
| Tiếng Anh: phần bổ sung | 6 mục | Starter và Review 1–4; mục lục có thêm tài nguyên Wordlist nhưng không tính là bài học |
| **Tổng danh mục** | **168 mục** | Bao gồm bài học, Starter và các bài ôn tập |

Lưu ý: ước tính trước đây là 56 bài Tiếng Việt chưa chính xác. Đối chiếu OCR từ mục lục hai tập cho thấy có 32 + 30 = **62 bài đọc**.

Danh mục có ID, tên bài, tập sách và trang nguồn nằm tại:
- data/CHUONG_TRINH_LOP_3_FULL.json

## Trạng thái nội dung trong website
- Website giữ nguyên 17 bài mẫu đã có.
- Các mục còn lại được tải từ danh mục OCR để đủ phạm vi bài học; giao diện tạo bản nháp tóm tắt và câu hỏi luyện tập gợi ý theo môn học/chủ điểm.
- **Đây chưa phải bản số hóa hoàn chỉnh và được kiểm chứng độc lập cho từng bài.** Các câu hỏi đọc hiểu Tiếng Việt còn mang tính luyện kĩ năng chung; nội dung, đáp án, độ khó và trang nguồn cần giáo viên rà soát trước khi dùng chính thức.
- Website không đăng lại nguyên văn toàn bộ SGK; nội dung học nên là tóm tắt, giải thích và bài tập mới dựa trên kiến thức nguồn.

## Các thay đổi đã thực hiện
- Thêm quy trình OCR cho sáu PDF dạng ảnh quét.
- Tạo danh mục 168 mục với ID, tên bài, tập và khoảng trang nguồn.
- Cập nhật website để tải danh mục đầy đủ, tạo phần học tập nháp cho các mục còn thiếu và cập nhật số lượng theo môn.
- Cập nhật README và cảnh báo rõ về trạng thái bản nháp.
- Giữ chức năng hồ sơ học sinh, lưu tiến độ cục bộ, sao lưu JSON và khôi phục JSON.

## Việc còn cần hoàn thiện
1. Rà soát từng bài với trang nguồn OCR; sửa lỗi nhận dạng chữ, nhất là tiêu đề hoặc số trang bị OCR nhầm.
2. Thay các câu hỏi đọc hiểu chung bằng câu hỏi cụ thể đã đối chiếu với nội dung bài; kiểm tra mọi đáp án.
3. Hoàn thiện phần giảng giải, ví dụ và bài tập theo từng bài; không coi danh mục đủ tên là đồng nghĩa nội dung từng bài đã hoàn chỉnh.
4. Kiểm tra trên website sau khi GitHub Pages hoàn tất triển khai và thử luồng chọn môn, mở bài, làm câu hỏi, lưu/khôi phục tiến độ.

## Nguyên tắc hoàn thiện
Không tự bịa nội dung để lấp chỗ trống. Khi nguồn OCR chưa rõ hoặc đáp án chưa được xác minh, phải đánh dấu cần rà soát thay vì coi là nội dung chính thức.
