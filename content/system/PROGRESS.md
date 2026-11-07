# Batch 9 — trạng thái mới nhất, 07/11/2026

| Môn | AI biên soạn và kiểm tra | Tổng mục | Còn nháp |
|---|---:|---:|---:|
| Toán | 36 | 81 | 45 |
| Tiếng Việt | 0 | 62 | 62 |
| Tiếng Anh | 0 | 25 | 25 |
| Tổng | 36 | 168 | 132 |

- 1440 câu, 36 trò chơi. Giáo viên duyệt Toán 1–4; 32 bài chờ duyệt. Bài mới giữ AI_CHECKED_AWAITING_TEACHER.
- Batch 9: Toán 33–36, 160 câu riêng (mỗi bài 10/10/20), 4 trò chơi, 2 SVG mới; lượt luyện tập 10 câu 3/3/4. Bài 33–34 có hoạt động dụng cụ.
- Đã đọc trực quan trang in 91–98 (PDF 92–99) Toán tập 1: nhiệt độ, trải nghiệm đo lường, luyện tập chung, nhân ba chữ số. Số liệu nhiệt độ là mô phỏng học toán.
- validate_site.py/validate_content.py đạt: 36 bài, 1440 câu, 1366 đẳng thức lời giải. DOM 36 bài và test_batch7.py/test_batch8.py/test_batch9.py đạt. Hai SVG đã render và xem; chưa có Chromium để kiểm thử trình duyệt thật.
- Batch 8 đã xác minh commit e2ec25ed0b6472d889e9158ae1662c19eba0e60e; luồng Publish class 3 website to GitHub Pages thành công.
- Checkpoint tiếp: Toán 37–40; đọc nguồn và xác nhận trang theo danh mục trước khi biên soạn. Giữ thứ tự Toán → Tiếng Việt → Tiếng Anh.
- Kiểm thử: python scripts/validate_site.py; python scripts/test_batch7.py; python scripts/test_batch8.py; python scripts/test_batch9.py; npm test.

## Lịch sử trước Batch 9

# Batch 8 — trạng thái mới nhất, 07/11/2026

| Môn | AI biên soạn và kiểm tra | Tổng mục | Còn nháp |
|---|---:|---:|---:|
| Toán | 32 | 81 | 49 |
| Tiếng Việt | 0 | 62 | 62 |
| Tiếng Anh | 0 | 25 | 25 |
| Tổng | 32 | 168 | 136 |

- 1280 câu, 32 trò chơi. Giáo viên duyệt Toán 1–4; 28 bài chờ duyệt. Mọi bài mới giữ AI_CHECKED_AWAITING_TEACHER.
- Batch 8: Toán 29–32; 4 JSON, 4 Markdown, 160 câu riêng, 4 trò chơi, 3 SVG mới; ba bài đo lường có hoạt động thực hành với dụng cụ.
- Đọc trực quan toàn bộ trang in 83–90 (PDF 84–91) Toán tập 1. Nội dung: ôn nhân/chia/gấp/giảm/hai bước; mi-li-mét, gam, mi-li-lít.
- Kiểm tra dữ liệu/cú pháp, DOM 32 bài, hồi quy Batch 7 và 27 đáp án trọng yếu Batch 8 đạt. Đã render và xem cả 3 SVG. Chưa có Chromium để kiểm thử trình duyệt thật.
- Checkpoint tiếp: Toán 33–36, trang in 91–98; đọc nguồn trước khi biên soạn. Giữ thứ tự Toán → Tiếng Việt → Tiếng Anh.
- Lệnh kiểm tra: python scripts/validate_site.py; python scripts/test_batch7.py; python scripts/test_batch8.py; npm test.

## Lịch sử trước Batch 8

# Batch 7 — trạng thái mới nhất, 07/11/2026

