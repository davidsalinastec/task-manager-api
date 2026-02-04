# Task Manager API

API REST sencilla para gestión de tareas.

## Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Ejecutar
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
