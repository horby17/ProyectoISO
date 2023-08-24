from django.test import TestCase
from config.wsgi import *
from core.models import Categorias
from django.db import connection

def insertar_categoria():
    # Crea una instancia del modelo Categorias y asigna los valores
    cat = Categorias(
        categoria_codigo='011',
        descripcion='Mancuernas 10'
    )

    cat.save()
insertar_categoria()