from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('crop-image/', views.upload_and_crop, name='upload_and_crop'),
]