from ecommerce.db import Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from .hashing import get_password_hash, verify_password


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    cart = relationship("Cart", back_populates="user_cart")
    order = relationship("Order", back_populates="user_info")

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = get_password_hash(password)

    def check_password(self, password):
        return verify_password(
            self.password,
            password
        )
