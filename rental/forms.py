from django import forms
from django.forms import ModelForm
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['ReturnDate', 'RentalDate']
