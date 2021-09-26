from django import forms
from .models import Product

class ProductForm (forms.ModelForm):
    title       = forms.CharField(
                    widget= forms.TextInput(attrs=
                    {"placeholder":"Your title"}))
    description = forms.CharField(required= False,
                    widget=forms.Textarea(
                    attrs={
                        "placeholder": "Your description",
                        "class": "new-class-name two",
                        "id": "my-id",
                        "rows": 12,
                        "cols" : 20,
                    }
                )
                )
    price       = forms.DecimalField()
    class Meta:
        model   = Product
        fields= [
            'title',
            'description',
            'price'
        ]