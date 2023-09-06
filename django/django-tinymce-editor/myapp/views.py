from django.shortcuts import render
from django.http import HttpResponse
from .forms import YourForm

def home(request):
    form = YourForm()
    return render(request, 'home.html', {'form': form})