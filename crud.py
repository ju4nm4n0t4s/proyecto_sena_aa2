from sqlalchemy.orm import Session
from models import Estudiante
from schemas import EstudianteCreate, EstudianteUpdate

def crear_estudiante(db: Session, data: EstudianteCreate) -> Estudiante:
    est = Estudiante(nombre=data.nombre, correo=data.correo)
    db.add(est)
    db.commit()
    db.refresh(est)
    return est

def obtener_estudiantes(db: Session):
    return db.query(Estudiante).all()

def obtener_estudiante(db: Session, estudiante_id: int):
    return db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()

def actualizar_estudiante(db: Session, estudiante_id: int, data: EstudianteUpdate):
    est = obtener_estudiante(db, estudiante_id)
    if not est:
        return None
    est.nombre = data.nombre
    db.commit()
    db.refresh(est)
    return est

def eliminar_estudiante(db: Session, estudiante_id: int):
    est = obtener_estudiante(db, estudiante_id)
    if not est:
        return None
    db.delete(est)
    db.commit()
    return est
