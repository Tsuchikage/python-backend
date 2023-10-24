import pytest
from fastapi.testclient import TestClient
from server.payment.main import app
from server.payment.database import engine
from sqlalchemy.orm import sessionmaker

# Определяем тестовый клиент
client = TestClient(app)

# Фикстура для создания временной базы данных
@pytest.fixture(scope="module")
def test_db():
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

# Тест получения информации о товаре
def test_get_product_info():
    product_id = 1
    response = client.get(f"/get_product_info/{product_id}")
    assert response.status_code == 200

# Тест создания заказа
def test_create_order(test_db):
    # Тест создания заказа
    product_id = 1  # Предполагается, что такой товар есть в inventory
    product_quantity = 5
    data = {
        "product_id": product_id,
        "product_quantity": product_quantity
    }
    response = client.post("/create_order", json=data)
    assert response.status_code == 200

def test_read_all_orders(test_db):
    # Тест метода чтения всех заказов
    response = client.get("/orders")
    assert response.status_code == 200

