from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('export/', views.export_to_excel, name='export_to_excel'),
]