# views.py
from django.shortcuts import render
from .forms import ProductForm, CommentForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
    else:
        form = ProductForm(initial={
            'name': 'New Product',
            'price': 0.00,
        })

    return render(request, 'create_product.html', {'form': form})

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
    else:
        form = CommentForm()

    return render(request, 'create_comment.html', {'form': form})
