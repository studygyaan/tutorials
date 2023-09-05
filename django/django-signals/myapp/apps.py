from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals
        from .signals import custom_signal
        custom_signal.connect(myapp.signals.custom_signal_handler)