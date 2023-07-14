from rest_framework import serializers
from app.models import Edificio, Departamento

class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'  # Include all fields of the model

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'  # Include all fields of the model
