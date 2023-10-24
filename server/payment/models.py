from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float

from server.payment.database import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    price = Column(Float)
    fee = Column(Float)
    total = Column(Float)
    quantity = Column(Integer)
    status = Column(String)


class OrderRequest(BaseModel):
    price: float = Field(gt=0)
    fee: int = Field(gt=0)
    total: int = Field(gt=0)
    quantity: int = Field(gt=0)
    status: str = Field(min_length=3)
