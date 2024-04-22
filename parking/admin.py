from django.contrib import admin
from rest_framework.authtoken.models import TokenProxy

from .models import ParkingZone

admin.site.register(ParkingZone)

