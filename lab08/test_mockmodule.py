# mock_module.py
import hashlib

# Dữ liệu giả lập
users = [
    {"id": 1, "username": "admin", "password": hashlib.sha256("admin123".encode()).hexdigest(), "role": "admin"},
    {"id": 2, "username": "editor", "password": hashlib.sha256("editor123".encode()).hexdigest(), "role": "editor"}
]

posts = []
logs = []

def login_user(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    for u in users:
        if u["username"] == username and u["password"] == hashed:
            return u
    return None

def add_post(user_id, title, content):
    post_id = len(posts) + 1
    post = {"id": post_id, "user_id": user_id, "title": title, "content": content, "approved": False}
    posts.append(post)
    logs.append(f"User {user_id} added post {post_id}")
    return post

def approve_post(admin_id, post_id):
    admin = next((u for u in users if u["id"] == admin_id), None)
    if not admin or admin["role"] != "admin":
        raise PermissionError("Not authorized")
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        raise ValueError("Post not found")
    post["approved"] = True
    logs.append(f"Admin {admin_id} approved post {post_id}")
    return post

