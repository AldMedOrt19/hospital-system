from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Historial(Base):
    __tablename__ = "historiales"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, nullable=False)
    descripcion = Column(String, nullable=False)
