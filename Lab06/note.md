**Cafe Media Management System**

## 1. Class Diagram
- **User**: đại diện người dùng (Admin, Writer, Approver, Manager).  
- **Article**: bài viết truyền thông. Có thể gắn Media và được duyệt trước khi xuất bản.  
- **Media**: hình ảnh/video gắn vào bài viết.  
- **Campaign**: chiến dịch truyền thông, bao gồm nhiều bài viết.  
- **Approval**: quá trình duyệt bài, gồm trạng thái approved/rejected.  
- **Report**: báo cáo về hiệu quả, có thể export.  

## 2. Package Diagram
- **UI**: giao diện người dùng (login, dashboard, editor, report).  
- **Controller**: xử lý request từ UI.  
- **Service**: nghiệp vụ chính (auth, quản lý bài viết, campaign, report).  
- **Database (DAO)**: giao tiếp với CSDL.  

## 3. Ánh xạ Use Case → Class
- UC “Đăng nhập” → User + AuthService  
- UC “Viết bài & duyệt bài” → Article, Approval, User (writer/approver)  
- UC “Quản lý chiến dịch” → Campaign + Article  
- UC “Xem báo cáo” → Report + Campaign  

