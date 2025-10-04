import mysql.connector

# ====== 1. Kết nối Database ======
db = mysql.connector.connect(
    host="localhost",
    user="root",          # đổi theo user MySQL của em
    password="matkhau",   # đổi theo mật khẩu MySQL
    database="CMS_demo"
)

cursor = db.cursor()

# ====== 2. Kiểm tra quyền admin ======
def is_admin(username):
    sql = "SELECT role FROM users WHERE username=%s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    if result and result[0].lower() == "admin":
        return True
    return False

# ====== 3. Thêm bài viết ======
def add_post(title, content, author):
    sql = "INSERT INTO posts (title, content, author, status) VALUES (%s, %s, %s, %s)"
    val = (title, content, author, "pending")
    cursor.execute(sql, val)
    db.commit()
    log_action(author, f"Added post: {title}")
    print(f"Bài viết '{title}' đã được thêm thành công!")

# ====== 4. Duyệt bài viết ======
def approve_post(post_id, admin_user):
    if not is_admin(admin_user):
        print("Bạn không có quyền admin.")
        return
    sql = "UPDATE posts SET status='approved' WHERE id=%s"
    cursor.execute(sql, (post_id,))
    db.commit()
    log_action(admin_user, f"Approved post ID {post_id}")
    print(f"Post ID {post_id} đã được duyệt.")

# ====== 5. Ghi log hành động ======
def log_action(username, action):
    sql = "INSERT INTO logs (username, action) VALUES (%s, %s)"
    cursor.execute(sql, (username, action))
    db.commit()

# ====== 6. Xem posts và logs (dùng để test) ======
def show_posts():
    cursor.execute("SELECT * FROM posts")
    for post in cursor.fetchall():
        print(post)

def show_logs():
    cursor.execute("SELECT * FROM logs")
    for log in cursor.fetchall():
        print(log)

# ====== 7. Ví dụ sử dụng ======
if __name__ == "__main__":
    # Thêm bài
    add_post("Khai trương cửa hàng mới", "Chi nhánh mới tại quận 1 đã mở.", "Tracy")
    add_post("Khuyến mãi cafe", "Giảm giá 20% cho khách hàng đầu tiên.", "Luca")

    # Duyệt bài (chỉ admin)
    approve_post(1, "Tracy")
    approve_post(2, "Luca")  # sẽ báo không có quyền

    # Hiển thị dữ liệu
    print("\n=== POSTS ===")
    show_posts()

    print("\n=== LOGS ===")
    show_logs()
