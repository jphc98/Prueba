from rest_framework.serializers import ModelSerializer

from company.models import *

class FranquiciaSerializer(ModelSerializer):
    class Meta:
        model = Franquicia
        fields = "__all__"

class SucursalSerializer(ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"