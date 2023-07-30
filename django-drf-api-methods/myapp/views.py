from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

# Get Method
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Get Method with Parameter
class BookListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        publication_year = self.request.query_params.get('publication_year', None)

        if publication_year is not None:
            queryset = queryset.filter(publication_date__year=publication_year)

        return queryset

# Get One Method
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# POST Method
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
