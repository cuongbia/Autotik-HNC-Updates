Autotik HNC 1.0.20 tăng tốc đăng video và gỡ kẹt nick chờ xác minh.

- Slot đăng và slot render tách riêng: trước đây job đang tải/render cũng bị tính vào giới hạn 10 profile, nên lúc cao điểm video đã render xong vẫn phải chờ. Giờ video sẵn sàng được đăng ngay khi có trình duyệt rảnh; render dùng ngân sách "số luồng render" trong Cài đặt.
- Render dùng lõi CPU riêng: trước đây mọi FFmpeg bị ghim chung vào 4 lõi đầu của máy. Giờ mỗi render có nhóm lõi riêng (tối đa 4), xoay vòng trên 3/4 số lõi, phần còn lại để dành cho trình duyệt và giao diện.
- Chỉ chuyển video sang UPLOADING đúng lúc bấm nút Đăng. Lỗi khi đang chờ proxy/GPM hoặc trước khi bấm Đăng: video về hàng chờ, giữ file đã render, thử lại sau 15 phút, nick không bị chặn.
- Tự xác minh: lúc bấm Đăng, app lưu caption và thời điểm. Khi điều phối đang chạy, mỗi 10 phút app đọc kênh TikTok của nick: thấy video thì ghi Đã đăng; đọc được kênh mà qua 6 giờ không thấy thì đưa lại hàng chờ; lỗi mạng/kênh riêng tư thì giữ nguyên để tránh đăng trùng.
- Màn hình mới "Video chờ xác minh" trong Trung tâm sao chép: mở kênh, tự kiểm tra ngay, đánh dấu Đã đăng hoặc Chưa đăng (có xác nhận). Video kẹt từ bản cũ không có caption đã lưu nên cần xác nhận tay ở đây.
- Video PROCESSING dở dang của phiên trước (chưa bấm Đăng) được trả về hàng chờ khi bấm Chạy lần đầu.
- Bấm Lưu chỉ lưu cấu hình, không tự bật lịch; đổi nguồn tạm dừng lịch của nick đó. Cấu hình từng nick có thêm nút "Lưu và chạy lịch". Nút chuyển trang không còn bị cắt chữ.

Sau cập nhật: dừng tác vụ, đóng/mở lại app để nạp code. Vào Trung tâm sao chép → "Video chờ xác minh" để xử lý các video kẹt từ bản cũ, rồi Chạy các tài khoản cần chạy.

Kiểm chứng: 143 ca kiểm thử bản khách và 359 ca trên mã nguồn gốc (SQLite tạm, mô phỏng lỗi trước/sau bấm Đăng, xác minh kênh, phân slot, chia lõi CPU, màn hình xác minh) đạt. EXE có 92 module khách đã đối chiếu bytecode, khởi động với license/dữ liệu tạm và chạy chu kỳ quét thông tin rỗng được; GPM Global API mô phỏng chỉ đọc, không ghi profile. Chưa chạy cả ngày trên máy khách và chưa đăng lên tài khoản thật bằng bản này; không cam kết số video/ngày. Chỉ tiêu mỗi ngày/khoảng cách đăng vẫn theo cấu hình.
