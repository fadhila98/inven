from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
                                CreateView,
                                DetailView,
                                ListView,
                                UpdateView,
                                DeleteView
                                )
from .models import Product
from .forms import ProductForm
# Create your views here.

class ProductListView(ListView):
    template_name   = 'products/products_list.html'
    queryset= Product.objects.all()

class ProductDetailView(DetailView):
    template_name   = 'products/products_detail.html'
    # queryset= Article.objects.all()  #use pk in url

    def get_object(self):    #in url use id instead of pk
        id_= self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

class ProductCreateView(CreateView):
    template_name   = 'products/products_create.html'
    form_class = ProductForm
    queryset= Product.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        
    # def get_success_url(self):
    #     return '/'

class ProductUpdateView(UpdateView):
    template_name   = 'products/products_create.html'
    form_class = ProductForm
    
    def get_object(self):   
        id_= self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    template_name   = 'products/products_delete.html'

    def get_object(self):    #in url use id instead of pk
        id_= self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)
    
    def get_success_url(self):
        return reverse('products:product-list')