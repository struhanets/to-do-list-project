import pytest

from fastapi.testclient import TestClient

from datetime import datetime
from main import app
from crud import tasks_storage

client = TestClient(app)


@pytest.fixture
def clear_storage():
    tasks_storage.clear()
    with TestClient(app) as c:
        yield c
    tasks_storage.clear()


def test_main_page():
    response = client.get("/")
    message = response.json().get("message")
    assert response.status_code == 200
    assert message == "Welcome to New Page"


def test_add_task(clear_storage):
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
    assert len(tasks_storage) == 1


def test_update_task(clear_storage):
    mock_data = {
        "name": "Test Task",
        "description": "Some description",
        "creation_date": datetime.now().isoformat(),
        "status": "todo",
        "priority": "low"
    }

    response = client.post("/tasks/", json=mock_data)
    task_id = response.json().get("id")
    response = client.put(
        f"/tasks/{task_id}",
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
    assert json_data["id"] == task_id
    assert json_data["name"] == "Task"
    assert json_data["status"] == "completed"
    assert json_data["priority"] == "high"


def test_delete_task(clear_storage):
    mock_data = {
        "name": "Test Task",
        "description": "Some description",
        "creation_date": datetime.now().isoformat(),
        "status": "todo",
        "priority": "low"
    }

    response = client.post("/tasks/", json=mock_data)
    task_id = response.json()["id"]

    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 200

    deleted_data = response.json()
    print(deleted_data)
    assert deleted_data["id"] == task_id
    assert deleted_data["name"] == "Test Task"
    assert len(tasks_storage) == 0
