export const API = {
  auth: "http://localhost:8004/auth",
  pacientes: "http://localhost:8001/pacientes/",
  citas: "http://localhost:8002/citas/",
  historiales: "http://localhost:8003/historiales/"
};

export function authHeaders() {
  return {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + localStorage.getItem("token")
  };
}
