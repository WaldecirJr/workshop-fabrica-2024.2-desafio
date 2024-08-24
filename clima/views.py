from django.shortcuts import render
from rest_framework import viewsets
from .models import Clima
from .serializers import ClimaSerializer

# Create your views here.

class ClimaViewSet(viewsets.ModelViewSet):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer
