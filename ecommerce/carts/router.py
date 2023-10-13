from fastapi import APIRouter, status, Depends
from ecommerce.db import get_db
from sqlalchemy.orm import Session
from . import services
from . import schemas

router = APIRouter(prefix="/cart", tags=['Cart'])


@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_cart(product_id: int, db: Session = Depends(get_db)):
    cart = await services.add_to_cart(product_id, db)
    return cart


@router.get('/', response_model=schemas.PresentCart)
async def get_all_items(database: Session = Depends(get_db)):
    return await services.get_all_cart_items(database)


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart_items(cart_items_id: int, database: Session = Depends(get_db)):
    await services.remove_cart_items(cart_items_id, database)
