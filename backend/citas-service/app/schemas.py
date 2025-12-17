from datetime import date
from pydantic import BaseModel

class CitaBase(BaseModel):
    paciente_id: int
    fecha: date
    motivo: str

class CitaCreate(CitaBase):
    pass

class CitaResponse(CitaBase):
    id: int

    class Config:
        from_attributes = True
