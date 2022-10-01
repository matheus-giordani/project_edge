from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class PeapleView(viewsets.ModelViewSet):
    queryset = models.Peaple.objects.all()
    serializer_class = serializers.PeapleSerializer
    
class DevicesView(viewsets.ModelViewSet):
    queryset = models.Devices.objects.all()
    serializer_class = serializers.DevicesSerializer
    
class DevicesControlView(viewsets.ModelViewSet):
    queryset = models.DevicesControl.objects.all()
    serializer_class = serializers.DevicesControlSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['device','peaple' ]