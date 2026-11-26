Bản khách Autotik HNC 1.0.13 — cải thiện khởi động GPM.

- Khi mở GPM từ Autotik EXE, tách các đường dẫn thư viện của bộ đóng gói; khôi phục môi trường Autotik sau khi tạo tiến trình, kể cả khi mở GPM thất bại.
- Nhận diện tên GPMLoginGlobal.exe và đưa vào bộ lọc chọn chương trình.
- BÁO RÕ CHƯA HỖ TRỢ API GLOBAL: Autotik hiện vẫn điều khiển GPM Legacy /api/v3; Global dùng /api/v1 và mặc định cổng 9495. Đổi tên EXE hoặc chỉ đổi cổng không đủ. Khi chọn Global và không có API v3 tương thích, app dừng sớm với hướng dẫn thay vì chờ 90 giây.
- Báo sớm nếu GPM tự thoát với mã lỗi. Trường hợp GPM mở trực tiếp cũng lỗi Newtonsoft.Json cần sửa bộ cài GPM; cập nhật Autotik không thay DLL của GPM.
- Giữ dữ liệu và license; không thêm Telegram/Kick Stu.

Đã đạt 16 ca kiểm tra khởi động GPM. EXE được kiểm tra mở cửa sổ chính và chạy chu kỳ quét nền với dữ liệu tạm; chưa kiểm thử điều khiển profile qua API Global.

Khách đang không vào được app có thể tải trực tiếp Autotik_HNC-1.0.13.exe, đóng app rồi đổi tên thành Autotik_HNC.exe để thay file cũ. Giữ nguyên vùng dữ liệu khách.
