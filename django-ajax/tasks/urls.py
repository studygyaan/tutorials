# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('get_tasks/', views.get_tasks, name='get_tasks'),
    path('add_task/', views.add_task, name='add_task'),
]
