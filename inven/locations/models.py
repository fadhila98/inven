from django.db import models
from django.db.models import fields
from django.urls import reverse
from products.models import Product
from django.utils import timezone


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.location_name

    def get_absolute_url(self):  
        return reverse("locations:location-detail", kwargs={"id": self.id}) 

