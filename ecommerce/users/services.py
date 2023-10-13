from . import models
from fastapi import HTTPException, status


async def new_user_register(request, database) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def get_all(db) -> list[models.User]:
    users = db.query(models.User).all()
    return users


async def get_user_id(user_id, db) -> models.User:
    query_users = db.query(models.User).get(user_id)
    if not query_users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'User with {user_id} is not found 😀!')
    return query_users


async def delete_user(user_id, db):
    user = db.query(models.User).filter(models.User.id == user_id).delete()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {user_id} doesn't exists")
    db.commit()
