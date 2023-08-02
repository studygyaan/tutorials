from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)  # Add the otp

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
