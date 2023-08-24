from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery_with_upload, name='gallery_with_upload'),
]
