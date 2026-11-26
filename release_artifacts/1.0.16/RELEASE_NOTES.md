Autotik HNC 1.0.16 sửa lỗi không tìm thấy Chrome core khi GPM Global lưu core ngoài thư mục engine.

- Đọc thêm kho trình duyệt tại %APPDATA%\GPMLoginGlobal\Browsers\ChromiumCore_*, đúng cấu trúc khách cung cấp: ChromiumCore_v157 chứa chrome.exe.
- Dùng biến APPDATA của người dùng Windows hiện tại, không gắn cứng tên Admin hoặc yêu cầu chép core vào C:\Autotik\engine.
- Đọc phiên bản đầy đủ từ file trình duyệt; không suy đoán số bản dựng từ tên v157. Chế độ Random chọn phiên bản cao nhất tìm được.
- Nhận diện kho AppData cả khi không tìm thấy GPMLoginGlobal.exe trong thư mục engine. Không lấy core trên máy Autotik khi kết nối API GPM từ xa.
- Giữ bảo vệ kiểm tra core trước khi tạo nhóm/profile; lệnh tạo bị timeout không tự gửi lại. Giữ dữ liệu/license và hỗ trợ Legacy.

Kiểm tra: 46 ca GPM đạt, gồm ca tích hợp tạo 5 profile qua API mô phỏng bằng đường dẫn AppData mới; bộ kiểm tra khách 104 ca và 18 ca thông tin/chọn video đạt. EXE khởi động thành công trong dữ liệu tạm với API Global mô phỏng chỉ đọc. Chưa chạy profile thật trên máy khách; không cam kết tương thích 100% mọi bản GPM.

Cập nhật trong app, sau đó khi tạo profile chọn Chrome = Random. Không di chuyển hoặc đổi tên thư mục core. Nếu thay EXE thủ công, đóng Autotik và thay EXE cũ; giữ nguyên thư mục dữ liệu/license và GPM.
