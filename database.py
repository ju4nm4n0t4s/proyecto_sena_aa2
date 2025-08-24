from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base de datos SQLite local (archivo sena.db en la raíz del proyecto)
DATABASE_URL = "sqlite:///./sena.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)  # necesario en SQLite para hilos

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
