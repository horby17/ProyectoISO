from django.test import TestCase
from config.wsgi import *
from core.models import Cliente
from django.db import connection


#select * from tabla
#listar
"""

query = Cliente.objects.all()
print(query)"""
""""
#insertar
c = Cliente(
    cedula_cliente='1256789',
    nombre='Juan',
    apellido='Perez',
    direccion='Calle 123',
    telefono=5555555
)

"""

""""
cliente, created = Cliente.objects.get_or_create(
    cedula_cliente='1234342342589',
    defaults={
        'nombre': 'mdfdn',
        'apellido': 'Pefvsf',
        'direccion': 'Calle 123',
        'telefono': 5555555}
)
if created:
    print("Nuevo cliente creado:", cliente)
else:
    print("Cliente existente:", cliente)
"""

#eliminar
"""
cedula_cliente_a_eliminar = '1256789'  # Cambia este valor por la cédula correcta

try:
    # Intenta obtener el cliente por su cédula y eliminarlo
    cliente = Cliente.objects.get(cedula_cliente=cedula_cliente_a_eliminar)
    cliente.delete()
    print("Cliente eliminado con éxito:", cliente)
except Cliente.DoesNotExist:
    print("El cliente con la cédula {} no existe.".format(cedula_cliente_a_eliminar))
"""

#actualizar
"""
cedula_a_actualizar = '1234342342589'

# Define los nuevos valores para los campos
nuevos_valores = {
    'nombre': 'Nuevo Nombre',
    'apellido': 'Nuevo Apellido',
    'direccion': 'Nueva Dirección',
    'telefono': 9999999
}

try:
    # Intenta obtener el cliente por su cédula
    cliente = Cliente.objects.get(cedula_cliente=cedula_a_actualizar)

    # Actualiza los campos del cliente con los nuevos valores
    cliente.__dict__.update(**nuevos_valores)
    cliente.save()

    print("Cliente con cédula", cedula_a_actualizar, "actualizado con éxito")
except Cliente.DoesNotExist:
    print("No se encontró ningún cliente con cédula", cedula_a_actualizar)
"""


"""
#buscar
cedula_a_buscar = '1234342342589'

try:
    # Intenta obtener el cliente por su cédula
    cliente = Cliente.objects.get(cedula_cliente=cedula_a_buscar)

    # Imprime los datos del cliente
    print("Cédula:", cliente.cedula_cliente)
    print("Nombre:", cliente.nombre)
    print("Apellido:", cliente.apellido)
    print("Dirección:", cliente.direccion)
    print("Teléfono:", cliente.telefono)
except Cliente.DoesNotExist:
    print("No se encontró ningún cliente con cédula", cedula_a_buscar)
"""