from rest_framework import viewsets, permissions
from .models import Ubicacion
from .serializers import UbicacionSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_queryset(self):
        queryset = super().get_queryset()
        departamento = self.request.query_params.get("departamento")
        ciudad = self.request.query_params.get("ciudad")
        tipo_ubicacion = self.request.query_params.get("tipo_ubicacion")

        if departamento:
            queryset = queryset.filter(departamento=departamento)
        if ciudad:
            queryset = queryset.filter(ciudad__icontains=ciudad)
        if tipo_ubicacion:
            queryset = queryset.filter(tipo_ubicacion=tipo_ubicacion)

        return queryset
