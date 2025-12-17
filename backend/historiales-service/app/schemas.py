from pydantic import BaseModel

class HistorialBase(BaseModel):
    paciente_id: int
    descripcion: str

class HistorialCreate(HistorialBase):
    pass

class HistorialResponse(HistorialBase):
    id: int

    class Config:
        from_attributes = True
