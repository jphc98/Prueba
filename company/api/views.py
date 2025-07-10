from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from company.api.serializers import *

class FranquiciaViewSet(ModelViewSet):
    serializer_class = FranquiciaSerializer
    queryset = Franquicia.objects.all()
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "id": ["exact"],
        "Nombre": ["exact"],
    }

class SucursalViewSet(ModelViewSet):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "id": ["exact"],
        "Nombre_s": ["exact"],
    }

class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "id": ["exact"],
        "Nombre_p": ["exact"],
    }