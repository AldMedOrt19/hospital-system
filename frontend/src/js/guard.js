// src/js/guard.js
if (!localStorage.getItem("token")) {
  window.location.href = "/login.html";
}
