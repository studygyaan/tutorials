from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.dispatch import Signal

@receiver(post_save, sender=User)
def send_registration_notification(sender, instance, created, **kwargs):
    print("Post Save Signal Trigger after Inserting in User Model")
    pass

# Create a custom signal
custom_signal = Signal()

def custom_signal_handler(sender, **kwargs):
    # Code to perform custom actions
    print("Custom Signal is Triggered!")
    pass