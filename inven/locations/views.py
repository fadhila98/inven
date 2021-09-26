from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Location
from .forms import LocationModelForm

# Create your views here.
class LocationCreateView(CreateView):
    template_name   = 'locations/location_create.html'
    form_class = LocationModelForm
    queryset= Location.objects.all()

class LocationListView(ListView):
    template_name   = 'locations/location_list.html'
    queryset = Location.objects.all()

class LocationDetailView(DetailView):
    template_name   = 'locations/location_detail.html'
    # queryset= Article.objects.all()  #use pk in url

    def get_object(self):    #in url use id instead of pk
        id_= self.kwargs.get("id")
        return get_object_or_404(Location, id=id_)

class LocationDeleteView(DeleteView):
    template_name   = 'locations/location_delete.html'

    def get_object(self):   
        id_= self.kwargs.get("id")
        return get_object_or_404(Location, id=id_)
    
    def get_success_url(self):
        return reverse('locations:location-list')

class LocationUpdateView(UpdateView):
    template_name   = 'locations/location_create.html'
    form_class = LocationModelForm

    def get_object(self):   
        id_= self.kwargs.get("id")
        return get_object_or_404(Location, id=id_)
    
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)




