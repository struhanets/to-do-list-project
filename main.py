from typing import List

import joblib
from fastapi import FastAPI
from celery.result import AsyncResult

from celery_worker import celery_app
from schemas import TaskCreate, TaskResponseData, Task
import crud

app = FastAPI()

model = joblib.load("priority_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.get("/")
async def root():
    return {"message": "Welcome to New Page"}


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


@app.post("/run-task")
async def run_task():
    task = celery_app.send_task("task_parser")
    return {"task_id": task.id}


@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }


@app.post("/predict")
async def task_priority_predict(task: Task):
    map_result = {0: "low", 1: "high"}
    vectors = vectorizer.transform([task.description])
    prediction = model.predict(vectors)
    priority = map_result[prediction[0]]
    return {"priority": priority}
