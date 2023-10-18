import pytest
from fastapi.testclient import TestClient
from server.inventory import models
from server.inventory.database import SessionLocal, engine
from server.inventory.main import app

client = TestClient(app)

# Создаем фикстуру для создания сессии базы данных
@pytest.fixture(scope="module")
def db_session():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Тест создание товара.
def test_create_product(db_session):
    inventory_data = {
        "name": "Test Product",
        "price": 10,
        "quantity": 100
    }

    response = client.post("/create", json=inventory_data)

    # Выводим результаты теста
    if response.status_code == 201:
        print("Тест успешно завершен. Созданный товар:")
    else:
        print("Тест неуспешен.")
