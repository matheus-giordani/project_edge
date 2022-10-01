from django.contrib import admin

# Register your models here
from . import models 

admin.site.register(models.Devices)
admin.site.register(models.Peaple)