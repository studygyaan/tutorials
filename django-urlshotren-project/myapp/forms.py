from django import forms
from .models import ShortenedURL

class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['long_url']
