# test_mockmodule.py
import pytest
from mock_module import login_user, add_post, approve_post, posts, logs

# --- Login Tests ---
def test_login_success():
    user = login_user("admin", "admin123")
    assert user is not None
    assert user["username"] == "admin"
    assert user["role"] == "admin"

def test_login_fail_wrong_password():
    user = login_user("admin", "wrongpass")
    assert user is None

def test_login_fail_no_user():
    user = login_user("unknown", "admin123")
    assert user is None

# --- Add Post Tests ---
def test_add_post_success():
    post = add_post(2, "Test Post", "This is a test content")
    assert post in posts
    assert post["title"] == "Test Post"
    assert post["approved"] is False
    # Kiểm tra log
    assert logs[-1] == f"User 2 added post {post['id']}"

# --- Approve Post Tests ---
def test_approve_post_success():
    # Tạo post mới
    post = add_post(2, "To Approve", "Content")
    approved_post = approve_post(1, post["id"])
    assert approved_post["approved"] is True
    assert logs[-1] == f"Admin 1 approved post {post['id']}"

def test_approve_post_fail_not_admin():
    post = add_post(2, "Another Post", "Content")
    with pytest.raises(PermissionError):
        approve_post(2, post["id"])  # user 2 là editor, không phải admin

def test_approve_post_fail_not_found():
    with pytest.raises(ValueError):
        approve_post(1, 999)  # post_id không tồn tại
