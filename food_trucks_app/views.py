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
        geom = "point"
        abstract = True


# use this for a router only approach

#     def nearest(self, request):
#         latitude = lat
#         longitude = lng
#         point = Point(lat, lng)
#         nearest = self.queryset.filter(point__distance_lte=(point, D(m=1)))
#         serializer = self.get_serializer(nearest, many=True)
#         return Response(serializer.data)


def home_page(request):
    return render(request, 'index.html')


def nearest(request):
    #need to add decorator to prevent any old request from being passed through this function!
    #import pdb; pdb.set_trace()
    if request.method == 'GET':

        lat = float(request.GET['latitude'])
        lng = float(request.GET['longitude'])

        origin = Point(lng, lat)

        nearest = MobileFoodTrucks.objects.filter(point__distance_lte=(origin, D(m=1)))
        serializer = MobileFoodTruckSerializer(nearest, many=True)
        print(serializer.data)
        return Response(serializer.data)
