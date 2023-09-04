from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    datetime = models.DateTimeField()