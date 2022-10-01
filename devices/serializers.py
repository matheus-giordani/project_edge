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
        
    def to_representation(self, instance):
        return { 
                'device': {'nome':instance.device.nome, 'marca': instance.device.marca, 'modelo': instance.device.modelo},
                'peaple': { 'nome':instance.peaple.nome}
                
                }