# Tiến độ kho học liệu lớp 3

## Cập nhật ngày 07/11/2026 — Batch 1

- Danh mục hiện có: 168 mục (81 Toán, 62 Tiếng Việt, 20 Unit, Starter và 4 Review).
- Đã biên soạn và AI rà soát: 4 bài Toán đầu tiên, 160 câu, 4 trò chơi theo bài.
- Giáo viên đã xác nhận hoàn thiện: 0 bài. Không tự gán xác nhận của giáo viên.
- Còn 164 mục chưa được biên soạn và kiểm tra theo chuẩn mới; giao diện vẫn giữ bài mẫu/bản nháp cũ.
- Mỗi bài Batch 1 có 10 câu nhận biết, 10 thông hiểu, 20 vận dụng; JSON và Markdown riêng.
- Luyện tập tổng hợp: 10 câu/lượt theo phân bố 3/3/4. Trắc nghiệm và điền đáp án có chế độ riêng.
- Batch 1: đã lưu trong cùng commit với tệp này. Xem lịch sử GitHub của tệp để lấy SHA, không tự ghi SHA phỏng đoán.
- Batch tiếp theo: Toán 3 tập 1, Bài 5–8; đọc trang 16–27 trước khi biên soạn.

## Phạm vi kiểm tra

Đã kiểm tra cấu trúc 168 mục; chưa đối chiếu lại toàn bộ sáu mục lục PDF và từng trang của 164 bài còn lại. Số 168 là phạm vi danh mục hiện tại, không phải tuyên bố đã số hóa hoàn chỉnh.

Batch 1 đã đọc trực quan trang in 6–15 của sách Toán tập 1 (trang PDF 7–16). Đã kiểm tra JSON, ID, phân mức, đáp án và lời giải. Kiểm thử DOM/JavaScript đạt; Chromium không có sẵn và tải không thành công nên chưa xác nhận giao diện thực tế trên máy tính/điện thoại hay triển khai Pages.

## Tiếp tục

1. Đọc INDEX.json, PROGRESS.md và AUDIT_REPORT.md.
2. Đối chiếu sách cho Bài 5–8; không dùng mẫu thay tên bài.
3. Tạo JSON và Markdown theo Batch 1, kiểm tra nội dung và đáp án.
4. Mở rộng bộ tải học liệu (hiện tải bốn tệp Batch 1), cập nhật chỉ mục và kiểm thử.
5. Commit trực tiếp main sau khi kiểm tra nhánh chưa có thay đổi mới.

## Quay lui

Revert commit Batch 1 sẽ khôi phục mã và học liệu trước đó. Không đổi ID bài, khóa localStorage hay dữ liệu tiến độ người học.
