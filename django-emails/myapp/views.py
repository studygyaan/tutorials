from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")

from .email_utils import send_custom_email
def my_email_view(request):
    # ... Your view logic ...

    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    recipient_list = ['recipient@example.com']  # Replace with the recipient's email addresses

    send_custom_email(subject, message, recipient_list)

    # ... Rest of your view logic ...
    return HttpResponse("Normal Email Send Successfully!")