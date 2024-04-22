from rest_framework import serializers
from .models import ParkingZone


class ParkingZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingZone
        fields = ['id', 'title', 'image', 'rating', 'phoneNumber', 'max_count', 'empty_count', 'electro_count',
                  'empty_electro_count', 'lat', 'lon']
