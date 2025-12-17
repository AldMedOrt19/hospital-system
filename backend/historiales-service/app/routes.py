from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import SessionLocal
from app.models import Historial
from app.schemas import HistorialCreate, HistorialResponse

router = APIRouter(prefix="/historiales", tags=["Historiales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def paciente_existe(db: Session, paciente_id: int) -> bool:
    res = db.execute(text("SELECT 1 FROM pacientes WHERE id = :id"), {"id": paciente_id}).first()
    return res is not None

# ✅ GET: listar historiales
@router.get("/", response_model=list[HistorialResponse])
def listar_historiales(db: Session = Depends(get_db)):
    return db.query(Historial).all()

# ✅ GET: obtener por id
@router.get("/{historial_id}", response_model=HistorialResponse)
def obtener_historial(historial_id: int, db: Session = Depends(get_db)):
    historial = db.query(Historial).filter(Historial.id == historial_id).first()
    if not historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    return historial

# ✅ POST: crear historial
@router.post("/", response_model=HistorialResponse)
def crear_historial(historial: HistorialCreate, db: Session = Depends(get_db)):
    if not paciente_existe(db, historial.paciente_id):
        raise HTTPException(status_code=400, detail="El paciente_id no existe")

    nuevo = Historial(paciente_id=historial.paciente_id, descripcion=historial.descripcion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# ✅ PUT: actualizar historial
@router.put("/{historial_id}", response_model=HistorialResponse)
def actualizar_historial(historial_id: int, historial: HistorialCreate, db: Session = Depends(get_db)):
    existente = db.query(Historial).filter(Historial.id == historial_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Historial no encontrado")

    if not paciente_existe(db, historial.paciente_id):
        raise HTTPException(status_code=400, detail="El paciente_id no existe")

    existente.paciente_id = historial.paciente_id
    existente.descripcion = historial.descripcion
    db.commit()
    db.refresh(existente)
    return existente

# ✅ DELETE: eliminar historial
@router.delete("/{historial_id}")
def eliminar_historial(historial_id: int, db: Session = Depends(get_db)):
    existente = db.query(Historial).filter(Historial.id == historial_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Historial no encontrado")

    db.delete(existente)
    db.commit()
    return {"mensaje": "Historial eliminado correctamente"}
