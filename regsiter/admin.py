from django.contrib import admin
from rest_framework.authtoken.models import TokenProxy

from regsiter.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
