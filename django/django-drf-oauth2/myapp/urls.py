from django.urls import path
from .views import ProtectedResourceView

urlpatterns = [
    path('api/protected-resource/', ProtectedResourceView.as_view(), name='hello_world'),
]
