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

    # Модульные тесты для CRUD
    # Модульный Тест. Создание задачи.
    def test_create_task(db_session):
        task_data = {"title": "Test Task", "description": "This is a test task"}

        response = client.post("/tasks/create", json=task_data)

        assert response.status_code == 200

        task = response.json()
        task_id = task["id"]
        print(f"\nСозданная задача имеет ID: {task_id}")
        # Проверяем, что заголовок и описание задачи совпадают с отправленными данными
        assert task["title"] == "Test Task"
        assert task["description"] == "This is a test task"

        # Выводим результаты теста
        if response.status_code == 200:
            # Выводим ID созданной задачи
            print("Тест успешно завершен. Полученная задача:")
            print(task)
        else:
            print("Тест неуспешен. \n")

    # Модульный Тест. Получение задачи по ее ID.
    def test_get_task_by_id(db_session):

        task_data = {"title": "Test Task", "description": "This is a test task"}

        response_create = client.post("/tasks/create", json=task_data)

        assert response_create.status_code == 200

        task = response_create.json()
        task_id = task["id"]

        # Выводим ID созданной задачи
        print(f"\nСозданная задача имеет ID: {task_id}")

        # Получение задачи по ее ID
        response_get = client.get(f"/tasks/{task_id}")

        assert response_get.status_code == 200

        fetched_task = response_get.json()

        # Проверяем, что ID задачи соответствует ожидаемому
        assert fetched_task["id"] == task_id

        # Выводим результаты теста
        if response_get.status_code == 200:
            print("Тест успешно завершен. Полученная задача:")
            print(fetched_task)
        else:
            print("Тест неуспешен. \n")

    # Модульный Тест. Обновление задачи по ее ID.
    def test_update_task_by_id(db_session):

        task_data = {"title": "Test Task", "description": "This is a test task"}

        response_create = client.post("/tasks/create", json=task_data)

        assert response_create.status_code == 200

        task = response_create.json()
        task_id = task["id"]

        print(f"\nСозданная задача имеет ID: {task_id}")

        # Подготавливаем данные для обновления задачи
        update_data = {"title": "Updated Task", "description": "This task has been updated"}

        response_update = client.put(f"/tasks/{task_id}", json=update_data)

        assert response_update.status_code == 200

        updated_task = response_update.json()

        # Проверяем, что заголовок и описание задачи обновились
        assert updated_task["title"] == "Updated Task"
        assert updated_task["description"] == "This task has been updated"

        # Выводим результаты теста
        if response_update.status_code == 200:
            print("Тест успешно завершен. Обновленная задача:")
            print(updated_task)
        else:
            print("Тест неуспешен.")

    # Модульный Тест. Удаление задачи по ее ID.
    def test_delete_task_by_id(db_session):

        task_data = {"title": "Test Task", "description": "This is a test task"}

        response_create = client.post("/tasks/create", json=task_data)

        assert response_create.status_code == 200

        task = response_create.json()
        task_id = task["id"]

        print(f"\nСозданная задача имеет ID: {task_id}")

        # Отправляем запрос на удаление задачи по ее ID
        response_delete = client.delete(f"/tasks/{task_id}")

        assert response_delete.status_code == 200

        deleted_task = response_delete.json()

        assert deleted_task["id"] == task_id

        # Выводим результаты теста
        if response_delete.status_code == 200:
            print("Тест успешно завершен. Удаленная задача:")
            print(deleted_task)
        else:
            print("Тест неуспешен.")
