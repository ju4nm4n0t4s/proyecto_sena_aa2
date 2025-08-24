from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models, database, crud
from schemas import EstudianteCreate, EstudianteOut, EstudianteUpdate

# Crear tablas en la primera ejecución
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SENA AA2-EV01", description="CRUD de Estudiantes con FastAPI + SQLAlchemy + SQLite")

# Dependencia para obtener sesión de BD por solicitud
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudiantes/", response_model=EstudianteOut, status_code=status.HTTP_201_CREATED)
def crear_estudiante(data: EstudianteCreate, db: Session = Depends(get_db)):
    # validar correo único
    existente = db.query(models.Estudiante).filter(models.Estudiante.correo == data.correo).first()
    if existente:
        raise HTTPException(status_code=400, detail="El correo ya existe")
    return crud.crear_estudiante(db, data)

@app.get("/estudiantes/", response_model=List[EstudianteOut])
def listar_estudiantes(db: Session = Depends(get_db)):
    return crud.obtener_estudiantes(db)

@app.get("/estudiantes/{estudiante_id}", response_model=EstudianteOut)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    est = crud.obtener_estudiante(db, estudiante_id)
    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return est

@app.put("/estudiantes/{estudiante_id}", response_model=EstudianteOut)
def actualizar_estudiante(estudiante_id: int, data: EstudianteUpdate, db: Session = Depends(get_db)):
    est = crud.actualizar_estudiante(db, estudiante_id, data)
    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return est

@app.delete("/estudiantes/{estudiante_id}", response_model=EstudianteOut)
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    est = crud.eliminar_estudiante(db, estudiante_id)
    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return est
