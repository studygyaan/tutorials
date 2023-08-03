from celery import shared_task

@shared_task
def send_email_task(recipient_email, message):
    # Code to send the email
    # ...
    return f"Email sent to {recipient_email}"