from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorias(models.Model):
    categoria_codigo = models.CharField(db_column='Categoria_Codigo', primary_key=True, max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorias'


class Cliente(models.Model):
    cedula_cliente = models.CharField(db_column='Cedula_Cliente', primary_key=True, max_length=30)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Factura(models.Model):
    codigo_factura = models.CharField(db_column='Codigo_Factura', primary_key=True, max_length=30)  # Field name made lowercase.
    cedula_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cedula_Cliente', blank=True, null=True)  # Field name made lowercase.
    precio_unidad = models.FloatField(db_column='Precio_Unidad', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    impuesto = models.FloatField(db_column='Impuesto', blank=True, null=True)  # Field name made lowercase.
    descuento = models.FloatField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'


class MetodoPago(models.Model):
    metodos_pago = models.CharField(db_column='Metodos_Pago', primary_key=True, max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class Pedido(models.Model):
    codigo_pedido = models.CharField(db_column='Codigo_Pedido', primary_key=True, max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    fecha_pedido = models.DateTimeField(db_column='Fecha_Pedido', blank=True, null=True)  # Field name made lowercase.
    fecha_entrega = models.DateTimeField(db_column='Fecha_Entrega', blank=True, null=True)  # Field name made lowercase.
    metodos_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='Metodos_Pago', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProducto(models.Model):
    codigo_pedidoproducto = models.CharField(db_column='Codigo_PedidoProducto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Codigo_Producto', blank=True, null=True)  # Field name made lowercase.
    codigo_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='Codigo_Pedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido_producto'


class Producto(models.Model):
    codigo_producto = models.CharField(db_column='Codigo_Producto', primary_key=True, max_length=30)  # Field name made lowercase.
    nombre_producto = models.CharField(db_column='Nombre_Producto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion_producto = models.CharField(db_column='Descripcion_Producto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    precio_unidad = models.FloatField(db_column='Precio_Unidad', blank=True, null=True)  # Field name made lowercase.
    no_existencia = models.IntegerField(db_column='No_Existencia', blank=True, null=True)  # Field name made lowercase.
    categoria_codigo = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='Categoria_Codigo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoFactura(models.Model):
    codigo_productofactura = models.CharField(db_column='Codigo_ProductoFactura', primary_key=True, max_length=30)  # Field name made lowercase.
    codigo_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='Codigo_Factura', blank=True, null=True)  # Field name made lowercase.
    codigo_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Codigo_Producto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_factura'


class Proveedor(models.Model):
    cedula_proveedor = models.CharField(db_column='Cedula_Proveedor', primary_key=True, max_length=30)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nombre_empresa = models.CharField(db_column='Nombre_Empresa', max_length=30, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'


class ProveedorProductoentrante(models.Model):
    codigo_productoentrante = models.CharField(db_column='Codigo_ProductoEntrante', primary_key=True, max_length=30)  # Field name made lowercase.
    codigo_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Codigo_Producto', blank=True, null=True)  # Field name made lowercase.
    cedula_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='Cedula_Proveedor', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    costo = models.FloatField(db_column='Costo', blank=True, null=True)  # Field name made lowercase.
    fecha_entrante = models.DateTimeField(db_column='Fecha_Entrante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor_productoentrante'
