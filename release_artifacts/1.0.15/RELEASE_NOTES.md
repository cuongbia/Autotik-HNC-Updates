Autotik HNC 1.0.15 — sửa nhận diện Chrome core trên GPM Global.

- Chế độ Random đọc core đã cài từ thư mục GPM Global đang chạy hoặc đường dẫn GPM đã chọn. Tạo được profile đầu tiên khi chưa có profile Chrome mẫu.
- Đọc phiên bản từ tài nguyên EXE Windows hoặc thư mục Chromium hoàn chỉnh; không chạy Chrome để dò và không dùng danh sách core Legacy cố định.
- Ưu tiên bộ GPM đang chạy, tránh lấy core từ đường dẫn cũ. Khi có nhiều bộ Global chạy, chỉ dùng bộ khớp đường dẫn đã chọn.
- Kiểm tra core trước khi gửi lệnh tạo nhóm/profile. Khi chọn tay phiên bản chưa cài mà đã nhận diện được kho core, báo phiên bản có thể dùng.
- Giữ lệnh tạo một lần; timeout không tự tạo lại, tránh profile trùng.
- Giữ hỗ trợ API Global v1/Legacy v3, proxy, nhóm, CDP, xếp cửa sổ và giới hạn slot. Giữ dữ liệu/license; bản khách không kèm Telegram/Kick Stu.

Kiểm chứng: 41 ca GPM (gồm tạo 5 profile đầu tiên qua API mô phỏng), tổng bộ kiểm tra khách 100 ca và 18 ca thông tin/chọn video đạt; EXE khởi động thành công với dữ liệu tạm và Global mô phỏng chỉ đọc. Đã kiểm tra hàm đọc phiên bản trên Chrome EXE thật. Chưa kiểm chứng tạo/mở profile và đăng TikTok trên GPM Global thật của khách; không tuyên bố tương thích 100% mọi bản GPM.

Khách mở app và chọn Cập nhật. Nếu cần thay thủ công: đóng Autotik, tải EXE, đổi tên thành Autotik_HNC.exe và thay file cũ. Giữ nguyên thư mục dữ liệu/license và bộ GPM.
