import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task():
    task_data = {
        "id": 1,
        "title": "Test task",
        "completed": False
    }

    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test task"
