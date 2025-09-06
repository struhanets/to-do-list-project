from typing import List

from fastapi import FastAPI

from schemas import TaskCreate, TaskResponseData

import crud

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/tasks", response_model=TaskResponseData)
async def create_task(new_task: TaskCreate):
    new_task_created = await crud.create_task(new_task)
    return new_task_created


@app.get("/tasks", response_model=List[TaskResponseData])
async def get_tasks():
    tasks = await crud.get_tasks()
    return tasks


@app.put("/tasks/{task_id}", response_model=TaskResponseData)
async def update_task(task_id: int, new_task_data: TaskCreate):
    new_task = await crud.update_task(task_id, new_task_data)
    return new_task


@app.delete("/tasks/{task_id}", response_model=TaskResponseData)
async def delete_task(task_id: int):
    deleted_task = await crud.delete_task(task_id)

    return deleted_task
