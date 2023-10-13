from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ecommerce.db import get_db
from . import schema
from . import services

router = APIRouter(prefix='/orders', tags=['Orders'])


@router.post('/')
async def initiate_order(db: Session = Depends(get_db)):
    result = await services.initiate_order(db)
    return result


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schema.Order])
async def order_list(db: Session = Depends(get_db)):
    return await services.get_order_list(db)
