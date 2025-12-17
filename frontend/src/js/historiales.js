import { API, authHeaders } from "./api.js";

const tabla = document.getElementById("tabla-historiales");

async function cargarHistoriales() {
  const res = await fetch(API.historiales, {
    headers: authHeaders()
  });

  const data = await res.json();
  tabla.innerHTML = "";

  data.forEach(h => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${h.id}</td>
      <td>${h.paciente_id}</td>
      <td>${h.descripcion}</td>
    `;
    tabla.appendChild(tr);
  });
}

document.addEventListener("DOMContentLoaded", cargarHistoriales);

window.crearHistorial = async function (e) {
  e.preventDefault();

  const paciente_id = document.getElementById("paciente_id").value;
  const descripcion = document.getElementById("descripcion").value;

  await fetch(API.historiales, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ paciente_id, descripcion })
  });

  cargarHistoriales();
};
