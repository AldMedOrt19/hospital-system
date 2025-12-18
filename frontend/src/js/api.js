const BASE_URL = "http://3.81.227.64";

export const API = {
  auth: `${BASE_URL}:8004/auth`,
  pacientes: `${BASE_URL}:8001/pacientes`,
  citas: `${BASE_URL}:8002/citas`,
  historiales: `${BASE_URL}:8003/historiales`
};

export function authHeaders() {
  return {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + localStorage.getItem("token")
  };
}
