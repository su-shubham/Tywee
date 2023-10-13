from . import models
from fastapi import HTTPException, status


async def create_new_category(request, database):
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


def get_all_category(database) -> list[models.Category]:
    category = database.query(models.Category).all()
    return category


def get_by_id(c_id, database) -> models.Category:
    category_id = database.query(models.Category).get(c_id)
    return category_id


def delete_id(c_id, database):
    category = database.query(models.Category).filter(models.Category.id == c_id).delete()
    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found!")
    database.commit()


async def create_product(request, db):
    product = models.Product(name=request.name, quantity=request.quantity, description=request.description,
                             price=request.price, category_id=request.category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


async def get_category_products(db) -> list[models.Product]:
    products = db.query(models.Product).all()
    return products
