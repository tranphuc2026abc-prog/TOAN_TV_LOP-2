# Tự học lớp 3 – Hành trình tri thức

Bản dùng thử đang phát triển trên nhánh `build-lop-3`; nhánh `main` được giữ nguyên cho website lớp 2.

## Chức năng hiện có
- Giao diện thân thiện với học sinh tiểu học, chia thành Toán 3, Tiếng Việt 3 và Tiếng Anh 3.
- Hồ sơ theo tên học sinh, câu hỏi luyện tập, thử thách tổng hợp, sao, XP và huy hiệu.
- Lưu tiến độ trên trình duyệt bằng `localStorage`.
- **Sao lưu tiến độ ra tệp JSON và khôi phục từ tệp JSON** trong mục Hồ sơ & tiến độ.
- Sao lưu trang chủ cũ tại `archive/index-lop2-backup.html`.
- Bộ tài liệu nguồn được giữ trong thư mục `data/`.

## Phạm vi dữ liệu đang có trong giao diện
- Toán 3: 6 bài.
- Tiếng Việt 3: 6 bài.
- Tiếng Anh 3 Global Success: Starter và Unit 1–4.
- Tổng: 17 mục học tập.

Đây là bản thử nghiệm, chưa bao phủ toàn bộ chương trình Toán 3 (81 bài), Tiếng Việt 3 (56 bài) và Tiếng Anh 3 (20 units). Một số câu hỏi do AI soạn và cần giáo viên rà soát đáp án, độ phù hợp lứa tuổi và đối chiếu SGK trước khi dùng chính thức. Không coi phần trăm tiến độ trong ứng dụng là tiến độ của cả năm học.

## Kiểm kê dữ liệu
Xem [KIEM_KE_DU_LIEU_LOP_3.md](KIEM_KE_DU_LIEU_LOP_3.md) để biết rõ những gì đã có và phần còn thiếu.

## Giới hạn lưu tiến độ
Tiến độ chỉ lưu trên trình duyệt và thiết bị hiện tại, chưa có đồng bộ đám mây. Hãy dùng chức năng sao lưu JSON trước khi đổi thiết bị hoặc xóa dữ liệu trình duyệt.
