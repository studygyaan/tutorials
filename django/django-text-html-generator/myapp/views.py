from django.shortcuts import render
from .forms import MyForm

def convertor_view(request):
    form = MyForm()
    return render(request, 'index.html', {'form': form})
