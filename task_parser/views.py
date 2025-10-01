from celery.result import AsyncResult
from fastapi import APIRouter

from workers.celery_worker import celery_app

router = APIRouter(tags=["Task_parser"])


@router.post("/run-task/")
async def run_task():
    task = celery_app.send_task("task_parser")
    return {"task_id": task.id}


@router.get("/task-status/{task_id}/")
async def get_task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None,
    }
