from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from . import schema
from . import services
from . import validators
from ecommerce import db

router = APIRouter(tags=['Products'], prefix='/products')


@router.post('/category', status_code=status.HTTP_200_OK)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    if not new_category:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Not creating at moment.☹")
    return new_category


@router.get('/category', response_model=list[schema.ListingCategory])
async def get_category(db: Session = Depends(db.get_db)):
    return services.get_all_category(db)


@router.get('/category/{c_id}')
def get_category_by_id(c_id: int, db: Session = Depends(db.get_db)):
    valid = services.get_by_id(c_id, db)
    if not valid:
        raise HTTPException(detail='Category not found', status_code=status.HTTP_404_NOT_FOUND)
    return valid


@router.delete('/category/{c_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(c_id: int, db: Session = Depends(db.get_db)):
    return services.delete_id(c_id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, db: Session = Depends(db.get_db)):
    category = await validators.category_exists(request.category_id, db)
    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Category is invalid.🌀')
    new_product = await services.create_product(request, db)
    return new_product


@router.get('/', response_model=list[schema.ProductCategory])
async def get_category_products(database: Session = Depends(db.get_db)):
    return await services.get_category_products(database)
