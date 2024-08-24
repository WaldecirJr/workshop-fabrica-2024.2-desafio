from django.shortcuts import render
from rest_framework import viewsets
from .models import Viagem, Destino
from .serializers import ViagemSerializer, DestinoSerializer

# Create your views here.

class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
