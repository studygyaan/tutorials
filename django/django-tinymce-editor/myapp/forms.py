# forms.py
from django import forms
from tinymce.widgets import TinyMCE

class YourForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        fields = ['title', 'content']
