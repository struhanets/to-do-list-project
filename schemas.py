from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from enums import StatusEnum, PriorityEnum


class TaskRequestData(BaseModel):
    id: int
    name: str
    description: Optional[str] = ""
    creation_date: datetime
    status: StatusEnum
    priority: PriorityEnum


class TaskResponseData(BaseModel):
    name: str
    creation_date: datetime
    status: StatusEnum
