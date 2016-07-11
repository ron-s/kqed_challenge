from django.db import models

# Create your models here.
class mobile_food_trucks(models.Model):
    locationid = models.IntegerField()
    applicant = models.CharField(max_length=254)
    facility = models.CharField(max_length=254)
    descriptio = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    block_lot = models.CharField(max_length=254)
    block = models.CharField(max_length=254)
    lot = models.CharField(max_length=254)
    permit = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    food_items = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.CharField(max_length=254)
    days_hours = models.CharField(max_length=254)
    approved = models.CharField(max_length=254)
    received = models.CharField(max_length=254)
    priorpermi = models.IntegerField()
    exp_date = models.CharField(max_length=254)
    location = models.CharField(max_length=254)