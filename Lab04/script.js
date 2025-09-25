
document.getElementById("loginForm").addEventListener("submit", function(e){
  e.preventDefault();
  
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  const remember = document.getElementById("rememberMe").checked;

  if(user === "" || pass === ""){
    alert("Vui lòng nhập đầy đủ Username và Password!");
    return;
  }
  if(pass.length < 8){
    alert("Mật khẩu phải có ít nhất 8 ký tự!");
    return;
  }

  
  if(remember){
    localStorage.setItem("savedUser", user);
  } else {
    localStorage.removeItem("savedUser");
  }

  // Chuyển sang dashboard
  document.getElementById("login-container").classList.add("hidden");
  document.getElementById("dashboard").classList.remove("hidden");
  document.getElementById("section-title").innerText = "Xin chào, " + user;
});

// Nút Cancel
document.getElementById("cancelBtn").addEventListener("click", function(){
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
});

// Hiện nội dung Dashboard theo menu
function showSection(section){
  const title = document.getElementById("section-title");
  const content = document.getElementById("section-content");

  switch(section){
    case "posts":
      title.innerText = "Quản lý Bài viết";
      content.innerHTML = "<p>Danh sách bài viết quảng bá cafe sẽ hiển thị ở đây...</p>";
      break;
    case "menu":
      title.innerText = "Quản lý Menu";
      content.innerHTML = "<p>Danh sách sản phẩm đồ uống sẽ hiển thị ở đây...</p>";
      break;
    case "customers":
      title.innerText = "Quản lý Khách hàng";
      content.innerHTML = "<p>Thông tin khách hàng thân thiết sẽ hiển thị ở đây...</p>";
      break;
    case "stats":
      title.innerText = "Thống kê";
      content.innerHTML = "<p>Biểu đồ doanh thu, lượt check-in sẽ hiển thị ở đây...</p>";
      break;
  }
}

// Logout
function logout(){
  document.getElementById("dashboard").classList.add("hidden");
  document.getElementById("login-container").classList.remove("hidden");
}
const users = [
  { username: "admin1", role: "Admin Tổng" },
  { username: "manager1", role: "Quản lý Chi nhánh" },
  { username: "editor1", role: "Biên tập nội dung" },
  { username: "campaign1", role: "Quản lý Chiến dịch" }
];

// Hiển thị quyền sau khi đăng nhập
function showRole(username) {
  const user = users.find(u => u.username === username);
  if (user) {
    document.querySelector('.admin-name').textContent = user.role;
  }
}
let activityLog = [];

function logActivity(username, action) {
  const time = new Date().toLocaleString();
  activityLog.push({ username, action, time });
  console.log(`${time} - ${username}: ${action}`);
}


logActivity("admin1", "Đăng nhập hệ thống");
logActivity("editor1", "Chỉnh sửa bài viết #123");
