Autotik HNC 1.0.19 sửa hàng đợi bị giữ sau lỗi trước khi gửi bài đăng.

- Trước đây hàng đợi chuyển UPLOADING trước khi kiểm tra proxy/mở GPM, nhưng nhánh giữ video để thử lại chỉ xử lý PROCESSING. Lỗi proxy/GPM có thể khiến lượt sau bị chặn vĩnh viễn.
- Ghi nhận đã vào bước bấm Đăng trước khi thực hiện thao tác. Chỉ trả UPLOADING về PENDING khi kết quả có xác nhận chưa vào bước gửi bài. Lỗi trước bước này giữ video đã render, thử lại sau 15 phút, không tải/render lại. Hết phiên đăng nhập/CAPTCHA vẫn yêu cầu xử lý.
- Lỗi sau khi vào bước gửi bài, ngoại lệ không rõ giai đoạn hoặc kết quả cũ thiếu thông tin đều giữ chờ xác minh; không suy đoán an toàn từ chữ timeout/proxy. Dọn lỗi worker không đổi UPLOADING thành FAILED; dọn cache giữ file của bài chờ xác minh.
- Kết nối CDP chờ tối đa 45 giây và dùng context sẵn có của GPM; toàn bộ phiên đăng giới hạn 15 phút, kết thúc có kiểm soát để nhả lượt.
- FFmpeg có giám sát riêng: 5 phút không có thời gian media tiến lên thì dừng đúng tiến trình worker đang sở hữu, kể cả FFmpeg không xuất log. Có giới hạn tổng thời gian theo độ dài video. Không dừng FFmpeg ngoài app.
- Bao gồm sửa đồng bộ proxy GPM Global của 1.0.18 và kết nối CDP Auto Login. Giữ core trong AppData, dữ liệu/license và lịch đăng do người dùng đặt.

Sau cập nhật: dừng tác vụ, đóng/mở lại app để nạp code; sau đó chủ động Chạy các tài khoản cần chạy. PROCESSING dở dang được cơ chế khởi động hiện có đưa lại hàng đợi. UPLOADING chưa rõ kết quả vẫn giữ để đối chiếu trên TikTok; cập nhật không tự xác nhận video chưa đăng và không tự khởi chạy tài khoản.

Kiểm chứng: 39 ca trên mã nguồn bản khách (SQLite tạm, lỗi proxy/GPM, timeout trước/sau bấm Đăng, CDP, tiến trình im lặng/hủy và video FFmpeg mẫu) đạt. EXE có 90 module khách đã đối chiếu bytecode, khởi động với license/dữ liệu tạm được; GPM Global API mô phỏng chỉ đọc, không ghi profile. Chưa có nhật ký của khách 1.0.17, chưa đo chạy cả ngày trên máy khách và chưa đăng lên tài khoản thật; không cam kết số video/ngày hoặc giải quyết mọi nguyên nhân chậm. Chỉ tiêu mỗi ngày/khoảng cách đăng vẫn theo cấu hình.
