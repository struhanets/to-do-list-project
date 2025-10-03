from fastapi import FastAPI
from tasks.views import router as tasks_router
from task_parser.views import router as task_parser_router
from task_priority.views import router as task_priority_router

app = FastAPI()
app.include_router(tasks_router)
app.include_router(task_parser_router)
app.include_router(task_priority_router)


@app.get("/")
async def root():
    return {"message": "Welcome to New Page"}
