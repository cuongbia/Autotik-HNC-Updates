Autotik HNC 1.0.17 — chẩn đoán lỗi mở profile GPM Global.

Khách đã tạo được profile nhưng GPM từ chối mở profile để chạy auto. Bản trước chỉ hiện “profiles (HTTP 200)” và bỏ mất trường message từ GPM, nên chưa xác định được nguyên nhân thật.

- Hiển thị lý do lỗi do GPM cung cấp, kèm đúng thao tác: mở/dừng/tạo/cập nhật/xóa profile hoặc nhóm.
- Giữ xử lý success=false là thất bại kể cả HTTP 200. Không tự gửi lại lệnh mở/tạo sau timeout.
- Che mật khẩu, proxy có tài khoản, token, khóa API và email trong thông báo; không ghi nguyên đối tượng data/request của GPM.
- Giữ nhận diện core trong AppData, dữ liệu/license và hỗ trợ Legacy.

Đây là bản bổ sung chẩn đoán, chưa sửa hay xác nhận nguyên nhân GPM không mở được profile thật trên máy khách. Sau cập nhật, thử một profile và gửi nội dung lỗi chi tiết mới để tiếp tục xử lý.

Kiểm tra: 50 ca GPM, 109 ca kiểm tra khách và 18 ca thông tin/chọn video đạt. EXE khởi động thành công trong dữ liệu tạm và API Global mô phỏng chỉ đọc. Không chạy tài khoản TikTok thật trong quá trình kiểm thử.
