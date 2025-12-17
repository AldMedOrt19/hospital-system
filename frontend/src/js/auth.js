// src/js/auth.js
const AUTH_API = "http://localhost:8004/auth/login";

document.getElementById("login-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch(AUTH_API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  if (!res.ok) {
    alert("Credenciales inválidas");
    return;
  }

  const data = await res.json();

  // 🔑 guardar sesión
  localStorage.setItem("token", data.access_token);
  localStorage.setItem("role", data.role);

  // 🚀 redirigir
  window.location.href = "/dashboard.html";
});
