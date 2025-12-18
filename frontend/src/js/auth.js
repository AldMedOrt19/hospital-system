import { API } from "./api.js";

document.getElementById("login-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch(`${API.auth}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  if (!res.ok) {
    alert("Credenciales inválidas");
    return;
  }

  const data = await res.json();

  localStorage.setItem("token", data.access_token);
  localStorage.setItem("role", data.role);

  window.location.href = "/dashboard.html";
});
