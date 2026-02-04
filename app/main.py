from fastapi import FastAPI

from .database import engine
from . import models
from .routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
