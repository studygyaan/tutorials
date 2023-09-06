# translator_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.translator_home, name='translator_home'),
    path('translate_text/', views.translate_text, name='translate_text'),
]
