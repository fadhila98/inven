from django import forms
from django.db.models.fields import AutoField
from django.forms import fields

from .models import Location

class LocationModelForm(forms.ModelForm):
    location_name = forms.CharField()
    class Meta:
        model = Location
        fields = [
            'location_name',
        ]

