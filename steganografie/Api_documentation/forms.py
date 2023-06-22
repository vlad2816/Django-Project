from django import forms
from .models import HiddenImage


class HiddenImageForm(forms.ModelForm):
    class Meta:
        model = HiddenImage
        fields = ('image', 'text')
