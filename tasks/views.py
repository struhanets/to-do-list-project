from typing import List

from fastapi import APIRouter

from core.schemas import TaskCreate, TaskResponseData
from . import crud

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponseData)
async def create_task(new_task: TaskCreate):
    new_task_created = await crud.create_task(new_task)
    return new_task_created


@router.get("/", response_model=List[TaskResponseData])
async def get_tasks():
    tasks = await crud.get_tasks()
    return tasks


@router.put("/{task_id}/", response_model=TaskResponseData)
async def update_task(task_id: int, new_task_data: TaskCreate):
    new_task = await crud.update_task(task_id, new_task_data)
    return new_task


@router.delete("/{task_id}/", response_model=TaskResponseData)
async def delete_task(task_id: int):
    deleted_task = await crud.delete_task(task_id)

    return deleted_task