- Toán: 28/81 bài có học liệu riêng; Tiếng Việt: 0/62; Tiếng Anh: 0/25. Tổng 28/168; còn 140 mục bản nháp.
- 1120 câu, 28 trò chơi. AI đã biên soạn/kiểm tra 28 bài; giáo viên đã duyệt 4 bài Toán 1–4; 24 bài chờ duyệt. Mọi bài mới giữ AI_CHECKED_AWAITING_TEACHER.
- Batch 7: Toán 25–28, 160 câu riêng (mỗi bài 10/10/20), 4 trò chơi; lượt luyện tập 10 câu phân mức 3/3/4.
- Đọc trực quan trang in 72–82 (PDF 73–83) Toán tập 1. Chủ đề: chia hết/có dư, chia hai chữ số, giảm số lần, toán hai bước.
- validate_site.py, validate_content.py, test_batch7.py và test_content_dom.cjs đạt trên toàn bộ 28 bài. npm ci tái lập thành công. Chưa có Chromium để kiểm thử trình duyệt thật.
- Checkpoint kế tiếp: Toán 29–32, trang in 83–90. Đọc nguồn trước khi biên soạn; tiếp tục Toán rồi Tiếng Việt rồi Tiếng Anh.
- Kiểm thử: npm ci; npm test; python scripts/validate_site.py; python scripts/test_batch7.py.

## Lịch sử trước Batch 7

## Cập nhật kiểm thử — 07/11/2026

Đã bổ sung package.json và package-lock.json để tái lập kiểm thử bằng `npm ci` rồi `npm test`, thay cho phụ thuộc jsdom trong thư mục tạm. Đã chạy thành công trên toàn bộ 24 bài hiện có. Số học liệu vẫn là 24 bài Toán, 960 câu; chưa tạo Batch 7. Checkpoint nội dung kế tiếp giữ nguyên Toán 25–28.

# Trạng thái mới nhất — Batch 6, 07/11/2026

| Môn | Có học liệu riêng | Tổng danh mục | Còn bản nháp |
|---|---:|---:|---:|
| Toán | 24 | 81 | 57 |
| Tiếng Việt | 0 | 62 | 62 |
| Tiếng Anh (gồm Starter/Review) | 0 | 25 | 25 |
| Tổng | 24 | 168 | 144 |

- **960 câu, 24 trò chơi theo bài.** Toán 1–4 đã được thầy thẩm định; Toán 5–24 do AI biên soạn/rà soát và chờ thẩm định.
- Batch 6: Toán 21–24, 160 câu, 4 trò chơi và 5 SVG mới. Đã đọc trực quan toàn bộ trang in 63–71 (PDF 64–72).
- Học liệu phân biệt mặt/cạnh/đỉnh và bộ phận bị khuất; ôn hình học; nhân số hai chữ số có/không nhớ trong phạm vi 100; gấp số lần khác thêm đơn vị, tổng và chênh lệch.
- Kiểm tra 24 bài/960 câu, 824 đẳng thức trong lời giải, cú pháp và DOM: đạt. Đã render và xem cả 5 SVG mới. Chưa kiểm thử bố cục toàn website/âm thanh/cảm ứng bằng trình duyệt thật.
- GitHub Pages của Batch 5 đã hoàn tất thành công: commit d25f25641fe3d2d685c0667d372538f05d9034de, workflow run 42379465425.
- Batch kế tiếp: **Toán 25–28**, dự kiến trang in **72–82**. Đọc nguồn cho phép chia có dư, chia số hai chữ số, giảm số lần và bài toán hai bước trước khi biên soạn.
- Giữ thứ tự Toán → Tiếng Việt → Tiếng Anh. Mỗi batch phải kiểm tra và commit riêng, giữ dữ liệu tiến độ và các xác nhận đã có.
- Kiểm tra: `python scripts/validate_site.py`; nếu có jsdom: `NODE_PATH=/tmp/class3-test/node_modules node scripts/test_content_dom.cjs`.

## Lịch sử trước Batch 6

# Trạng thái mới nhất — Batch 5, 07/11/2026

| Môn | Có học liệu riêng | Tổng danh mục | Còn bản nháp |
|---|---:|---:|---:|
| Toán | 20 | 81 | 61 |
| Tiếng Việt | 0 | 62 | 62 |
| Tiếng Anh (gồm Starter/Review) | 0 | 25 | 25 |
| Tổng | 20 | 168 | 148 |

