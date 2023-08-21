from django.shortcuts import render
from .forms import MyForm

def hello_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            pass
    else:
        form = MyForm()

    return render(request, 'home.html', {'form': form})
