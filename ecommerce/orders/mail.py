from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType
import celery

conf = ConnectionConfig(
    MAIL_USERNAME="12028bfbefdd9f",
    MAIL_PASSWORD="52d0e864ffdc2e",
    MAIL_FROM="bot@replyloop.com",
    MAIL_PORT=587,
    MAIL_SERVER="sandbox.smtp.mailtrap.io",
    MAIL_FROM_NAME="Fastapi testing",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)
fm = FastMail(conf)
subject = "HELLO TESTING"
body = "TESTIGN NOT WORKED"


@celery.shared_task()
async def order_notifications(recipient_email):
    message = MessageSchema(
        subject=subject,
        recipients=[recipient_email],
        body=body,
        subtype="html",
    )
    await fm.send_message(message)
