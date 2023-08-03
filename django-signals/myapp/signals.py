from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_registration_notification(sender, instance, created, **kwargs):
    print("Post Save Signal Trigger after Inserting in User Model")
    pass
