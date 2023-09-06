from django.shortcuts import render
from .forms import MyForm

def index(request):
    form = MyForm()
    return render(request, 'index.html', {'form': form})