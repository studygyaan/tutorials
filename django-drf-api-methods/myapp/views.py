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
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
