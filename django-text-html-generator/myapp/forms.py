from django import forms
from ckeditor.widgets import CKEditorWidget

class MyForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget(), label='')