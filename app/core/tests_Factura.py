from django.test import TestCase
from config.wsgi import *
from core.models import Factura, Cliente
from django.db import connection


def insertar_factura():
    cliente = Cliente.objects.get(cedula_cliente='123344589')

    # Crea una instancia del modelo Factura y asigna los valores
    fac= Factura(
        codigo_factura='CODIGO_FACTURA123',
        cedula_cliente=cliente,  # Asigna la instancia de Cliente
        precio_unidad=100.0,
        cantidad=5,
        impuesto=15.0,
        descuento=10.0
    )

    # Guarda la nueva factura en la base de datos
    fac.save()


# Llama a la función para realizar la inserción
insertar_factura()