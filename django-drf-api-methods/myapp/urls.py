from django.urls import path
from .views import HelloWorldAPIView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, BookView

urlpatterns = [
    path('hello/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('api/books/', BookListView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/', BookCreateView.as_view(), name='book-create'),
    path('api/books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('api/books/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('api/books/', BookView.as_view(), name='book-list'),
    path('api/book/<int:pk>/', BookView.as_view(), name='book-detail'),
]

