from typing import List

from fastapi import HTTPException

from core.schemas import TaskResponseData, TaskCreate

tasks_storage: list[TaskResponseData] = []
task_id_counter = 0


async def create_task(task_data: TaskCreate) -> TaskResponseData:
    global task_id_counter
    task_id_counter += 1
    new_task = TaskResponseData(id=task_id_counter, **task_data.dict())
    tasks_storage.append(new_task)
    return new_task


async def get_tasks() -> List[TaskResponseData]:
    return tasks_storage


async def update_task(task_id: int, task_update: TaskCreate) -> TaskResponseData:
    for task in tasks_storage:
        if task.id == task_id:
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
            return TaskResponseData(**task.dict())

    raise HTTPException(status_code=404, detail="Task not found")
