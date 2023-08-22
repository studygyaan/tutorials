from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    raise Exception('This is a test error')
    # return HttpResponse("Hello, world!")


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

