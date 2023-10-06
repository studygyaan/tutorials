from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'email'], name='unique_username_email')
        ]