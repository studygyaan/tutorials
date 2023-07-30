from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

# PUT Method
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DELETE Method
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Combining Methods in the View
class BookView(APIView):
    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Book.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)