from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    motivo = Column(String, nullable=False)
