from django.forms import ModelForm
from django.core import validators
from django import forms
from .models import Item


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields=['name','quantity', 'status']
        widgets ={
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'quantity': forms.TextInput(attrs={'class':'form-control'}),
        'status': forms.Select(attrs={'class':'form-control'}),
        }