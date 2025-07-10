from django.urls import path, include

from company.api.router import *

urlpatterns = [
    path("v1/", include(Franquicia_router.urls)),
    path("v1/", include(Sucursal_router.urls)),
    path("v1/", include(Producto_router.urls)),
]