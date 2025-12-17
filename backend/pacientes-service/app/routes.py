from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Paciente
from app.schemas import PacienteCreate, PacienteResponse

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 GET: listar pacientes
@router.get("/", response_model=list[PacienteResponse])
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(Paciente).all()

@router.get("/{paciente_id}", response_model=PacienteResponse)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente


# 🔹 POST: crear paciente
@router.post("/", response_model=PacienteResponse)
def crear_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):

    # 🔍 VALIDACIÓN DNI
    if not paciente.dni.isdigit():
        raise HTTPException(status_code=400, detail="El DNI debe contener solo números")

    if len(paciente.dni) != 8:
        raise HTTPException(status_code=400, detail="El DNI debe tener exactamente 8 dígitos")

    ya_existe = db.query(Paciente).filter(Paciente.dni == paciente.dni).first()
    if ya_existe:
        raise HTTPException(status_code=400, detail="Ya existe un paciente con ese DNI")

    nuevo = Paciente(nombre=paciente.nombre, dni=paciente.dni)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo



# 🔹 PUT: actualizar paciente
@router.put("/{paciente_id}", response_model=PacienteResponse)
def actualizar_paciente(
    paciente_id: int,
    paciente: PacienteCreate,
    db: Session = Depends(get_db)
):
    existente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    # validar DNI repetido (excepto el mismo paciente)
    repetido = db.query(Paciente).filter(
        Paciente.dni == paciente.dni,
        Paciente.id != paciente_id
    ).first()
    if repetido:
        raise HTTPException(status_code=400, detail="Ese DNI ya está registrado por otro paciente")

    existente.nombre = paciente.nombre
    existente.dni = paciente.dni
    db.commit()
    db.refresh(existente)
    return existente



# 🔹 DELETE: eliminar paciente
@router.delete("/{paciente_id}")
def eliminar_paciente(
    paciente_id: int,
    db: Session = Depends(get_db)
):
    existente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    db.delete(existente)
    db.commit()
    return {"mensaje": "Paciente eliminado correctamente"}

