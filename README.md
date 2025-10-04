# 🛠️ Software Engineering Project – HỆ THỐNG QUẢN TRỊ CỔNG TRUYỀN THÔNG SỐ CHUỖI CAFE T.G

## 📌 Giới thiệu
Dự án này được phát triển trong môn **Nhập môn Công nghệ Phần mềm** tại Học Viện Công nghệ Bưu chính Viễn thông cơ sở Tp. Hồ Chí Minh.

Mục tiêu là áp dụng toàn bộ quy trình phát triển phần mềm theo mô hình **Agile - Scrum**, từ phân tích yêu cầu, thiết kế, lập trình, kiểm thử và triển khai, để xây dựng một hệ thống quản lý tập trung cho hoạt động truyền thông và nội dung của chuỗi cà phê T.G.

---

## 👥 Thành viên nhóm & Vai trò
| Họ tên | Vai trò | Kỹ năng chính |
| :--- | :--- | :--- |
| **Hồ Thị Cẩm** | **Leader** | Lập kế hoạch dự án, phân tích yêu cầu, quản lý đội nhóm. |
| **Đinh Thị Thi Duyên** | **Developer** | Lập trình (Java/Python), thiết kế CSDL (MySQL), sử dụng Git. |
| **Nguyễn Ngọc Ánh** | **Tester** | Lập kế hoạch kiểm thử, viết kịch bản kiểm thử (test case), kiểm thử thủ công. |

### 🎯 Mục tiêu chung của dự án
* Hoàn thành và bàn giao hệ thống quản lý **Quản trị Cổng truyền thông số Chuỗi Cafe T.G** đúng thời hạn.
* Áp dụng thành công mô hình phát triển **Agile – Scrum** để quản lý quy trình làm việc (Lab 09).
* Xây dựng một sản phẩm đáp ứng đầy đủ các yêu cầu đã đề ra trong phần phân tích (Lab 02).

---

## 🎯 Use Case chính (Phạm vi dự án)
- **Quản lý Nội dung (CMS)**: Tạo, chỉnh sửa, duyệt bài viết, hình ảnh, video.
- **Xuất bản Đa kênh**: Đăng tải nội dung lên các nền tảng xã hội (Facebook, Zalo, YouTube).
- **Phân quyền người dùng**: Gán vai trò (Admin, Content Manager).
- **Theo dõi & Báo cáo**: Thống kê truy cập, hiệu suất bài viết.

(Sơ đồ use case tổng thể đã được hoàn thành trong Lab 02)

---

## 📐 Thiết kế hệ thống (Các Artifacts)
- **Use Case Diagram**: ![Use Case Diagram](./docs/usecase.png)
- **Sequence Diagram**: ![Sequence Diagram](./docs/sequence.png)
- **Class Diagram**: ![Class Diagram](./docs/class_diagram.png)
- **ERD (Entity Relationship Diagram)**: ![ERD Diagram](./docs/erd.png)

---

## 💻 Công nghệ sử dụng
- **Ngôn ngữ**: [Python] / [JavaScript] (Cập nhật theo ngôn ngữ thực tế)
- **Framework/Thư viện**: [Ví dụ: Flask/Django cho Python, Node.js cho JS]
- **IDE**: Visual Studio Code
- **CSDL**: MySQL / PostgreSQL (Cập nhật theo lựa chọn)
- **Quản lý phiên bản**: Git + GitHub
- **Quản lý dự án**: Jira / ClickUp (Áp dụng Scrum/Agile)

---

## 🚀 Cài đặt & chạy thử
1. Clone repo:
   ```bash
   git clone [https://github.com/vancv43/](https://github.com/Hicam93-cmyk/)nhapmon-PhanMem.git
   cd nhapmon-PhanMem

   ## 📅 Quy trình Lab (Labs 01 - 10)

Đây là lộ trình thực hiện các bài Lab, áp dụng các yêu cầu kỹ thuật vào dự án **Hệ thống Quản trị Cổng Truyền thông số Chuỗi Cafe T.G**.

| Lab | Mục tiêu chính | Nội dung áp dụng cho **Chuỗi Cafe T.G** | Artifacts cần nộp |
| :--- | :--- | :--- | :--- |
| **Lab 01** | Thiết lập môi trường GitHub & Git | Tạo Repo, Cấu hình Git, Cập nhật **README.md** (thông tin nhóm/dự án). | Link Repo GitHub |
| **Lab 02** | Phân tích yêu cầu & Thiết kế Use Case | Chọn Mini Project, Vẽ **Use Case Diagram tổng thể**, Viết **Use Case Descriptions** (Quản lý Nội dung, Xuất bản Đa kênh). | UCD (ảnh/drawio), UCDs (file .md) |
| **Lab 03** | UML Thiết kế (Sequence Diagram) | Vẽ **Sequence Diagram** cho một quy trình nghiệp vụ cốt lõi (Ví dụ: 'Tạo và Duyệt bài viết' hoặc 'Tạo Đơn hàng/Menu'). | SQD (ảnh/drawio), File mô tả luồng |
| **Lab 04** | Coding giao diện cơ bản | Viết **Form Login** (HTML/CSS/JS) cho hệ thống quản trị bằng VSC. | Source code (HTML, CSS, JS) |
| **Lab 05** | Tích hợp, quản lý & báo cáo | Gom artifacts (Lab 02-04), Tạo **Project Report** (Markdown/PDF), **Tag version v1.0**. | Project Report, Link Repo (Tag v1.0) |
| **Lab 06** | Thiết kế chi tiết lớp & kiến trúc | Thiết kế **Class Diagram** (Lớp `Content`, `User`, `Product`, `Branch`) và **Package Diagram** cho hệ thống Cafe. | `class-coffee.puml/png`, `package-diagram.puml/png` |
| **Lab 07** | Phát triển Module Code (Prototype) | Viết **Module Python/Java** mô phỏng nghiệp vụ (Ví dụ: **Xử lý tồn kho** sau khi bán/tạo đơn, hoặc **Xác thực quyền hạn**). | Mã nguồn Module, ảnh màn hình chạy thử |
| **Lab 08** | Kiểm thử Unit test & Integration test | Viết **Unit Test** cho hàm logic nghiệp vụ (tính toán, kiểm tra tồn kho) và **Integration Test (Selenium)** cho Form Login (Lab 04). | Source test files, ảnh màn hình test pass/fail |
| **Lab 09** | Quản lý dự án trên Jira (Agile) | Tạo Project **"T.G Coffee System"**, Tạo Epic, Stories, **Lập Sprint 1** (Ví dụ: Login + Tạo Nội dung). | File report (.md/.pdf) với ảnh chụp Backlog, Board, Burndown |
| **Lab 10** | Báo cáo tổng hợp & Demo cuối kỳ | Gom toàn bộ Artifacts (Lab 02-09), Viết **Final Report**. **Demo** Form Login → Module Code → Trình bày Jira Board. | Final Report, Slide PPT (nếu có), Link Repo |
