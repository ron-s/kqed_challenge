from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import MobileFoodTrucks
from .serializers import MobileFoodTruckSerializer
from rest_framework.response import Response

from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from geopy import distance as geodistance

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

#issue bad request response


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def nearest(request):
    #need to add decorator to prevent any old request from being passed through this function!
    #import pdb; pdb.set_trace()
    radius = float(request.GET['radius'])
    lat = float(request.GET['latitude'])
    lng = float(request.GET['longitude'])
    origin = Point(lat, lng)
    #import pdb; pdb.set_trace()
    trucks = MobileFoodTrucks.objects.all()

    for truck in trucks:
        print(geodistance.distance(origin, truck.point).miles)

    nearby = [truck for truck in trucks if geodistance.distance(origin, truck.point).miles <= radius]
    print(len(nearby))
    #nearest = MobileFoodTrucks.objects.filter(point__distance_lte=(origin, D(mi=1)))
 
    serializer = MobileFoodTruckSerializer(nearby, many=True)
    return Response(serializer.data)
