from sqlalchemy.orm import Session
from . import models
from typing import Optional


async def category_exists(category_id: int, database: Session) -> Optional[models.Category]:
    return database.query(models.Category).filter(models.Category.id == category_id).first()
