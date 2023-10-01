from fastapi import FastAPI

from . import models
from .database import engine
from .database import SessionLocal
from .routers import router

app = FastAPI()

app.include_router(router)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
