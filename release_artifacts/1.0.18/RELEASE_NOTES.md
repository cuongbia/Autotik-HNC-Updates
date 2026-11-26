Autotik HNC 1.0.18 sửa lỗi Autotik hiện proxy đã lưu nhưng profile GPM chưa được gán proxy.

Trước đây bảng Đổi Proxy lưu SQLite và đổi cột hiển thị trước khi biết GPM đã cập nhật thành công; thao tác lỗi vẫn được tính thành công và đóng bảng. Adapter cũng tự thêm tiền tố http:// vào dạng IP:PORT:USER:PASS.

- Giữ dạng proxy native mà GPM Global hỗ trợ; giữ giao thức SOCKS/HTTPS khi nhập và chọn từ kho.
- Sau cập nhật proxy, đọc lại đúng profile GPM và đối chiếu giao thức, host, port, user, password. Chỉ lưu SQLite và báo thành công sau khi khớp.
- Khi GPM lỗi, chưa lưu, sai proxy hoặc timeout: giữ dữ liệu cũ và nội dung nhập; chỉ báo những profile thành công, giữ bảng mở để thử lại. Không đổi proxy profile đang mở trong app.
- Khi tạo profile có proxy, xác nhận proxy trên GPM, bổ sung bằng update nếu thiếu rồi xác nhận lại. Nếu không xác nhận được, báo profile đã tạo, không tạo lại để tránh trùng.
- Trước khi mở profile có proxy lưu trong Autotik, đọc và đối chiếu GPM. Nếu chưa khớp, yêu cầu Lưu & cập nhật GPM, không chạy auto khi proxy chưa đồng bộ.
- Với ProxyCheckFailed và proxy đang lưu có đúng tiền tố HTTP thừa của bản cũ, chuyển về dạng native, xác nhận rồi thử mở lại tối đa một lần. Không bỏ proxy, không đổi sang IP trực tiếp và không dùng skip_proxy_check.
- Giữ dữ liệu/license, GPM Legacy, core trong AppData và khóa profile/proxy theo workspace.

Khách cần làm sau cập nhật: chọn những profile cũ đang hiện proxy nhưng GPM chưa có → Đổi Proxy → giữ giá trị đã nhập → Lưu & cập nhật GPM. Đợi báo xác nhận thành công rồi chạy Auto Login/Nuôi Nick.

Kiểm tra: 66 ca GPM; 126 ca kiểm tra khách, 18 ca thông tin/chọn video và 8 ca dialog/SQLite qua tiến trình riêng đạt. Đã xem giao diện lỗi với font Windows; EXE khởi động được với dữ liệu tạm và Global API mô phỏng chỉ đọc. Chưa kiểm chứng chạy tài khoản thật trên máy khách; không cam kết tương thích 100% mọi bản GPM.
