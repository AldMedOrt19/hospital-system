from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import SessionLocal
from app.models import Cita
from app.schemas import CitaCreate, CitaResponse

router = APIRouter(prefix="/citas", tags=["Citas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def paciente_existe(db: Session, paciente_id: int) -> bool:
    # consultamos directo a la tabla pacientes (está en la misma BD)
    res = db.execute(text("SELECT 1 FROM pacientes WHERE id = :id"), {"id": paciente_id}).first()
    return res is not None

# ✅ GET: listar citas
@router.get("/", response_model=list[CitaResponse])
def listar_citas(db: Session = Depends(get_db)):
    return db.query(Cita).all()

# ✅ GET: obtener por id
@router.get("/{cita_id}", response_model=CitaResponse)
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

# ✅ POST: crear cita (valida paciente_id)
@router.post("/", response_model=CitaResponse)
def crear_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    if not paciente_existe(db, cita.paciente_id):
        raise HTTPException(status_code=400, detail="El paciente_id no existe")

    nueva = Cita(paciente_id=cita.paciente_id, fecha=cita.fecha, motivo=cita.motivo)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# ✅ PUT: actualizar cita
@router.put("/{cita_id}", response_model=CitaResponse)
def actualizar_cita(cita_id: int, cita: CitaCreate, db: Session = Depends(get_db)):
    existente = db.query(Cita).filter(Cita.id == cita_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Cita no encontrada")

    if not paciente_existe(db, cita.paciente_id):
        raise HTTPException(status_code=400, detail="El paciente_id no existe")

    existente.paciente_id = cita.paciente_id
    existente.fecha = cita.fecha
    existente.motivo = cita.motivo
    db.commit()
    db.refresh(existente)
    return existente

# ✅ DELETE: eliminar cita
@router.delete("/{cita_id}")
def eliminar_cita(cita_id: int, db: Session = Depends(get_db)):
    existente = db.query(Cita).filter(Cita.id == cita_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Cita no encontrada")

    db.delete(existente)
    db.commit()
    return {"mensaje": "Cita eliminada correctamente"}
