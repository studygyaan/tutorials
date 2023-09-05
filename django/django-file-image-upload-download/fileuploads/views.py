from django.shortcuts import render, redirect
from .models import UploadedFile, UploadedImage
from .forms import UploadFileForm, UploadFileForm2, UploadImageForm
from django.http import HttpResponse

def upload_and_display_files(request):
    files = UploadedFile.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                UploadedFile.objects.create(file=uploaded_file)
            return redirect('upload_and_display')
    else:
        form = UploadFileForm()

    return render(request, 'upload_and_display.html', {'form': form, 'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm2()
    files = UploadedFile.objects.all()
    return render(request, 'upload_file.html', {'form': form, 'files': files})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadImageForm()
    images = UploadedImage.objects.all()
    return render(request, 'upload_image.html', {'form': form, 'images': images})