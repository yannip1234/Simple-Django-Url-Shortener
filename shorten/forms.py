from crispy_forms.bootstrap import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class CreateURLForm(forms.Form):
    original_url = forms.URLField(label=False, widget=forms.URLInput(
        attrs={'placeholder': "https://yanni.dev/"}))
    shortened_path = forms.CharField(label=False, max_length=64)

    def __init__(self, *args, **kwargs):
        super(CreateURLForm, self).__init__(*args, **kwargs)
        print(args)
        if 'error' in args:
            self.fields['shortened_path'].widget.attrs['class'] = 'is-invalid'
