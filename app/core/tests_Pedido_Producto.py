from django.test import TestCase
from config.wsgi import *
from core.models import PedidoProducto, Pedido, Producto
from django.db import connection

def insertar_Pedido_Producto():
    Pro = Producto.objects.get(codigo_producto='CODIGO123')
    Ped = Pedido.objects.get(codigo_pedido='CODIGO_PEDIDO123')
    PeProd = PedidoProducto (
        codigo_pedidoproducto='09422',
    )
    PeProd.save()
insertar_Pedido_Producto()