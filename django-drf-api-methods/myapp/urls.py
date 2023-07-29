from django.urls import path
from .views import HelloWorldAPIView
from .views import BookListView

urlpatterns = [
    path('hello/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('books/', BookListView.as_view(), name='book-list'),
]
