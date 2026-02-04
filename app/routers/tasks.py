from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    return crud.create_task(db, task)

@router.get("/", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{task_id}", response_model=schemas.TaskResponse)
def read_task_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    db_task = crud.get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    db_task = crud.get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return crud.update_task(db, db_task, task_update)

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    db_task = crud.get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    crud.delete_task(db, db_task)
    return {"message": "Tarea eliminada"}


