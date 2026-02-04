from sqlalchemy.orm import Session

from . import models, schemas


#Crea ORM, la añade a la sesion, la commitea y refresca para obtener id y fechas

def create_task(db: Session, task: schemas.TaskCreate): 
    db_task = models.Task(
        title=task.title,
        description=task.description,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#Obtener todas las tareas
def get_tasks(
    db: Session,
    completed: bool | None,
    limit: int,
    offset: int
):
    query = db.query(models.Task)

    if completed is not None:
        query = query.filter(models.Task.completed == completed)

    return query.offset(offset).limit(limit).all()




#Obtener una tarea por id
def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

#Si no existe devuelve None


#Actualizar una tarea
def update_task(
    db: Session,
    db_task: models.Task,
    task_update: schemas.TaskUpdate
):
    db_task.title = task_update.title
    db_task.description = task_update.description
    db_task.completed = task_update.completed
    
    db.commit()
    db.refresh(db_task)
    return db_task


#Eliminar una tarea
def delete_task(db: Session, db_task: models.Task):
    db.delete(db_task)
    db.commit()
    