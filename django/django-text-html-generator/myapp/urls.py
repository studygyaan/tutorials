from django.urls import path
from . import views

urlpatterns = [
    path('', views.convertor_view, name='convertor_view'),
]