from django import forms
from . import models


class CityForm(forms.ModelForm):
    class Meta:
        model=models.City
        fields=('name', 'description')


def clean(self):
    cleaned_data = super().clean()
    name = cleaned_data.get('name')

    if name == "Moscow":
        self.add_error('name', 'This name is invalid')
    return cleaned_data    

