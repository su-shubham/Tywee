from pydantic import BaseModel, constr


class Category(BaseModel):
    name: constr(min_length=1, max_length=50)


class ListingCategory(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    id: int
    name: str
    description: str
    quantity: int
    price: float

    class Config:
        from_attributes = True


class Product(ProductBase):
    category_id: int


class ProductCategory(ProductBase):
    category: ListingCategory

    class Config:
        from_attributes = True
