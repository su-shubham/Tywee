from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from ecommerce.db import get_db
from ecommerce.users.models import User
from ecommerce.carts.models import Cart, CartItems
from ecommerce.products.models import Product
from . import schemas


async def add_items(cart_id, product_id, db: Session = Depends(get_db)):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    db.add(cart_items)
    db.commit()
    db.refresh(cart_items)


async def add_to_cart(product_id, db: Session = Depends(get_db)):
    product_info = db.query(Product).get(product_id)
    if not product_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Product not found!')
    if product_info.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Out of stock!')

    user_info = db.query(User).filter(User.email == "elon@x.com").first()
    cart_info = db.query(Cart).filter(Cart.user_id == user_info.id).first()

    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        db.add(new_cart)
        db.commit()
        db.refresh(new_cart)
        await add_items(new_cart.id, product_info.id, db)

    await add_items(cart_info.id, product_info.id, db)
    return {"status": "Item added to cart"}


async def get_all_cart_items(database) -> schemas.PresentCart:
    user_info = database.query(User).filter(User.email == "elon@x.com").first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    return cart


async def remove_cart_items(cart_item_id: int, database) -> None:
    user_info = database.query(User).filter(User.email == "elon@x.com").first()
    cart_id = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    if not cart_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Cart Items not found')
    database.query(CartItems).filter(and_(CartItems.id == cart_item_id, CartItems.cart_id == cart_id.id)).delete()
    database.commit()
    return
