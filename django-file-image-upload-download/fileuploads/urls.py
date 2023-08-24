from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_and_display_files, name='upload_and_display'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
