from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from enums import StatusEnum, PriorityEnum


class TaskBase(BaseModel):
    name: str
    description: Optional[str] = ""
    creation_date: datetime
    status: StatusEnum
    priority: PriorityEnum


class TaskCreate(TaskBase):
    pass


class TaskResponseData(TaskBase):
    id: int
    name: str
    creation_date: datetime
    status: StatusEnum
