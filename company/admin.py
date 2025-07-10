from django.contrib import admin
from company.models import *

@admin.register(Franquicia)
class FranquiciaAdmin(admin.ModelAdmin):
    list_display = [
        "Nombre",
    ]
    list_filter = ["Nombre"]

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = [
        "Nombre_s",
        "Franquicia"
    ]
    list_filter = ["Nombre_s"]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "Nombre_p",
        "Sucursal",
        "Stock"
    ]
    list_filter = ["Nombre_p"]
