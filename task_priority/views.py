import os

from fastapi import APIRouter
import joblib

from core.schemas import Task

router = APIRouter(tags=["Prediction"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "priority_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


@router.post("/predict/")
async def task_priority_predict(task: Task):
    map_result = {0: "low", 1: "high"}
    vectors = vectorizer.transform([task.description])
    prediction = model.predict(vectors)
    priority = map_result[prediction[0]]
    return {"priority": priority}
