from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import MobileFoodTrucks
from .serializers import MobileFoodTruckSerializer

from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point



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




# class MobileFoodTrucksNearestView(viewsets.ModelViewSet):


#     point = Point(lng, lat)

#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ('applicant', 'address', 'dayshours', 'fooditems', 'permit', 'permit_exp', 'latitude', 'longitude',)
#     queryset = MobileFoodTrucks.objects.all()
#     queryset = queryset.filter(point__distance_lte=(point, D(m=1)))
#     serializer_class = MobileFoodTruckSerializer

#     class Meta:
#         model = MobileFoodTrucks
#         abstract = True


# def home_page(request):
#     return render(request, 'index.html')