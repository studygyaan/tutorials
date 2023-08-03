from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('email/', views.my_email_view, name='normal-email'),
    path('email-template/', views.my_email_template_view, name='email-template'),
    path('email-attachment/', views.my_email_with_attachment_view, name='email-template'),
]