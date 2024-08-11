from typing import List

from pydantic import BaseModel


class CartItemSchema(BaseModel):
    product_id: str
    quantity: float


class OrderSchema(BaseModel):
    user_id: str
    items: List[CartItemSchema]
    total_price: float
    status: str = "pending"
