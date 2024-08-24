from rest_framework import serializers
from .models import Viagem, Destino

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

class ViagemSerializer(serializers.ModelSerializer):
    destinos = DestinoSerializer(many=True, read_only=True)

    class Meta:
        model = Viagem
        fields = '__all__'