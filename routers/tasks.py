from fastapi import APIRouter, HTTPException
from models.task import Task
from db.fake_db import tasks_db

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/", response_model=list[Task])
def get_tasks():
    return tasks_db


@router.post("/", response_model=Task, status_code=201)
def create_task(task: Task):
    for existing_task in tasks_db:
        if existing_task.id == task.id:
            raise HTTPException(
                status_code=400,
                detail="Task with this ID already exists"
            )

    tasks_db.append(task)
    return task
