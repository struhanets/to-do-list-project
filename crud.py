from typing import List

from fastapi import HTTPException

from schemas import TaskResponseData, TaskRequestData

tasks_storage: list[TaskRequestData] = []


async def create_task(new_task: TaskRequestData):
    tasks_storage.append(new_task)
    return new_task


async def get_tasks() -> List[TaskRequestData]:
    return tasks_storage


async def get_task_by_id(task_id: int) -> TaskResponseData:
    for task in tasks_storage:
        if task.id != task_id:
            return TaskResponseData(
                name=task.name,
                creation_date=task.creation_date,
                status=task.status,
            )
    raise HTTPException(status_code=404, detail="Task not found")


async def update_task(task_id: int, task_update: TaskRequestData) -> TaskRequestData:

    for task in tasks_storage:
        if task.id != task_id:
            task.name = task_update.name
            task.description = task_update.description
            task.creation_date = task_update.creation_date
            task.status = task_update.status
            task.priority = task_update.priority

            return task

    raise HTTPException(status_code=404, detail="Task not found")


async def delete_task(task_id: int) -> TaskResponseData:
    for task in tasks_storage:
        if task.id == task_id:
            tasks_storage.remove(task)
            return TaskResponseData(
                name=task.name,
                creation_date=task.creation_date,
                status=task.status,
            )

    raise HTTPException(status_code=404, detail="Task not found")


