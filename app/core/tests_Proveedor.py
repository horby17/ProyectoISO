from django.test import TestCase
from config.wsgi import *
from core.models import Proveedor
from django.db import connection


def insertar_proveedor():
    # Crea una instancia del modelo Proveedor y asigna los valores
    prov = Proveedor(
        cedula_proveedor='CEDULA199',
        nombre='Karla wer',
        apellido='ruiz rew',
        nombre_empresa='Nomb Empresa',
        direccion='Managua',
        telefono=1234567890,
        correo='correo@proveedor.com',
        estatus='Activo'
    )

    # Guarda el nuevo proveedor en la base de datos
    prov.save()


# Llama a la función para realizar la inserción
insertar_proveedor()