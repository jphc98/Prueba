from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from company.api.serializers import *
from company.models import *

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

class ProductosSucursal(APIView):

    def get(self, request, format=None):
        fran = request.query_params.get("franquicia")
        sucur = Sucursal.objects.filter(Franquicia=fran).values()
        array_result = []
        for sucursal in sucur:
            pro = Producto.objects.filter(Sucursal=sucursal['id']).order_by('-Stock').values()[:2]
            for produc in pro:
                array_result.append({
                    "Sucursal:" : sucursal['Nombre_s'],
                    "Producto:" : produc['Nombre_p'],
                    "Stock:" : produc['Stock']
                })
        return Response(array_result)