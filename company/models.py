from django.db import models

class Franquicia(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name="Nombre Franquicia")

    class Meta:
        verbose_name = "Franquicia"
        verbose_name_plural = "Franquicias"

    def __str__(self):
        return self.Nombre

class Sucursal(models.Model):
    Nombre_s = models.CharField(max_length=100, verbose_name="Nombre Sucursal")
    Franquicia = models.ForeignKey(Franquicia, on_delete=models.CASCADE, verbose_name="Franquicia")    

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.Nombre_s

class Producto(models.Model):
    Nombre_p = models.CharField(max_length=100, verbose_name="Nombre Producto")
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, verbose_name="Sucursal")
    Stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.Nombre_p