from django import forms
from django.forms import ModelForm
from .models import Rental, Car, CustomerProfile
from django.forms import HiddenInput, CheckboxInput, DateTimeInput

class RentalForm(forms.ModelForm):
    
    Car = forms.ModelChoiceField(queryset=Car.objects.all(),  widget=forms.Select(attrs={'readonly': 'readonly'}))
    Renter = forms.ModelChoiceField(queryset=CustomerProfile.objects.all(),  widget=forms.Select(attrs={'readonly': 'readonly'}))
    
    class Meta:
        model = Rental
        fields = ['Car', 'Renter', 'ReturnDate']

        widgets = {
            'ReturnDate': DateTimeInput(format='%m/%d/%Y %H:%M:%S', attrs={'type': 'datetime-local'}),
        }

class FinishRentForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['FinishedRent']
        widgets = {
            'FinishedRent':forms.CheckboxInput(attrs={'class': 'hidden-field'})
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     for field in self.fields.values():
    #         field.widget.attrs['disabled'] = True
