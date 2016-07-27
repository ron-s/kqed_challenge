# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point


class MobileFoodTrucks(geomodels.Model):
    locationid = geomodels.IntegerField()
    applicant = geomodels.CharField(max_length=254)
    facility = geomodels.CharField(max_length=254)
    block = geomodels.CharField(max_length=254)
    address = geomodels.CharField(max_length=254)
    permit = geomodels.CharField(max_length=254)
    status = geomodels.CharField(max_length=254)
    fooditems = geomodels.CharField(max_length=254)
    latitude = geomodels.FloatField()
    longitude = geomodels.FloatField()
    dayshours = geomodels.CharField(max_length=254)
    permit_exp = geomodels.CharField(max_length=254)
    location = geomodels.CharField(max_length=254)
    point = geomodels.PointField(srid=-1)

    def __str__(self):
        return 'Business Name:' + " " + str(self.applicant) + " " + 'Cuisine:' + " " + self.fooditems + " "

    def save(self, *args, **kwargs):
        self.point = Point(self.latitude, self.longitude)
        super(MobileFoodTrucks, self).save(*args, **kwargs)
