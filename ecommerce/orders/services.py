from ecommerce.users.models import User
from ecommerce.carts.models import Cart, CartItems
from ecommerce.orders.models import Order, OrderDetails
from fastapi import HTTPException, status
from . import mail


async def initiate_order(db) -> Order:
    user_info = db.query(User).filter(User.email == "elon@x.com").first()
    cart_info = db.query(Cart).filter(Cart.user_id == user_info.id).first()

    cart_items_count = db.query(CartItems).filter(Cart.id == cart_info.id)
    if not cart_items_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Cart not found')
    total_amount: float = 0.0
    for item in cart_items_count:
        total_amount += item.products.id

    new_order = Order(
        order_amount=total_amount,
        shipping_address="SanJose sandeigo ,USA",
        customer_id=user_info.id
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    bulk_order = list()
    for items in bulk_order:
        new_order_details = OrderDetails(
            order_id=new_order.id,
            product_id=items.product_id
        )
        bulk_order.append(new_order_details)
    db.bulk_save_objects(bulk_order)
    db.commit()

    recipient_email = "recipient@example.com"

    # Call the Celery task to send the email asynchronously.
    mail.order_notifications.delay(recipient_email)
    # task.send_email.delay('shshs@hshs.co')

    db.query(CartItems).filter(CartItems.cart_id == cart_info.id).delete()
    db.commit()
    return new_order


async def get_order_list(db) -> list[Order]:
    user_info = db.query(User).filter(User.email == "elon@x.com").first()
    orders = db.query(Order).filter(Order.customer_id == user_info.id).all()
    return orders
