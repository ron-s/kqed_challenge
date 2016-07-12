import os
from django.contrib.gis.utils import LayerMapping
from .models import MobileFoodTrucks

trucks_mapping = {
    #remember 10 character limit
    'locationid': 'locationid',
    'applicant': 'applicant',
    'facility': 'facility',
    'block': 'block',
    'address': 'address',
    'permit': 'permit',
    'status': 'status',
    'fooditems': 'fooditems',
    'x': 'x',
    'y': 'y',
    'dayshours': 'dayshours',
    'permit_exp': 'permit_exp',
    'location': 'location',
    'longitude': 'longitude',
    'latitude': 'latitude',
    'geom': 'POINT',
}

# Copypaste from geodjango tutorial.
trucks_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Mobile_Food_Trucks.shp'))


def run(verbose=True):
    lm = LayerMapping(MobileFoodTrucks, trucks_shp, trucks_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)
