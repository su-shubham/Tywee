from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from ecommerce.db import get_db

from . import schema
from . import validators
from . import services

router = APIRouter(tags=['Users'], prefix='/users')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(get_db)):
    user = validators.verify_email_exists(request.email, database)
    if user:
        raise HTTPException(status_code=400, detail=f'User with email already exists')
    new_user = await services.new_user_register(request, database)
    return new_user


@router.get('/', response_model=list[schema.Display_user])
async def get_all_users(database: Session = Depends(get_db)):
    return await services.get_all(database)


@router.get('/{user_id}', response_model=schema.Display_user)
async def get_user_by_id(user_id: int, database: Session = Depends(get_db)):
    return await services.get_user_id(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, database: Session = Depends(get_db)):
    return await services.delete_user(user_id, database)
