from pydantic import BaseModel

class PacienteBase(BaseModel):
    nombre: str
    dni: str

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id: int

    class Config:
        from_attributes = True
