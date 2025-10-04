CREATE DATABASE cms_demo;
USE cms_demo;

-- Bảng người dùng
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(100),
  role VARCHAR(20)
);

-- Bảng bài viết
CREATE TABLE posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100),
  content TEXT,
  status VARCHAR(20)
);

-- Bảng ghi log
CREATE TABLE logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  action VARCHAR(100),
  admin_id INT,
  post_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dữ liệu mẫu
INSERT INTO users (username, password, role)
VALUES ('admin01', '12345', 'admin'),
       ('content01', '12345', 'content');

INSERT INTO posts (title, content, status)
VALUES ('Bài viết 1', 'Nội dung bài viết 1', 'pending'),
       ('Bài viết 2', 'Nội dung bài viết 2', 'pending');


