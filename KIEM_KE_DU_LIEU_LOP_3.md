# Kiểm kê dữ liệu và trạng thái website tự học lớp 3

## Trạng thái hiện tại
Website thử nghiệm đang phát triển trên nhánh `build-lop-3`. Nhánh `main` vẫn được giữ nguyên cho dự án lớp 2.

## Dữ liệu nguồn đã sao chép sang nhánh phát triển
Các tệp bàn giao được giữ nguyên trong thư mục `data/` để tiện kiểm tra và tiếp tục xử lý:
- Báo cáo phân tích 3 SGK.
- Kế hoạch số hóa website.
- Kho kiến thức của Toán 3, Tiếng Việt 3, Tiếng Anh 3.
- Mục lục CSV của cả ba môn.
- Bản đồ liên kết kiến thức JSON.
- Ngân hàng dạng bài tập tham khảo.
Xem [README dữ liệu](data/README.md).

## Phạm vi thực tế đang có trong website
| Môn học | Dữ liệu trong giao diện | Phạm vi toàn chương trình cần hướng tới |
|---|---:|---:|
| Toán 3 Kết nối tri thức | 6 bài | 81 bài |
| Tiếng Việt 3 Kết nối tri thức | 6 bài | 56 bài |
| Tiếng Anh 3 Global Success | Starter + Unit 1–4 | 20 units |
| **Tổng** | **17 mục học tập** | Chưa đủ |

Các kho kiến thức và mục lục nguồn cũng chưa đầy đủ cho toàn bộ năm học. Một số câu hỏi được soạn để tạo bản dùng thử; cần giáo viên rà soát nội dung và đáp án trước khi dùng chính thức. Không được suy diễn rằng nhãn trạng thái trong CSV có nghĩa toàn bộ SGK đã được kiểm chứng độc lập.

## Các thay đổi đã thực hiện
- Giữ giao diện học tập và các bài học hiện có, bổ sung cảnh báo rõ ràng rằng đây là bản dùng thử.
- Ghi rõ số bài hiện có và liên kết tới báo cáo kiểm kê.
- Bổ sung chức năng sao lưu tiến độ học sinh thành tệp JSON và khôi phục từ tệp đó.
- Cập nhật README và sao chép tài liệu nguồn sang nhánh phát triển.
- Thêm GitHub Actions workflow để kiểm tra cú pháp JavaScript và một số điều kiện cơ bản khi workflow được chạy.

## Giới hạn còn lại
1. Chưa có dữ liệu đầy đủ cho 81 bài Toán, 56 bài Tiếng Việt và 20 units Tiếng Anh.
2. Cần kiểm chứng từng bài với SGK gốc; đặc biệt các câu hỏi, đáp án, trang sách, chính tả và ngữ cảnh đọc hiểu.
3. Tiến độ hiện lưu bằng `localStorage` trên trình duyệt/thiết bị hiện tại; chưa có đồng bộ đám mây. Đã có chức năng sao lưu/khôi phục thủ công.
4. Chưa xác nhận GitHub Pages đã được cấu hình để xuất bản nhánh `build-lop-3`.

## Nguyên tắc hoàn thiện
Không tự bịa nội dung để lấp các bài còn thiếu. Bài nào chưa có nguồn đủ tin cậy phải được đánh dấu thiếu dữ liệu, hoặc chờ bổ sung nguồn SGK, rồi mới đưa vào bản phát hành chính thức.
