from django.db import models
from django.contrib import admin

class ChartData(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.label + ' - ' + str(self.value)

admin.site.register(ChartData)