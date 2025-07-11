from django.urls import path, include

from company.api.router import *
from company.api.views import ProductosSucursal

urlpatterns = [
    path("v1/", include(Franquicia_router.urls)),
    path("v1/", include(Sucursal_router.urls)),
    path("v1/", include(Producto_router.urls)),
    path("v1/Prodxs", ProductosSucursal.as_view()),

]