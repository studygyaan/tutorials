from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import UploadImageForm

def gallery_with_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                GalleryImage.objects.create(image=image)
    else:
        form = UploadImageForm()
    
    gallery = GalleryImage.objects.all()
    return render(request, 'gallery_with_upload.html', {'form': form, 'gallery': gallery})
