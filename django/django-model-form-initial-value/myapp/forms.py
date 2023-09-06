# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CommentForm(forms.Form):
    name = forms.CharField(initial="Your name")
    url = forms.URLField(initial="http://")
    comment = forms.CharField()