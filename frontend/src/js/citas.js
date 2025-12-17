import { API, authHeaders } from "./api.js";

const tabla = document.getElementById("tabla-citas");

async function cargarCitas() {
  const res = await fetch(API.citas, {
    headers: authHeaders()
  });

  const data = await res.json();
  tabla.innerHTML = "";

  data.forEach(c => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${c.id}</td>
      <td>${c.paciente_id}</td>
      <td>${c.fecha}</td>
      <td>${c.motivo}</td>
    `;
    tabla.appendChild(tr);
  });
}

document.addEventListener("DOMContentLoaded", cargarCitas);

window.crearCita = async function (e) {
  e.preventDefault();

  const paciente_id = document.getElementById("paciente_id").value;
  const fecha = document.getElementById("fecha").value;
  const motivo = document.getElementById("motivo").value;

  await fetch(API.citas, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ paciente_id, fecha, motivo })
  });

  cargarCitas();
};
