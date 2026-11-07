# Rà soát học liệu — 07/11/2026

## Bằng chứng và phạm vi

- Đã đọc README.md, KIEM_KE_DU_LIEU_LOP_3.md, danh mục JSON, index.html và cây thư mục main.
- Kho có sáu PDF; bản đính kèm được dùng để đọc Batch 1. Chưa kiểm tra hash đối chiếu từng PDF đính kèm với kho.
- Không có tệp OCR toàn văn trong cây kho hiện tại. Báo cáo cũ nói OCR 716 trang được giữ trong artifact tạm; chưa truy cập được artifact đó.
- Danh mục JSON chứa 81 + 62 + 20 + 5 = 168 mục. Báo cáo cũ ghi “6 mục” Tiếng Anh bổ sung nhưng Starter + Review 1–4 chỉ là 5; đã sửa lỗi đếm đó. Chưa đối chiếu lại toàn bộ mục lục sáu PDF.

## Hiện trạng

- Các bài cũ có mẫu hoặc nội dung tự động; không đủ cơ sở công nhận hoàn thiện từng bài.
- INDEX.json phân loại 164 mục BẢN NHÁP và 4 mục CẦN RÀ SOÁT (AI đã kiểm tra, chờ giáo viên).
- question_count=null cho bài chưa kiểm kê ngân hàng riêng, không có nghĩa website không có câu hỏi.
- Website cũ tái sử dụng seed để tạo 12 nhiệm vụ; Batch 1 thay bằng 40 câu riêng/bài.
- Đường dẫn danh mục trên giao diện còn trỏ kho tên cũ; đã sửa về TOAN_TV_TA_LOP3.

## Batch 1: Toán tập 1, Bài 1–4

- Đọc trực quan tất cả trang in 6–15 (PDF 7–16); không đăng nguyên văn SGK.
- 160 câu mới, mỗi bài phân mức 10 nhận biết, 10 thông hiểu, 20 vận dụng.
- Có trắc nghiệm và điền đáp án; không tự tuyên bố có câu đúng/sai trong kho mới.
- Mỗi bài có mục tiêu, khám phá, quy tắc, cách học, ví dụ, lỗi thường gặp, trò chơi và đánh giá.
- Đáp án được AI rà soát; các phép tính và cách giải đã đọc lại. Kiểm tra tự động cấu trúc không thay thế thẩm định sư phạm.
- Không có xác nhận của giáo viên cho nội dung mới.

## Kết quả kỹ thuật

- JSON hợp lệ; 160 mã câu duy nhất, không trùng nguyên văn câu trong từng bài, không thiếu đáp án/lời giải.
- Mỗi MCQ có bốn phương án khác nhau và có đáp án trong phương án.
- Node kiểm tra cú pháp bộ tải: đạt.
- test_batch1_dom.cjs: đạt luồng 168 bài, bốn kho câu hỏi, lượt 10 câu phân mức 3/3/4, tám lượt xáo trộn khác bộ, trả lời/chấm điểm/lời giải, chặn chấm lại câu đã xong, bốn trò chơi theo bài, lưu/nạp hồ sơ, một tệp JSON lỗi 404 vẫn giữ bài cũ.
- Chưa chạy được test_batch1.cjs bằng Chromium do thiếu executable và tải Chromium không thành công. Chưa xác nhận bố cục, thao tác cảm ứng, âm thanh, tải tệp sao lưu/khôi phục bằng giao diện thực tế và trạng thái Pages sau commit.
- Bộ tải có lỗi độc lập từng tệp; dữ liệu cũ vẫn dùng được khi tệp mới không tải được. Không thay khóa lưu tiến độ.

## Cần theo dõi

1. Giáo viên rà soát nội dung, độ khó và phương án nhiễu của Batch 1.
2. Kiểm thử trình duyệt sau triển khai, gồm hồ sơ, sao lưu/khôi phục và màn hình điện thoại.
3. Đối chiếu lại mục lục và khoảng trang cho các bài sau; một số khoảng đang bao gồm phần ôn tập xen giữa.
4. Hoàn thiện 164 mục còn lại theo batch; không đánh dấu hoàn thành dựa vào tên bài có trên giao diện.

