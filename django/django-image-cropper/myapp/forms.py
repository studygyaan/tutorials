from django import forms
from .models import CroppedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = CroppedImage
        fields = ('file',)