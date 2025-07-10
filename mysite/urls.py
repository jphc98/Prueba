"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser, IsAuthenticated

schema_view = get_schema_view(
    openapi.Info(
        title="Prueba técnica - Neoris",
        default_version='v1',
        description="Documentacion API: Franquicia, Sucursal, Producto",
        # terms_of_service="pagina :3",
        contact=openapi.Contact(email="jphc1998@hotmail.com"),
        license=openapi.License(name="Juan Pablo Hincapié Cárdenas"),
    ),
    public=True,
)
""" public=False,
permission_classes=(IsAuthenticated,IsAdminUser), """

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/", include("company.urls")),
]
