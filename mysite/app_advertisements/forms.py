from django import forms
from django.db import models
from .models import Adv

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Adv
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control-lg'}),
            'is_auction': forms.CheckboxInput(attrs={'class': 'form-control-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control-lg'})
        }