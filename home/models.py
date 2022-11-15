from django.db import models
from geopy.geocoders import Nominatim



# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    pincode = models.CharField(max_length=300)
    lat = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="home")
        location = geolocator.geocode(self.pincode)
        self.lat = location.latitude
        self.long = location.longitude
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name  
