from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from config.wsgi import *
from core.models import ProveedorProductoentrante, Proveedor, Producto
from django.db import connection

def insertar_proveedor_producto_entrante():
    fecha_entrante = timezone.make_aware(datetime.strptime('20/08/2023', '%d/%m/%Y'))
    producto = Producto.objects.get(codigo_producto='CODIGO123')  # Asegúrate de que este código de producto exista
    proveedor = Proveedor.objects.get(cedula_proveedor='CEDULA123')  # Asegúrate de que esta cédula de proveedor exista

    # Crea una instancia de ProveedorProductoentrante y asigna los valores
    proveedor_producto_entrante = ProveedorProductoentrante(
        codigo_productoentrante='CODIGO_ENTRANTE123',
        codigo_producto=producto,
        cedula_proveedor=proveedor,
        cantidad=4,
        costo=30.0,
        fecha_entrante=fecha_entrante,
    )

    # Guarda la nueva entrada de proveedor producto entrante en la base de datos
    proveedor_producto_entrante.save()

# Llama a la función para realizar la inserción
insertar_proveedor_producto_entrante()