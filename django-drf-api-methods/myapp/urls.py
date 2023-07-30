from django.urls import path
from .views import HelloWorldAPIView, BookListView, BookDetailView

urlpatterns = [
    path('hello/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('api/books/', BookListView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
