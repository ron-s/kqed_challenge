from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import MobileFoodTrucks

"""
Serializes geospatial fields from models into GeoJSON data.
"""


class MobileFoodTruckSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MobileFoodTrucks
        geo_field = 'point'
        fields = ('applicant', 'address', 'fooditems', 'dayshours', 'status', 'permit_exp', 'latitude', 'longitude', 'point')
