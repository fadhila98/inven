from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from products.models import  Product
from .models import ProductMovement
from .forms import ProductMovementForm
from .models import Location

# Create your views here.
#PRODUCT MOVEMENT
class ProductMovementListView(ListView):
    template_name   = 'productmovement/productmovement_list.html'
    queryset = ProductMovement.objects.all()

class ProductMovementCreateView(CreateView):
    template_name   = 'productmovement/productmovement_create.html'
    form_class = ProductMovementForm
    queryset= Location.objects.all()
    
    
class ProductMovementDetailView(DetailView):
    template_name   = 'productmovement/productmovement_detail.html'
    queryset= ProductMovement.objects.all()  

    def get_object(self):    
        id_= self.kwargs.get("id")
        return get_object_or_404(ProductMovement, id=id_)

class ProductMovementUpdateView(UpdateView):
    template_name   = 'productmovement/productmovement_create.html'
    form_class = ProductMovementForm

    def get_object(self):   
        id_= self.kwargs.get("id")
        return get_object_or_404(ProductMovement, id=id_)

class ProductMovementDeleteView(DeleteView):
    template_name   = 'productmovement/productmovement_delete.html'

    def get_object(self):   
        id_= self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)
    
    def get_success_url(self):
        return reverse('productmovement/productmovement_list.html')