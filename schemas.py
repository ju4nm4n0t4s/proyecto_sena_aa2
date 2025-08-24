from pydantic import BaseModel, EmailStr

class EstudianteBase(BaseModel):
    nombre: str
    correo: EmailStr

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(BaseModel):
    nombre: str

class EstudianteOut(EstudianteBase):
    id: int
    class Config:
        from_attributes = True  # pydantic v2 (equivalente a orm_mode)
