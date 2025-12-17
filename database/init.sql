CREATE TABLE IF NOT EXISTS pacientes (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  dni VARCHAR(8) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS citas (
  id SERIAL PRIMARY KEY,
  paciente_id INT NOT NULL REFERENCES pacientes(id) ON DELETE CASCADE,
  fecha DATE NOT NULL,
  motivo VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS historiales (
  id SERIAL PRIMARY KEY,
  paciente_id INT NOT NULL REFERENCES pacientes(id) ON DELETE CASCADE,
  descripcion TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  rol VARCHAR(30) NOT NULL
);

-- usuarios demo
INSERT INTO usuarios (username, password, rol) VALUES
('admin', 'admin123', 'admin'),
('doctor1', 'doctor123', 'doctor'),
('recep1', 'recep123', 'recepcionista')
ON CONFLICT (username) DO NOTHING;

-- seed (opcional)
INSERT INTO pacientes (nombre, dni) VALUES
('Juan Perez', '12345678'),
('Maria Lopez', '87654321'),
('Carlos Diaz', '45678912')
ON CONFLICT (dni) DO NOTHING;

INSERT INTO citas (paciente_id, fecha, motivo) VALUES
(1, '2025-12-20', 'Control general'),
(2, '2025-12-21', 'Dolor de cabeza')
ON CONFLICT DO NOTHING;
