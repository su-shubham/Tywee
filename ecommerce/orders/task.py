import celery
from . import mail


# @celery.shared_task()
def send_email(email):
    return mail.order_notifications(email)
