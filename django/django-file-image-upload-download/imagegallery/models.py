from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)
