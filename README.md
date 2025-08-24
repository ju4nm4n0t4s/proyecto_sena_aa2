# Proyecto SENA AA2-EV01 (FastAPI + SQLite + SQLAlchemy)

## 1) Preparar entorno (VS Code)
- Abre **VS Code** y esta carpeta.
- Crea un entorno virtual:
  - Windows (PowerShell):
    ```powershell
    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```
  - Linux/macOS:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

- Instala dependencias:
  ```bash
  pip install -r requirements.txt
  ```

## 2) Ejecutar
```bash
uvicorn main:app --reload
```
Abre: http://127.0.0.1:8000/docs (Swagger) y prueba el CRUD.

## 3) Versionamiento (Git)
```bash
git init
git add .
git commit -m "feat: CRUD estudiantes con FastAPI y SQLAlchemy"
git branch -M main
# Crea un repo en GitHub y pega su URL:
git remote add origin https://github.com/tuusuario/proyecto_sena_aa2.git
git push -u origin main
```

## 4) Estándar de codificación (opcional pero recomendado)
```bash
pip install black isort flake8
black . && isort . && flake8
git commit -am "style: formateo con black/isort y lint con flake8"
git push
```

## 5) Estructura
```
proyecto_sena_aa2/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
│── README.md
│── .gitignore
```
