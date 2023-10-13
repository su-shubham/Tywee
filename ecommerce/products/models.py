from ecommerce.db import Base
from sqlalchemy import String, Column, Text, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    product = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(Text)
    quantity = Column(Integer)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="product")
    cart_items = relationship("CartItems", back_populates="products")
    order_details = relationship("OrderDetails", back_populates="product_order_details")
