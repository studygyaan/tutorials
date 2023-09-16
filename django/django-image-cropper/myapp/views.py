from django.shortcuts import render
from .forms import ImageUploadForm
from django.http import JsonResponse
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")


def upload_and_crop(request):
    form = ImageUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'works'})
    context = {'form': form}
    return render(request, 'crop.html', context)