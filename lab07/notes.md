# Lab 07 - CMS Chuỗi Cà Phê

## 1. Mục tiêu
- Mô phỏng quản lý bài viết trong CMS của chuỗi cà phê.
- Thực hành kết nối MySQL với Python.
- Thêm bài viết, duyệt bài, kiểm tra quyền admin và ghi log hành động.

## 2. Cấu trúc Database
### Bảng `users`
| Column   | Type        | Mô tả                  |
|----------|------------|------------------------|
| id       | INT        | Khóa chính, tự tăng     |
| username | VARCHAR(50)| Tên người dùng          |
| role     | VARCHAR(10)| Quyền: admin hoặc user  |

### Bảng `posts`
| Column   | Type        | Mô tả                        |
|----------|------------|-------------------------------|
| id       | INT        | Khóa chính, tự tăng           |
| title    | VARCHAR(255)| Tiêu đề bài viết             |
| content  | TEXT       | Nội dung bài viết             |
| author   | VARCHAR(50)| Tên người đăng bài           |
| status   | VARCHAR(20)| Trạng thái: pending/approved |

### Bảng `logs`
| Column    | Type        | Mô tả                        |
|-----------|------------|-------------------------------|
| id        | INT        | Khóa chính, tự tăng           |
| action    | VARCHAR(255)| Hành động của user           |
| username  | VARCHAR(50)| Người thực hiện hành động    |
| timestamp | TIMESTAMP  | Thời gian thực hiện          |

## 3. Giải thích chức năng các hàm trong `cms_module.py`

### 3.1 Kết nối DB
```python
db = mysql.connector.connect(...)
cursor = db.cursor()

