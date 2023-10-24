from fastapi import FastAPI
from celery_worker import create_order
from model import Order

app = FastAPI()


@app.post('/create_order')
def add_order(order: Order):
    create_order.delay(order.product_name, order.order_quantity)
    return {"message": "Order Received!"}
