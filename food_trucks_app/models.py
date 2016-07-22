# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class MobileFoodTrucks(models.Model):
    locationid = models.IntegerField()
    applicant = models.CharField(max_length=254)
    facility = models.CharField(max_length=254)
    block = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    permit = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    fooditems = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    dayshours = models.CharField(max_length=254)
    permit_exp = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    geom = models.PointField(srid=-1)

    def __str__(self):
        return 'Business Name:' + " " + str(self.applicant) + " " + 'Cuisine:' + " " + self.fooditems + " "
