## Batch 8 — Toán 29–32, 07/11/2026

- Nguồn thực đọc: bản PDF Toán tập 1 sẵn trong môi trường, trang PDF 84–91 (trang in 83–90), đã render và đọc trực quan cả 8 trang. Chưa xác minh hash bản đính kèm với bản trong repo.
- Biên soạn 4 JSON/Markdown, 160 câu riêng, 4 trò chơi (kho báu, ghép cặp, đúng/sai), 3 SVG mới: thước chia từng mm với đầu A lệch 0; cân thăng bằng có ba quả cân; ca nước chia vạch 100 ml. Hình hiển thị ngay trong mọi câu phụ thuộc hình. Đã render và xem cả 3 hình, không dùng ảnh SGK.
- Có hướng dẫn, mục tiêu, lỗi thường gặp, ví dụ giải, phản hồi, đánh giá, hoạt động dụng cụ cho bài 30–32. Dữ kiện và bài tập mới, không chép hệ thống bài tập SGK.
- validate_site.py/validate_content.py: 32 bài, 1280 câu, 1193 đẳng thức số được tính lại; ID, lựa chọn, đáp án, phân mức 10/10/20, Markdown, hình, game và trạng thái đạt.
- test_batch8.py: 160 câu không trùng nguyên văn giữa batch; 27 đáp án trọng yếu và các phép tính độc lập về chia lấy số hộp, thước lệch 0, tổng quả cân, khối lượng trừ khay, nước tràn. test_batch7.py vẫn đạt.
- test_content_dom.cjs: toàn bộ 32 bài đạt, 10 câu/lượt 3/3/4, thay bộ, chấm điểm, chống chấm lặp, 4 loại game, hình/bảng/lưới vẽ cũ, lưu nạp wl3, fallback khi một JSON lỗi. Không đổi renderer hay khóa lưu trữ.
- Chưa có Chromium: chưa kiểm thử bố cục, cảm ứng và âm thanh bằng trình duyệt thật. AI kiểm tra không thay thẩm định giáo viên.
- Tổng 32/168 mục có học liệu riêng, 1280 câu, 32 trò chơi; giáo viên duyệt 4, chờ duyệt 28; còn 136 mục nháp. Checkpoint Toán 33–36 trang 91–98.

## Batch 7 — Toán 25–28, 07/11/2026

- Nguồn đã đọc trực quan: PDF Toán tập 1 sẵn trong môi trường, trang PDF 73–83 / trang in 72–82. Chưa xác minh hash với bản PDF trong repo.
- 4 JSON và 4 Markdown riêng; 160 câu và phương án nhiễu biên soạn riêng; 4 trò chơi theo bài. Các câu mới đủ dữ kiện chữ, không phụ thuộc hình ngầm, không cần hình hình học. Không sao chép hệ thống bài tập SGK.
- Rà soát số dư bé hơn số chia, phép kiểm tra bằng nhân cộng phần dư; phân biệt số nhóm đầy với số chỗ chứa hết; hạ chục dư; lượng còn lại với lượng đem dùng; trung gian với đáp số cuối.
- Kiểm tra toàn bộ 28 bài/1120 câu: JSON, ID, trùng câu trong bài, lựa chọn, đáp án, lời giải, Markdown, hình cũ, game và trạng thái đạt. Tính lại 1017 đẳng thức số. test_batch7.py kiểm tra 22 đáp án trọng yếu và hai cặp tình huống số dư/giảm số lần.
- DOM toàn bộ đạt: 10 câu 3/3/4, thay bộ, chấm điểm, 4 chế độ chơi, hồi quy hình/bảng/vẽ, lưu/nạp wl3 và fallback file lỗi. npm ci thành công.
- Chưa có Chromium: chưa kiểm thử bố cục, cảm ứng, âm thanh bằng trình duyệt thật. AI kiểm tra không thay giáo viên thẩm định.
- Tổng 28/168 có học liệu riêng; 1120 câu, 28 trò chơi; giáo viên duyệt 4, chờ duyệt 24; còn 140 mục nháp. Tiếp Toán 29–32.

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

## Cập nhật Batch 4 — 07/11/2026

- Nguồn: đọc trực quan toàn bộ trang in 39–51, gồm tìm thành phần trong nhân/chia, một phần mấy, ôn tập và điểm ở giữa/trung điểm.
- Biên soạn 160 câu có lời giải và phương án nhiễu riêng, 4 trò chơi; thêm 5 SVG có mô tả tiếp cận, render và xem cả 5 PNG để kiểm tra nhãn và dữ kiện.
- Đã rà soát phạm vi kiến thức: bỏ phép nhân hai chữ số chưa học trong tháp tích, giữ phép tính trong các bảng đã học; các bài tính nửa đoạn dùng số phù hợp bảng chia 2 đã học.
- Hai câu Bài 14 và năm câu Bài 16 có tham chiếu SVG, được kiểm tra hiện đúng tệp hình trong luồng làm bài.
- Tổng 16 bài, 640 câu qua validator; 633 đẳng thức số trong lời giải được tính lại. Kiểm thử DOM theo chỉ mục, gồm các hình mới: đạt.
- Giáo viên chỉ xác nhận Batch 1; không mở rộng xác nhận đó cho các batch khác. Hiện 4 bài đã thẩm định, 12 bài chờ thẩm định, 152 mục bản nháp.
- Đã thiết lập tác vụ tiếp tục tự động theo thứ tự Toán, Tiếng Việt, Tiếng Anh; mỗi lượt phải đọc checkpoint và xác minh commit thực tế, không giả báo hoàn thành.
- Giữ giới hạn: kiểm thử DOM không xác nhận thao tác cảm ứng, bố cục toàn trang, giọng đọc và tải tệp sao lưu/khôi phục bằng trình duyệt thật.

