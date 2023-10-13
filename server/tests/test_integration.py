import pytest
from fastapi.testclient import TestClient

from server.src.app import app
from server.src.app import engine
from server.src.app import models
from server.src.database import SessionLocal

client = TestClient(app)


class Tests:
    # Фикстура для создания сессии базы данных
    @pytest.fixture(scope="module")
    def db_session(self):
        models.Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Интеграционный тест. Создание и получение задачи.
    def test_create_and_get_task(db_session):

        task_data = {"title": "Test Task", "description": "This is a test task"}

        response_create = client.post("/tasks/create", json=task_data)

        assert response_create.status_code == 200

        task = response_create.json()
        task_id = task["id"]

        print(f"\nСозданная задача имеет ID: {task_id}")

        response_get = client.get(f"/tasks/{task_id}")

        assert response_get.status_code == 200

        fetched_task = response_get.json()

        assert fetched_task["title"] == "Test Task"
        assert fetched_task["description"] == "This is a test task"

        if response_get.status_code == 200:
            print("Интеграционный тест успешно завершен. Полученная задача:")
            print(fetched_task)
        else:
            print("Интеграционный тест неуспешен.")

    # Интеграционный Тест. Создание, обновление и удаление задачи.
    def test_create_update_and_delete_task(db_session):

        task_data = {"title": "Test Task", "description": "This is a test task"}

        response_create = client.post("/tasks/create", json=task_data)

        assert response_create.status_code == 200

        task = response_create.json()
        task_id = task["id"]

        print(f"\nСозданная задача имеет ID: {task_id}")

        update_data = {"title": "Updated Task", "description": "This task has been updated"}

        response_update = client.put(f"/tasks/{task_id}", json=update_data)

        assert response_update.status_code == 200

        updated_task = response_update.json()

        assert updated_task["title"] == "Updated Task"
        assert updated_task["description"] == "This task has been updated"

        print(f"Обновленная задача имеет ID: {task_id}")

        response_delete = client.delete(f"/tasks/{task_id}")

        assert response_delete.status_code == 200

        deleted_task = response_delete.json()

        assert deleted_task["id"] == task_id

        if response_delete.status_code == 200:
            print("Тест успешно завершен. Удаленная задача:")
            print(deleted_task)
        else:
            print("Тест неуспешен.")
