from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float

from server.inventory.database import Base


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


class InventoryRequest(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
