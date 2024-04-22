from django.db import models


class ParkingZone(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    max_count = models.IntegerField(default=0)
    empty_count = models.IntegerField(default=0)
    electro_count = models.IntegerField(default=0)
    empty_electro_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='parking_images/', blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title
