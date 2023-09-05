from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class MyForm(forms.Form):
    field1 = forms.CharField(label='Field 1')
    field2 = forms.EmailField(label='Field 2')

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('field1', css_class='custom-class'),
            Field('field2', css_class='custom-class'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
