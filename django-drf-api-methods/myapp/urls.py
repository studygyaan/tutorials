from django.urls import path
from .views import HelloWorldAPIView, BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('hello/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('api/books/', BookListView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/', BookCreateView.as_view(), name='book-create'),
]
