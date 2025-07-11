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

        # person = "LT1127"
        # person = "SV3975"
        #person = "LT1008"
        sucur = Sucursal.objects.filter(Franquicia=fran).values()
        # print(sucur[0]['id'])
        array_result = []
        # array_result.append({
        #     "Franquicia:" : fran,
        # })
        for sucursal in sucur:
            print(sucursal)
            pro = Producto.objects.filter(Sucursal=sucursal['id']).order_by('-Stock').values()[:2]
            for produc in pro:
                array_result.append({
                    "Sucursal:" : sucursal['Nombre_s'],
                    "Producto:" : produc['Nombre_p'],
                    "Stock:" : produc['Stock']
                })
            print(pro)
        
        # asignacion = AsignacionCuenta.objects.filter(Usuario=id[0]["id"]).values()
        # array_cuentas = [int(cuenta["Cuenta_id"]) for cuenta in asignacion]
        # print(array_cuentas)
        
        # query_raw = "SELECT sky_v_empleados.id, sky_v_empleados.Badge, sky_v_empleados.Nombre AS 'NombreEmpleado', sky_v_empleados.Cuenta, skyroster_cuenta.Nombre, sky_v_empleados.Supervisor, sky_v_empleados.Account, sky_v_empleados.Director FROM (SELECT skyrosterdaily_empleado.id, skyrosterdaily_empleado.Badge, GROUP_CONCAT(DISTINCT CASE WHEN skyrosterdaily_detalleempleado.Propiedad_id = 2 THEN skyrosterdaily_detalleempleado.Valor END) AS 'Nombre', GROUP_CONCAT(DISTINCT CASE WHEN skyrosterdaily_detalleempleado.Propiedad_id = 3 THEN skyrosterdaily_detalleempleado.Valor END) AS 'Cuenta', GROUP_CONCAT(DISTINCT CASE WHEN skyrosterdaily_detalleempleado.Propiedad_id = 10 THEN skyrosterdaily_detalleempleado.Valor END) AS 'Supervisor', GROUP_CONCAT(DISTINCT CASE WHEN skyrosterdaily_detalleempleado.Propiedad_id = 11 THEN skyrosterdaily_detalleempleado.Valor END) AS 'Account', GROUP_CONCAT(DISTINCT CASE WHEN skyrosterdaily_detalleempleado.Propiedad_id = 12 THEN skyrosterdaily_detalleempleado.Valor END) AS 'Director'FROM skyrosterdaily_detalleempleado INNER JOIN skyrosterdaily_empleado ON skyrosterdaily_detalleempleado.Empleado_id = skyrosterdaily_empleado.id GROUP BY skyrosterdaily_empleado.id ) AS sky_v_empleados INNER JOIN skyroster_cuenta ON skyroster_cuenta.id = sky_v_empleados.Cuenta WHERE sky_v_empleados.Cuenta IN (%s);"
        # params = ', '.join(map(str, array_cuentas))
        # print(params)
        # list_skyviewempleados = Empleado.objects.raw(query_raw, [params])
        # print(list_skyviewempleados)
        # array_of_dicts = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        # for employee in list_skyviewempleados:
        #     print(employee)
        #     array_of_dicts.append({
        #         "id": employee.id,
        #         "Badge": employee.Badge,
        #         "NombreEmpleado": employee.NombreEmpleado,
        #         "Cuenta": employee.Nombre,
        #         "Supervisor": employee.Supervisor,
        #         "Account": employee.Account,
        #         "Director": employee.Director,
        #         "CuentaId": employee.Cuenta,
        #     })
        # array_b = [str(emple["Badge"]) for emple in array_of_dicts]
        # excp = ExcepcionR.objects.filter(Badge__in=array_b).values()
        return Response(array_result)