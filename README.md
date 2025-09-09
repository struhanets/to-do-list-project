# Task Manager API
**Author:** Volodymyr Struhanets

---

This backend project demonstrates how to use **FastAPI** together with **Celery** for running asynchronous tasks (for example, fetching users from a public API and saving them into a CSV file). **Redis** is used as the task broker and result backend. Everything runs inside **Docker** via `docker-compose`. The project also functions as a task manager, allowing users to perform standard CRUD operations on their tasks via a RESTful API.

---

## ✨ Features
- 🗒️ **Task management (CRUD)** — create, read, update and delete tasks with fields:  
  `name`, `description`, `creation_date`, `status`, `priority`
- **Asynchronous tasks** — executed in the background with Celery  
- **Task status tracking** — check progress and results via API  
- **External API parsing** — fetch users from [JSONPlaceholder](https://jsonplaceholder.typicode.com/users)  
- **CSV export** — save parsed data into `users.csv`
- **Predicts** the priority of a task ("low" or "high") based on its description.
- **Dockerized environment** — reproducible setup with Docker Compose  
- **FastAPI auto-generated docs** — available at:
  - Swagger UI → `http://localhost:8000/docs`  
  - ReDoc → `http://localhost:8000/redoc`

---

## 📌 Task CRUD Endpoints

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| POST   | `/tasks`              | Create a new task    |
| GET    | `/tasks`              | Get all tasks        |
| PUT    | `/tasks/{task_id}`    | Update a task by ID  |
| DELETE | `/tasks/{task_id}`    | Delete a task by ID  |
| POST   | `/run-task`           | Run background task (parse & save)  |
| GET    | `/task-status/{task_id}`    | Check the status of a Celery task   |
| POST    | `/predict`    | Receives a task description and returns the predicted priority (low or high).   |

---

## 🛠️ Technologies Used

- **Python 3.13**
- **FastAPI 0.116.1** — web framework for building APIs
- **Celery 5.5.3** — distributed task queue for background jobs
- **Redis 6.4.0** — message broker and result backend for Celery
- **Docker & Docker Compose** — containerization and service orchestration
- **Requests 2.32.5** — for fetching data from external APIs
- **CSV module** — for saving parsed data
- **Uvicorn 0.35.0** — ASGI server for FastAPI
- **Pytest 8.4.2** — for testing CRUD operations
- **scikit-learn** (LogisticRegression, CountVectorizer)
- **joblib**


## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/struhanets/to-do-list-project.git
cd to-do-list-project
```
### 2. Build and start the services
```bash
docker-compose up --build
```
---
## 📌 Use CRUD operations for tasks

### 1. Open API docs
Interactive documentation is available at:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

### 2. Use CRUD operations for tasks
You can manage tasks directly via FastAPI:

- POST /tasks → Create a new task

- GET /tasks → Get all tasks

- PUT /tasks/{task_id} → Update a task by ID

- DELETE /tasks/{task_id} → Delete a task by ID

Example request (create task):
```bash
{
  "name": "Write report",
  "description": "Prepare Q3 summary",
  "creation_date": "2025-09-07T12:00:00Z",
  "status": "todo",
  "priority": "high"
}
```

## 📌 Run Celery tasks

### 1. Run task
```bash
curl -X POST http://localhost:8000/run-task
```
Example response:
```bash
{"task_id": "f3c5c9d2-1a2b-4f7f-90a8-123456789abc"}
```
---
### 2. Check task status
```bash
curl http://localhost:8000/task-status/f3c5c9d2-1a2b-4f7f-90a8-123456789abc

```
Example response:
```bash
{"task_id":"cf600df0-fac4-457a-b1dd-c25b699c8772","status":"SUCCESS","result":"Saved 10 users to users.csv"}
```
### Output
users.csv

## 📌 Task Priority Prediction
### 1. Open API docs
Interactive documentation is available at:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

### 2. Test the /predict endpoint
- POST /predict → Analyzes a task description and determines its priority ("low" or "high").

Example response:
```bash
{"priority": "high"}
```

## 🔍 Useful Commands
### View worker logs
```bash
docker logs -f celery_worker
```
### Stop and remove containers, volumes, and networks
```bash
docker-compose down -v
```