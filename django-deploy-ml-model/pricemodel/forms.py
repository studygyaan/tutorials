from django import forms

class PricePredictionForm(forms.Form):
    bedrooms = forms.IntegerField(label='Bedrooms', min_value=0)
    bathrooms = forms.IntegerField(label='Bathrooms', min_value=0)
    sqft_living = forms.IntegerField(label='Sqft Living', min_value=0)
    sqft_lot = forms.IntegerField(label='Sqft Lot', min_value=0)
    floors = forms.DecimalField(label='Floors', min_value=0, decimal_places=1)
    waterfront = forms.BooleanField(label='Waterfront', required=False)
    view = forms.IntegerField(label='View', min_value=0)
    condition = forms.IntegerField(label='Condition', min_value=1, max_value=5)
