from django import forms

class QRCodeForm(forms.Form):
    text_data = forms.CharField(label='Text to Encode', max_length=255)
