from fastapi import FastAPI

from .database import engine
from . import models
from .routers import tasks
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
