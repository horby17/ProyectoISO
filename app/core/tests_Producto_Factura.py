from django.test import TestCase
from config.wsgi import *
from core.models import ProductoFactura, Factura, Producto
from django.db import connection

def insertar_Producto_Factura():
    fac = Factura.objects.get(codigo_factura='CODIGO_FACTURA123')
    pro = Producto.objects.get(codigo_producto='CODIGO123')
    PrFac = ProductoFactura(
        codigo_productofactura= '00023',
    )
    PrFac.save()
insertar_Producto_Factura()