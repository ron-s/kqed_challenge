from django.db import models

# Create your models here.
class MobileFoodTrucks(models.Model):
    objectid = models.IntegerField()
    business_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    cuisine = models.CharField(max_length=254)
    hours_of_operation = models.CharField(max_length=254)
    permit_status = models.CharField(max_length=254)
    permit_exp_date = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    



    def __str__(self):
        return 'Business Name:' + " " + str(self.business_name) + " " + 'Address:' + self.address + " " + 'Hours of Operation:' + self.hours_of_operation + " " + 'Cuisine:' + self.cuisine + " " + 'cuisine:' + self.cuisine