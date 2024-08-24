from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Viagem, Destino
from .serializers import ViagemSerializer, DestinoSerializer
from clima.utils import buscar_clima

# Create your views here.

class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        viagem_id = response.data['id']
        buscar_clima(viagem_id)  # Chamada da função após a criação
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        viagem_id = kwargs['pk']
        buscar_clima(viagem_id)  # Chamada da função após a atualização
        return response

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer