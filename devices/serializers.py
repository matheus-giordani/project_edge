from rest_framework import serializers
from . import models



class PeapleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.Peaple


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.Devices
        
class DevicesControlSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = models.DevicesControl