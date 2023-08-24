from django.test import TestCase
from config.wsgi import *
from core.models import Producto, Categorias
from django.db import connection


def insertar_producto():
    # Crea una instancia del modelo Producto y asigna los valores
    pro = Producto(
        codigo_producto='CODIGO123',
        nombre_producto='Mancuernas',
        descripcion_producto='10 libras',
        precio_unidad=99.99,
        no_existencia=100,
        categoria_codigo=Categorias.objects.get(pk='011')  # Asegúrate de reemplazar '1' con la clave primaria correcta
    )

    # Guarda el nuevo producto en la base de datos
    pro.save()


# Llama a la función para realizar la inserción
insertar_producto()

