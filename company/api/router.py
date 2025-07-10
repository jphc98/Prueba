from rest_framework.routers import DefaultRouter

from company.api.views import *

Franquicia_router = DefaultRouter()

Franquicia_router.register(
    prefix="Franquicia",
    basename="Franquicia",
    viewset=FranquiciaViewSet,
)

Sucursal_router = DefaultRouter()

Sucursal_router.register(
    prefix="Sucursal",
    basename="Sucursal",
    viewset=SucursalViewSet,
)

Producto_router = DefaultRouter()

Producto_router.register(
    prefix="Producto",
    basename="Producto",
    viewset=ProductoViewSet,
)