from django.db import models

class ShortenedURL(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("URL", unique=True)