## Cập nhật Batch 5 — 07/11/2026

- Đã đọc toàn bộ trang in 52–62; xác định OCR lệch ranh giới Bài 18/19: Bài 18 kết thúc ở 55, Bài 19 bắt đầu ở 56. Sửa danh mục CHUONG_TRINH_LOP_3_FULL.json và dẫn trang; không sửa số lượng danh mục.
- Toán 17–20 có 160 câu mới (10/10/20 mỗi bài), 4 trò chơi, kiến thức, ví dụ, lỗi thường gặp và lời giải. Bài 20 có ba hoạt động thực hành bằng dụng cụ, tiêu chí tự kiểm tra và lưới vẽ tương tác.
- Sáu SVG mới được dựng bằng tọa độ, render và xem trực quan: hình tròn với đường kính/bán kính/đoạn không qua tâm; ba góc; góc vuông xoay nghiêng; tam giác/chữ nhật/vuông; tứ giác cạnh bằng nhưng không vuông; lưới hình chữ nhật/vuông. Đã chỉnh nhãn nhóm góc để không lẫn với tên điểm.
- Kiểm tra toàn bộ 800 câu, ID, lựa chọn, lời giải, Markdown, hình và trạng thái duyệt: đạt. Tính lại 671 đẳng thức số trong lời giải: đạt.
- DOM hồi quy 20 bài và bốn loại game: đạt. Kiểm tra lưới vẽ có tám trường hợp đúng/sai cho bốn kiểu hình, góc vuông xoay nghiêng, đường tròn vượt lưới, chọn trùng điểm, xóa nét và chọn bằng phím/chuột: đạt. Vùng chọn chấm được mở rộng để dễ thao tác.
- Sửa thiếu dữ kiện ở trò ghép đôi: câu cần hình/bảng có phần tham chiếu chung hiển thị ngay trên màn chơi; đã kiểm thử với Bài 19 và bảng của Bài 12.
- Giới hạn: DOM và render SVG không thay thế kiểm thử bố cục toàn website, thao tác cảm ứng hay âm thanh bằng trình duyệt thật. Chỉ Bài 1–4 đã được giáo viên xác nhận.

## Cập nhật Batch 6 — 07/11/2026

- Đã đọc trực quan toàn bộ trang in 63–71 (PDF 64–72) cho Bài 21–24. Không thay đổi số lượng danh mục; các mốc nguồn của bốn bài khớp PDF.
- Biên soạn 160 câu, phân mức 10/10/20 mỗi bài, đáp án/lời giải và phương án nhiễu riêng; thêm 4 trò chơi. Nhân hai chữ số có hướng dẫn thẳng hàng, tính đơn vị trước, nhớ sang chục và ví dụ không vượt phạm vi bài.
- Câu gấp số lần có phân biệt thêm đơn vị, xác định số ban đầu, số phần trên sơ đồ, kiểm tra cách lập phép tính, tìm tổng và chênh lệch; không chỉ đổi số trong cùng một mẫu.
- Năm SVG mới: mô hình lập phương và hộp chữ nhật đủ cạnh/đỉnh khuất; trung điểm bốn cạnh hình vuông; đường tròn vừa khít hình vuông; sơ đồ số thẻ gấp ba. Đã render và xem cả năm hình; nhãn rõ, không cắt chữ.
- Validator đạt cho toàn bộ 24 bài, 960 câu. Tính lại 824 đẳng thức số trong lời giải: đạt. Bài 21 dùng phép cộng đã học nếu cần cộng 12 cạnh của hai khung, không yêu cầu thuật toán nhân hai chữ số trước Bài 23.
- DOM hồi quy 24 bài, 10 câu phân mức 3/3/4, chấm điểm/lời giải, bốn kiểu trò chơi, hình trong câu hỏi và ghép đôi, lưới vẽ, lưu/nạp tiến độ, fallback 404: đạt. Bổ sung kiểm thử ghép đôi với sơ đồ của Bài 24.
- Kiểm thử Chromium chưa thực hiện vì môi trường chưa có executable. Bộ kiểm thử trình duyệt đã sửa để lấy số học liệu từ chỉ mục thay vì hằng số cũ.
- Workflow Pages Batch 5 thành công (run 42379465425). Batch 6 cần xác minh theo commit thực tế sau khi ghi.
- Trạng thái duyệt giữ nguyên: 4 bài đã được giáo viên thẩm định; 20 bài mới chờ thẩm định; 144 mục còn bản nháp.

## Kiểm tra khả năng tái lập — 07/11/2026

- Kiểm tra lại main và các tệp tiến độ/chỉ mục/duyệt/mã ứng dụng trước khi thao tác.
- validate_site.py đạt: 168 mục, 24 bài riêng, 960 câu, 824 đẳng thức số.
- Phát hiện thư mục jsdom tạm không còn. Đã bổ sung package.json, package-lock.json với phiên bản jsdom thực tế đã kiểm tra và .gitignore cho node_modules.
- Đã chạy npm ci và npm test từ bộ phụ thuộc được khóa: DOM hồi quy 24 bài đạt. Không thay đổi số bài hoặc gán thêm xác nhận giáo viên. Chưa biên soạn Batch 7; tiếp tục Toán 25–28.
- Chưa kiểm thử Chromium; không suy diễn DOM thành kiểm thử trình duyệt thật.
