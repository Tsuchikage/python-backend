from fastapi import FastAPI
from pydantic import BaseModel
from routers import router

app = FastAPI()

app.include_router(router)


class GreetRequest(BaseModel):
    name: str
