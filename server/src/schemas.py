from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str = None


class TaskUpdate(BaseModel):
    title: str
    description: str = None


class Task(BaseModel):
    id: int
    title: str
    description: str = None


class TaskDelete(BaseModel):
    task_id: int
