from django.urls import path
from .views import HelloWorldAPIView

urlpatterns = [
    path('hello/', HelloWorldAPIView.as_view(), name='hello_world'),
]
