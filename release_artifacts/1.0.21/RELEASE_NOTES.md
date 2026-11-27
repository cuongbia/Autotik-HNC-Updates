Autotik HNC 1.0.21 sửa app đứng ở thông báo "Có video đã bấm Đăng chưa rõ kết quả".

- Nick có video đã bấm Đăng nhưng chưa rõ kết quả không còn được đưa vào điều phối mỗi 20 giây. Trước đây mỗi lượt nick đó giữ proxy một lúc rồi dừng, làm các nick dùng chung proxy liên tục "Chờ proxy" và không đăng được.
- Tự xác minh cả video kẹt từ bản cũ (không có caption lưu lúc bấm Đăng): app đọc kênh TikTok của nick, lấy thời điểm đăng từ mã video, rồi so số video trên kênh từ lúc video vào kho với số bài app đã ghi nhận đăng. Kênh có bài chưa được ghi nhận thì ghi Đã đăng; mọi video mới đều đã được ghi nhận và đã qua 6 giờ thì đưa lại hàng chờ (giữ file đã render). Không chắc chắn thì giữ để tránh đăng trùng.
- Video mới (từ 1.0.20) còn được nhận ra theo thời điểm video tạo trong 30 phút sau lúc bấm Đăng, kể cả khi TikTok đổi caption.
- Nick có từ 2 video kẹt kiểu cũ trở lên vẫn cần xác nhận tay ở "Video chờ xác minh".
- Bỏ yêu cầu kênh sao chép phải là kênh Việt Nam, cả lúc thêm kênh lẫn lúc chuẩn bị video. Chỉ từ chối kênh không đọc được hoặc không còn hoạt động. Phần tự tìm kênh bổ sung vẫn ưu tiên kênh Việt Nam.

Sau cập nhật: dừng tác vụ, đóng/mở lại app, bấm Chạy. Bộ xác minh chạy khoảng 1 phút sau khi bấm Chạy rồi mỗi 10 phút; có thể bấm "Tự kiểm tra ngay" trong Trung tâm sao chép → "Video chờ xác minh".

Kiểm chứng: 143 ca kiểm thử bản khách và 369 ca trên mã nguồn gốc (SQLite tạm, mô phỏng kênh TikTok, video kẹt kiểu cũ/mới, bỏ điều phối nick chờ xác minh, nguồn không phải Việt Nam) đạt. EXE có 92 module khách đã đối chiếu bytecode, khởi động với license/dữ liệu tạm và chạy chu kỳ quét thông tin rỗng được; GPM Global API mô phỏng chỉ đọc, không ghi profile. Chưa chạy cả ngày trên máy khách và chưa đăng lên tài khoản thật bằng bản này.
