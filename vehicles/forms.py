from django import forms
from .models import Vehicledata

class VehicledataModelForm(forms.ModelForm):
    class Meta:
        model = Vehicledata
        fields = [
           'vehiclenumber',
            'Averagespeed', 
            'Enginestatus', 
            'FuelLevel',
            'Temperature',
        ]
