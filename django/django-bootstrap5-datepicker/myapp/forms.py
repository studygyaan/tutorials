from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'datetime']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
            'time': forms.TimeInput(attrs={'class': 'timepicker'}),
            'datetime': forms.TextInput(attrs={'class': 'datetimepicker'}),
        }