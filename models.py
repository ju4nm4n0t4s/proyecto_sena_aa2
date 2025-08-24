from sqlalchemy import Column, Integer, String
from database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
