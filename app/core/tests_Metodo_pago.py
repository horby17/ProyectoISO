from django.test import TestCase
from config.wsgi import *
from core.models import MetodoPago
from django.db import connection

def insertar_metodo_pago():
    # Crea una instancia del modelo MetodoPago y asigna los valores
    nuevo_met = MetodoPago(
        metodos_pago='1',
        descripcion='Tarjeta de Credito'
    )

    # Guarda el nuevo método de pago en la base de datos
    nuevo_met.save()

# Llama a la función para realizar la inserción
insertar_metodo_pago()