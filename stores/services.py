from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry

# import your models here

def get_nearby_stores_within(latitude: float, longitude: float, km: int=10, limit: int=None, srid: int=4326):
    # Your code goes here:
    return None

