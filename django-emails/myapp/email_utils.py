from django.core.mail import send_mail
from django.conf import settings

def send_custom_email(subject, message, recipient_list):
    # Send the email using Django's send_mail function
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)