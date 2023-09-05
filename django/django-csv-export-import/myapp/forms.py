from django import forms

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()