- **800 câu, 20 trò chơi theo bài.** Thầy đã thẩm định Toán 1–4; Toán 5–20 chờ thẩm định.
- Batch 5: Toán 17–20, 160 câu, 4 trò chơi, 6 SVG mới. Đã đọc trực quan toàn bộ trang in 52–62 (PDF 53–63).
- Sửa lỗi OCR: Bài 18 đúng trang 54–55, Bài 19 đúng trang 56–60. Đã cập nhật danh mục nguồn và dẫn trang trong học liệu.
- Bài 20 có hướng dẫn thực hành trên giấy cùng lưới vẽ tương tác: chữ nhật 4 ô × 2 ô, vuông cạnh 3 ô, đường tròn bán kính 2 ô, góc vuông. Hỗ trợ chọn điểm bằng chuột/phím; phân biệt ô mô phỏng với cm thật; không cộng XP từ lưới vẽ.
- Trò ghép đôi nay luôn kèm hình/bảng nếu một câu được chọn cần tham chiếu; không để mất dữ kiện do giao diện ghép đôi.
- Kiểm tra 20 bài/800 câu, 671 đẳng thức trong lời giải, cú pháp và kiểm thử DOM: đạt. Đã render và xem 6 SVG. Chưa kiểm thử bố cục toàn trang, âm thanh và cảm ứng trên trình duyệt thật.
- Batch kế tiếp: **Toán 21–24**, dự kiến trang in **63–71**; phải đối chiếu PDF trước khi ghi nguồn.
- Tiếp tục theo thứ tự Toán → Tiếng Việt → Tiếng Anh; không đánh dấu phần mới được giáo viên duyệt.

## Lịch sử trước Batch 5

# Trạng thái mới nhất — Batch 4, 07/11/2026

## Phạm vi đã lưu

| Môn | Có học liệu riêng | Tổng danh mục | Còn bản nháp |
|---|---:|---:|---:|
| Toán | 16 | 81 | 65 |
| Tiếng Việt | 0 | 62 | 62 |
| Tiếng Anh (gồm Starter/Review) | 0 | 25 | 25 |
| Tổng | 16 | 168 | 152 |

- Ngân hàng mới: **640 câu, 16 trò chơi theo bài**.
- Thầy Nguyễn Thế Khanh đã thẩm định **Toán 1–4**. **Toán 5–16** được AI biên soạn/rà soát, chờ thầy thẩm định.
- Batch 4: Toán 13–16, 160 câu, 4 trò chơi; đã đọc trực quan trang in 39–51 (PDF 40–52).
- Năm SVG mới do AI dựng cho Bài 14 và 16; đã render PNG và xem trực quan, không tràn chữ hay sai nhãn. Các câu tham chiếu hình tự hiển thị hình ngay trong câu hỏi.
- Kiểm tra 16 bài, 640 câu và tính lại 633 đẳng thức số: đạt. Kiểm thử DOM đạt; chưa có kiểm thử bố cục toàn website/âm thanh bằng trình duyệt thật.
- Đã thiết lập tác vụ nối tiếp mỗi giờ theo yêu cầu làm khi thầy nghỉ; tác vụ phải đọc main mới nhất rồi tiếp tục, không dùng số liệu lịch sử làm trạng thái hiện tại. Thứ tự: hoàn thiện Toán → Tiếng Việt → Tiếng Anh. Không cam kết đủ 168 mục trước sáng hôm sau.
- Batch tiếp theo: **Toán 17–20**, trang in **52–62**. Cần hình mới cho tâm/bán kính/đường kính, góc và các tứ giác; giữ đúng kiến thức từng bài.
- Mỗi batch phải commit thành công và xác minh trước khi chuyển batch; không gộp hàng loạt bản nháp rồi đánh dấu hoàn thành.
- Kiểm tra: `python scripts/validate_site.py`; kiểm thử DOM: `NODE_PATH=/tmp/class3-test/node_modules node scripts/test_content_dom.cjs` nếu đã cài jsdom.

