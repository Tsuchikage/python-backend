from fastapi import FastAPI
import models
from database import engine
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from starlette import status
import requests

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/get_product_info/{product_id}", status_code=status.HTTP_200_OK)
async def get_product_info(product_id: int = Path(gt=0)):
    inventory_service_url = "http://inventory:8000/products/" + str(product_id)
    response = requests.get(inventory_service_url)

    if response.status_code == 200:
        product_info = response.json()
        return product_info
    else:
        raise HTTPException(status_code=404, detail='Product not found in inventory.')


@app.post("/create_order", status_code=status.HTTP_200_OK)
async def create_order(db: db_dependency, product_id: int = Body(...), product_quantity: float = Body(...)):
    inventory_service_url = "http://inventory:8000/products/" + str(product_id)
    response = requests.get(inventory_service_url)
    if response.status_code == 200:
        product_info = response.json()
    else:
        raise HTTPException(status_code=404, detail='Product not found in inventory.')
    order = models.Order(
        product_id=product_info['id'],
        price=product_info['price'],
        fee=0.2 * product_info['price'],
        total=1.2 * product_info['price'],
        quantity=product_quantity,
        status='completed'
    )
    db.add(order)
    db.commit()


@app.get("/orders", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(models.Order).all()
