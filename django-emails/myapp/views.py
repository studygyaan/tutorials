from django.shortcuts import render
from django.http import HttpResponse
from .email_utils import send_custom_email, send_email_with_template, send_email_with_attachment
from django.conf import settings

def hello_world(request):
    return HttpResponse("Hello, world!")

def my_email_view(request):
    # ... Your view logic ...

    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    recipient_list = ['recipient@example.com']  # Replace with the recipient's email addresses

    send_custom_email(subject, message, recipient_list)

    # ... Rest of your view logic ...
    return HttpResponse("Normal Email Send Successfully!")

def my_email_template_view(request):
    # ... Your view logic ...

    subject = 'Your Subject'
    recipient_list = ['recipient@example.com']
    template_name = 'email_template.html'
    context = {'username': 'John Doe', 'verification_link': 'http://example.com/verify/123/'}

    send_email_with_template(subject, recipient_list, template_name, context)

    # ... Rest of your view logic ...
    return HttpResponse("Email with Template Sent Successfully!")

def my_email_with_attachment_view(request):
    # ... Your view logic ...

    subject = 'Email with Attachment'
    message = 'Please find the attached file.'
    from_email = 'your_email@example.com'  # Replace with your email address
    recipient_list = ['recipient@example.com']  # Replace with the recipient's email address

    # Attach the file
    # Attach the file from the sibling folder of the templates folder
    attachment_path = 'documents/sample.pdf'  # Replace with the relative path to the file from the root directory

    file_path = settings.BASE_DIR / attachment_path

    send_email_with_attachment(subject, message, from_email, recipient_list, attachment_path)

    # ... Rest of your view logic ...
    return HttpResponse("Email with Attachment Sent Successfully!")