from celery import Celery
from fastapi import FastAPI
from ecommerce import config
from ecommerce.users import router as user_router
from ecommerce.products import routers as product_router
from ecommerce.carts import router as cart_router
from ecommerce.orders import routers as orders_router

app = FastAPI(title="Ecommerce APP", version="0.0.1")
app.secret_key = "your_secret_key_here"
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(orders_router.router)

celery = Celery(
    __name__,
    broker=f'redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}',
    # backend=f'redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}'
)

celery.conf.imports = [
    'ecommerce.orders.mail'
]
