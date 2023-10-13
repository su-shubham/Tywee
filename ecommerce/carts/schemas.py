from pydantic import BaseModel
from ecommerce.products.schema import Product


class CartItems(BaseModel):
    id: int
    products: Product

    class Config:
        from_attributes = True


class PresentCart(BaseModel):
    id: int
    cart: list[CartItems] = []

    class Config:
        from_attributes = True
