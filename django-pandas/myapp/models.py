from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
