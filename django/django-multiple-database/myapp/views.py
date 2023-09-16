from django.shortcuts import render
from django.http import HttpResponse
from .models import MySQLModel, PostgresModel


def hello_world(request):
    return HttpResponse("Hello, world!")


def my_view(request):
    mysql_data = MySQLModel.objects.using('mysql_db').all()
    postgres_data = PostgresModel.objects.using('postgres_db').all()
    # Your view logic here
