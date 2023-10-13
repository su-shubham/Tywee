import datetime
from typing import Optional
from pydantic import BaseModel
from ecommerce.products.schema import ProductCategory


class OrdersDetails(BaseModel):
    id: int
    order_id: int
    product_order_detail: ProductCategory

    class Config:
        from_attributes = True


class Order(BaseModel):
    id: Optional[int]
    order_date: datetime.datetime
    order_amount: float
    order_status: str
    shipping_address: str
    order_details: list[OrdersDetails] = []

    class Config:
        from_attributes = True
