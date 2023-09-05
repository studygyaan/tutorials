from django.urls import path
from . import views

urlpatterns = [
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment-status/', views.payment_status, name='payment_status'),
    path('payment-response/', views.payment_response, name='payment_response'),
]