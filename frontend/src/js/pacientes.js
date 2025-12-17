import { API, authHeaders } from "./api.js";

const tabla = document.getElementById("tabla-pacientes");

async function cargarPacientes() {
  const res = await fetch(API.pacientes, {
    headers: authHeaders()
  });

  const data = await res.json();
  tabla.innerHTML = "";

  data.forEach(p => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${p.id}</td>
      <td>${p.nombre}</td>
      <td>${p.dni}</td>
    `;
    tabla.appendChild(tr);
  });
}

async function crearPaciente(e) {
  e.preventDefault();

  const nombre = document.getElementById("nombre").value;
  const dni = document.getElementById("dni").value;

  const res = await fetch(API.pacientes, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ nombre, dni })
  });

  if (!res.ok) {
    alert("Error al registrar paciente");
    return;
  }

  cargarPacientes();
  e.target.reset();
}

document.addEventListener("DOMContentLoaded", cargarPacientes);

// 🔥 EXPÓN LA FUNCIÓN AL HTML
window.crearPaciente = crearPaciente;
