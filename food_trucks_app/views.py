from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import MobileFoodTrucks
from .serializers import MobileFoodTruckSerializer

from django.contrib.gis.measure import D
from django.contrib.gis.geos import *


"""
View Controller objects that render serialized JSON data through the Django REST framework.
"""


class MobileFoodTrucksViewSet(viewsets.ModelViewSet):

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('applicant', 'address', 'dayshours', 'fooditems', 'permit', 'permit_exp', 'latitude', 'longitude',)
    queryset = MobileFoodTrucks.objects.all()
    serializer_class = MobileFoodTruckSerializer

    class Meta:
        model = MobileFoodTrucks
        abstract = True


def home_page(request):
    return render(request, 'index.html')



def get_location(request):
    #locate all food trucks within a 1 mile distance from the user

    pnt = fromstr('POINT("latitude", "longitude")', srid=4326)
    qs = MobilefoodTrucks.objects.filter(point__distance_lte=(pnt, D(m=1)))

    return location
