from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from config.wsgi import *
from core.models import Pedido, MetodoPago
from django.db import connection


def insertar_pedido():
    fecha_pedido = timezone.make_aware(datetime.strptime('20/08/2023', '%d/%m/%Y'))
    fecha_entrega = timezone.make_aware(datetime.strptime('01/09/2023', '%d/%m/%Y'))

    ped = Pedido(
        codigo_pedido='CODIGO_PEDIDO123',
        cantidad=5,
        total=500,
        fecha_pedido= fecha_pedido,
        fecha_entrega= fecha_entrega,
        metodos_pago=MetodoPago.objects.get(pk='1')
    )
    ped.save()
insertar_pedido()