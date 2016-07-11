from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import MobileFoodTrucks
from .serializers import (MobileFoodtrucksSerializer,)

"""
View Controller objects that render serialized JSON data through the Django REST framework.
"""
class MobileFoodTrucksViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('business_name', 'address', 'hours_of_operation', 'cuisine', 'permit_status' 'permit_exp_date', 'latitude', 'longitude',)
    queryset = MobileFoodTrucks.objects.all()
    serializer_class = MobileFoodTrucksSerializer

    class Meta:
        model = MobileFoodTrucks
        abstract=True


def home_page(request):
    return render(request, 'index.html')