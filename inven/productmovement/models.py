from django.db import models
from locations.models import Location
from products.models import Product
from django.db.models.deletion import CASCADE
from django.urls import reverse


# Create your models here.
class ProductMovement(models.Model):
    # movement_id = models.
    from_location = models.ForeignKey(Location,related_name='location-from+', on_delete=models.CASCADE, default=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    to_location = models.ForeignKey(Location, related_name='location-to+',on_delete=models.CASCADE, default=True,blank= True)
    # qty = models.IntegerField(null=True)
    # qty_to_location = models.IntegerField()
    # product_name= models.ForeignKey(Product,on_delete=CASCADE,primary_key=True)
    
    # @property
    # def get_quantity(self):
    #      if self.from_location== '' and self.to_location != '':
    #         return self.qty_to_location == Product.objects.count
    #     #  elif self.to_location== '' and self.from_location != '':
    #     #     return self.qty_from_location ==+ 1

    
    # def save(self, *args, **kwargs):
    #       self.qty_from_location = self.get_quantity
    #       self.qty_to_location = self.get_quantity
    #       super(ProductMovement, self).save(*args, **kwargs)

    def __str__(self):
        return self.from_location
    
    def get_absolute_url(self):  
        return reverse("productmovement:productmov-detail", kwargs={"id": self.id}) 

    # def set_timezone(request):
    #     if request.method == 'POST':
    #         request.session['django_timezone'] = request.POST['timezone']
