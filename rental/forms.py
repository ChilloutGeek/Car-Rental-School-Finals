from django import forms
from django.forms import ModelForm
from .models import Rental
from django.forms import HiddenInput

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['Car', 'Renter']

class FinishRentForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['FinishedRent']
