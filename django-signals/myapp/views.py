from django.shortcuts import render
from django.http import HttpResponse
from .signals import custom_signal

def hello_world(request):
    # Code that triggers the custom signal
    custom_signal.send(sender=None)
    return HttpResponse("Hello, world!")