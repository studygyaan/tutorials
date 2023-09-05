from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('example1/', views.employees_data, name='employees_data'),
    path('example2/', views.save_employees_data, name='save_employees_data'),
    path('example3/', views.display_table, name='display_table'),
]