## Lịch sử trước Batch 4

# Trạng thái mới nhất — Batch 3, 07/11/2026

- Danh mục: **168 mục**.
- Học liệu riêng: **12 bài Toán, 480 câu, 12 trò chơi theo bài**.
- Đã được giáo viên thẩm định: **4 bài Toán 1–4** (Batch 1).
- Chờ giáo viên thẩm định: **8 bài Toán 5–12**, AI đã biên soạn và rà soát (Batch 2 và 3).
- Còn **156 mục bản nháp** chưa được biên soạn và kiểm tra theo chuẩn mới.
- Batch 3: Toán 9–12, 160 câu, 4 trò chơi; đọc trực quan trang in 28–38 (PDF 29–39).
- Bài 12 có bảng tra nhân/chia 2–9, hiển thị cả trong phần học và câu hỏi cần tra bảng; bảng có bản Markdown tương ứng.
- Kiểm tra 12 bài và tính lại 495 đẳng thức số trong lời giải: đạt. Cú pháp JavaScript và DOM đạt; chưa có kiểm thử bố cục bằng Chromium.
- Workflow GitHub Pages của Batch 2 đã thành công (commit d69e28c8c4c3696f8bb49af245e14e4108545b1f). Trạng thái triển khai Batch 3 xem trong Actions theo commit mới.
- Batch tiếp theo: Toán 13–16, trang in 39–51. Bài 16 cần hình minh họa mới cho điểm ở giữa và trung điểm; không dùng ảnh SGK chưa đính kèm vào câu hỏi.
- Lệnh kiểm tra: `python scripts/validate_site.py`; `NODE_PATH=/tmp/class3-test/node_modules node scripts/test_content_dom.cjs` (cần cài jsdom). Lệnh cũ `test_batch1_dom.cjs` gọi lại bộ kiểm thử hiện hành.
- Mỗi script build tự cập nhật INDEX.json và giữ xác nhận trong APPROVALS.json; không tự đánh dấu giáo viên duyệt các batch mới.

## Lịch sử trước Batch 3

# Trạng thái mới nhất — Batch 2, 07/11/2026

- Tổng danh mục: 168 mục.
- Học liệu riêng đã biên soạn và AI kiểm tra: **8 bài, 320 câu, 8 trò chơi**.
- Giáo viên Nguyễn Thế Khanh đã xác nhận thẩm định: **4 bài Batch 1** (Toán 1–4). Ghi nhận tại APPROVALS.json; JSON, Markdown và giao diện đã đồng bộ.
- Batch 2: Toán 5–8, **160 câu, 4 trò chơi**, chờ giáo viên thẩm định.
- Còn 160 mục ở trạng thái bản nháp, chưa được biên soạn/kiểm tra theo chuẩn mới.
- Nguồn Batch 2: đã đọc trực quan trang in 16–27 của Toán tập 1 (PDF 17–28).
- Trò chơi: Bài 5 ghép 5 cặp có đáp án khác nhau; Bài 6 tính nhanh 60 giây; Bài 7 mở rương; Bài 8 đúng/sai. Nút chơi lại giữ đúng bài.
- Bộ tải nay dùng INDEX.json để tự nhận những bài có tệp học liệu; một tệp lỗi không chặn các bài khác.
- Bài 7 có 2 hình SVG do AI dựng, được tham chiếu ngay trong câu hỏi; không sao chép hình SGK.
- Kiểm tra dữ liệu, cú pháp, luồng DOM và phép tính: đạt. Chưa có kiểm thử bố cục/âm thanh bằng Chromium.
- Batch kế tiếp: Toán 9–12, trang in 28–38; chỉ chuyển sang sau khi Batch 2 đã được commit thành công.
- Chạy lại học liệu: `python scripts/build_batch1.py`, `python scripts/build_batch2.py`; các bước này tự đồng bộ sổ duyệt và chỉ mục. Kiểm tra: `python scripts/validate_site.py`.

## Lịch sử trước Batch 2

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
