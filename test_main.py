import pytest
from fastapi import FastAPI

from fastapi.testclient import TestClient
from httpx import AsyncClient

from datetime import datetime
from main import app
from crud import tasks_storage

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_storage():
    tasks_storage.clear()
    yield
    tasks_storage.clear()


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200


def test_add_task():
    mock_data = {
        "name": "Test Task",
        "description": "Some description",
        "creation_date": datetime.now().isoformat(),
        "status": "todo",
        "priority": "low"
    }

    response = client.post("/tasks/", json=mock_data)

    assert response.status_code == 200
    json_data = response.json()
    print(json_data)
    assert "id" in json_data
    assert json_data["name"] == mock_data["name"]
    assert json_data["status"] == mock_data["status"]


def test_update_task():
    mock_data = {
        "name": "Test Task",
        "description": "Some description",
        "creation_date": datetime.now().isoformat(),
        "status": "todo",
        "priority": "low"
    }

    client.post("/tasks/", json=mock_data)
    response = client.put(
        "/tasks/1",
        json={
            "name": "Task",
            "description": "Some description",
            "creation_date": datetime.now().isoformat(),
            "status": "completed",
            "priority": "high"
        },
    )

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 1
    assert json_data["name"] == "Task"
    assert json_data["status"] == "completed"
    assert json_data["priority"] == "high"


def test_delete_task():
    mock_data = {
        "name": "Test Task",
        "description": "Some description",
        "creation_date": datetime.now().isoformat(),
        "status": "todo",
        "priority": "low"
    }

    client.post("/tasks/", json=mock_data)
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 1
    assert json_data["name"] == "Test Task"