## Cập nhật Batch 2 — 07/11/2026

- Ghi nhận xác nhận thực tế của giáo viên cho Batch 1. Chỉ 4 bài 1–4 được gắn TEACHER_APPROVED; 4 bài mới chưa được duyệt.
- Toán 5–8: đọc toàn bộ trang in 16–27, biên soạn 160 câu mới có phương án nhiễu riêng, lời giải; 4 kiểu trò chơi theo đúng phạm vi từng bài.
- Bài 7: 2 sơ đồ SVG có mô tả tiếp cận và chú thích; dữ kiện câu hỏi đủ, không dựa vào hình SGK không được đính kèm.
- Đã loại bỏ bộ tải cứng 4 tệp, chuyển sang chỉ mục. Bộ tải kiểm tra ID, câu hỏi, đáp án, lựa chọn trước khi dùng; khi lỗi giữ bài cũ.
- Sửa nút làm lại để vẫn lấy 10 câu thay vì toàn bộ 40 câu. Chơi lại mini game giữ phạm vi bài. Ghép đôi dùng 5 đáp án khác nhau để tránh ghép mơ hồ.
- Kiểm thử DOM cho 8 bài: phân mức 3/3/4, xáo trộn 8 lần, đáp án/lời giải, chặn chấm lặp, cả bốn kiểu chơi, hình ngay trong câu hỏi, trạng thái thẩm định, lưu/nạp hồ sơ, fallback khi 404: đạt.
- Tính lại độc lập 291 đẳng thức số trong lời giải của 8 bài: đạt. Các khẳng định bằng chữ và độ phù hợp sư phạm vẫn cần giáo viên kiểm tra.
- Tích hợp kiểm tra JSON, chỉ mục, hình, cú pháp JavaScript ngoài HTML và đẳng thức vào validate_site.py, là bước kiểm tra của workflow Pages hiện có.
- Hạn chế còn giữ: chưa kiểm thử bố cục/âm thanh/tải sao lưu/khôi phục trên trình duyệt thật; không tự tuyên bố đã hoàn thành toàn bộ 168 mục.

## Cập nhật Batch 3 — 07/11/2026

- Đọc trực quan trang in 28–38 (PDF 29–39), đối chiếu nội dung bảng nhân/chia 6, 7, 8, 9 và bảng tra chung.
- Thêm 160 câu mới, mỗi bài phân mức 10/10/20, có lời giải và phương án nhiễu riêng; đã rà soát phép tính và ngữ nghĩa của đề. Không sao chép hệ thống bài tập SGK.
- Bài 12 có bảng nhân/chia HTML chính xác; các câu hỏi tham chiếu bảng tự hiển thị bảng trong bài kiểm tra và trò chơi. Bảng được lưu cùng JSON và Markdown.
- Chỉ mục hiện có 12 bài riêng: 4 bài đã thẩm định, 8 bài chờ thẩm định, 156 bản nháp.
- Toàn bộ 480 câu qua kiểm tra JSON, ID, phân mức, đáp án, lựa chọn, lời giải, tài liệu Markdown và trạng thái duyệt. Tính lại 495 đẳng thức số trong lời giải: đạt.
- Bộ kiểm thử DOM mở rộng theo chỉ mục thay vì số bài cố định: 12 bài, 8 lượt xáo trộn/bài, phân mức 3/3/4, làm lại giữ 10 câu, bốn kiểu trò chơi và phạm vi bài, hình và bảng tham chiếu, lưu/nạp hồ sơ, một file 404: đạt. Đã kiểm tra đúng sau một lần sai được nửa điểm và hiện lời giải sau hai lần sai.
- Tên bộ kiểm thử hiện hành: scripts/test_content_dom.cjs; tên cũ gọi lại bộ hiện hành. Không tuyên bố đã kiểm thử trình duyệt thật.
- Workflow Publish class 3 website to GitHub Pages của Batch 2 đã hoàn tất thành công (run 42376240072). Kiểm tra triển khai Batch 3 sau khi commit.
