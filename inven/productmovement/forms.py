from django import forms
from django.http import request
from .models import ProductMovement
from products.models import Product


class ProductMovementForm(forms.ModelForm):
    
    from_location_qty = Product.objects.count()
    class Meta:
        model= ProductMovement
        fields=[
            'from_location',
            'to_location',
            'product_id',
            
        ]