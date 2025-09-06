# --- Ajuste para importar módulos desde la raíz del proyecto ---
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
# ---------------------------------------------------------------

import pytest
from fastapi.testclient import TestClient

from main import app
import database, models

client = TestClient(app)

def setup_module(module):
    # Reiniciar la BD antes de la suite
    models.Base.metadata.drop_all(bind=database.engine)
    models.Base.metadata.create_all(bind=database.engine)

def test_crear_estudiante_ok():
    payload = {"nombre": "Ana Perez", "correo": "ana@example.com"}
    r = client.post("/estudiantes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["id"] > 0
    assert data["nombre"] == payload["nombre"]
    assert data["correo"] == payload["correo"]

def test_crear_estudiante_correo_duplicado():
    payload = {"nombre": "Juan", "correo": "ana@example.com"}
    r = client.post("/estudiantes/", json=payload)
    assert r.status_code in (400, 409, 422)

def test_listar_estudiantes():
    r = client.get("/estudiantes/")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_actualizar_estudiante():
    r = client.get("/estudiantes/")
    est_id = r.json()[0]["id"]
    upd = {"nombre": "Ana María", "correo": "ana@example.com"}
    r2 = client.put(f"/estudiantes/{est_id}", json=upd)
    assert r2.status_code in (200, 202)
    assert r2.json()["nombre"] == "Ana María"

def test_eliminar_estudiante():
    r = client.get("/estudiantes/")
    est_id = r.json()[0]["id"]
    r2 = client.delete(f"/estudiantes/{est_id}")
    assert r2.status_code in (200, 204)
