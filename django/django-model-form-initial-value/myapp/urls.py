from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    path('create_comment/', views.create_comment, name='create_comment'),
]