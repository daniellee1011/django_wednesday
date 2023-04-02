from django import forms
from django.forms import ModelForm
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': 'Enter your Venue here',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name':  forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Venue name'}),
            'address': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Zip code'}),
            'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Web address'}),
            'email_address': forms.EmailInput(attrs = {'class':'form-control', 'placeholder': 'Email'}),
        }