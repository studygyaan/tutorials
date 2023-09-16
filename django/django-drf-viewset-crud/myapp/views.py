from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
