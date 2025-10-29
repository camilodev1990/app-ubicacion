# apps/ubicacion/serializers.py
from rest_framework import serializers
from .models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = [
            "id",
            "departamento",
            "ciudad",
            "via",
            "numero1",
            "numero2",
            "tipo_ubicacion",
            "nombre_ubicacion",
            "detalle_adicional",
            "fecha_creacion",
            "fecha_modificacion",
        ]
        read_only_fields = ["id", "fecha_creacion", "fecha_modificacion"]

