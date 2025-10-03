import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

celery_app = Celery(
    "worker",
    broker=BROKER_URL,
    backend=BROKER_URL,
    include=["task_parser.task_parser"],
)
