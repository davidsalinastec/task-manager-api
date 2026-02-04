from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class TaskResponse(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True