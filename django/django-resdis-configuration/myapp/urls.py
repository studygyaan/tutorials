from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('cached_view/', views.cached_view, name='cached_view'),
]