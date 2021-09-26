from django import forms
from django.http import request
from .models import ProductMovement
from products.models import Product


class ProductMovementForm(forms.ModelForm):
    # def product_deets(request,self,*args, **kwargs):
    #     product_name = Product.objects.get(kwargs={'title':Product.title})
    #     self.save()
    
    from_location_qty = Product.objects.count()
    class Meta:
        model= ProductMovement
        fields=[
            'from_location',
            'to_location',
            'product_id',
            'qty',
            
        ]