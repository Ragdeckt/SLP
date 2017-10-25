
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator
User = get_user_model()


class DatProveedor(models.Model):
    n_proveedor_id = models.AutoField("Numero proveedor",primary_key=True)
    c_proveedor_nombre = models.CharField("Nombre del proveedor",max_length=45)
    c_proveedor_nfiscal = models.CharField("Numero Fiscal",max_length=45)
    c_proveedor_domicilio = models.CharField("Domicilio",max_length=45, blank=True, null=True)
    c_proveedor_colonia = models.CharField("Colonia",max_length=45, blank=True, null=True)
    c_proveedor_telefono = models.CharField("Telefono",max_length=45, blank=True, null=True)
    c_proveedor_fax = models.CharField("Fax",max_length=45, blank=True, null=True)
    c_proveedor_rfc = models.CharField("RFC",max_length=45, blank=True, null=True)
    c_proveedor_cp = models.CharField("CP",max_length=45, blank=True, null=True)
    c_proveedor_ciudad = models.CharField("Ciudad",max_length=45, blank=True, null=True)
    c_proveedor_email = models.CharField("Email",max_length=45, blank=True, null=True)
    n_proveedor_idrel = models.IntegerField()

    def __str__(self):
        return self.c_proveedor_nombre

    class Meta:
        managed = False
        db_table = 'dat_proveedor'


class CatClasificacionPedido(models.Model):
    n_clasificacion_pedido_id = models.AutoField("Numero Pedido",primary_key=True)
    c_clasificacion_pedido_nombre = models.CharField("Nombre de la claseificacion",max_length=45)

    def __str__(self):
        return self.c_clasificacion_pedido_nombre
    class Meta:
        managed = False
        db_table = 'cat_clasificacion_pedido'

class DatPartida(models.Model):
    n_partida_id = models.AutoField(primary_key=True)
    c_partida_nombre = models.CharField("Nombre de la partida",max_length=45)
    n_clasificacion_pedido_id = models.ForeignKey(CatClasificacionPedido, on_delete=models.PROTECT, db_column='n_clasificacion_pedido_id')

    def __str__(self):
        return self.n_partida_id

    class Meta:
        managed = False
        db_table = 'dat_partida'


class CatEstado(models.Model):
    n_estado_id = models.AutoField(primary_key=True)
    c_estado_nombre = models.CharField("Estado",max_length=45)

    def __str__(self):
        return self.c_estado_nombre

    class Meta:
        managed = False
        db_table = 'cat_estado'



class DatRequisicion(models.Model):
    n_requisicion_id = models.AutoField(primary_key=True)
    d_requisicion_fecha = models.DateTimeField("Fecha")
    c_requisicion_solicitante = models.CharField("Solicitante",max_length=45)
    c_requisicion_fuente = models.CharField("Fuente",max_length=45)
    c_requisicion_elabora = models.CharField("Elabora",max_length=45)
    c_requisicion_solicita = models.CharField("Solicita",max_length=45)
    c_requsicion_autoriza = models.CharField("Autoriza",max_length=45)
    n_estado_id = models.ForeignKey(CatEstado, on_delete=models.PROTECT, db_column='n_estado_id')

    def __str__(self):
        return self.n_requisicion_id

    class Meta:
        managed = False
        db_table = 'dat_requisicion'

class CatEstatus(models.Model):
    n_estatus_id = models.AutoField(primary_key=True)
    c_estatus_nombre = models.CharField("Nombre ",max_length=45)

    def __str__(self):
        return self.c_estatus_nombre

    class Meta:
        managed = False
        db_table = 'cat_estatus'


class DatClave(models.Model):
    n_clave_id = models.AutoField(primary_key=True)
    n_clave_num = models.IntegerField("Numero de clave")
    n_clave_precioiva = models.FloatField("precio c/iva")
    c_clave_proceso = models.CharField("Proceso",max_length=45, blank=True, null=True)
    c_clave_presentacion = models.CharField("Presentacion",max_length=45, blank=True, null=True)
    c_clave_descripcion = models.TextField("Descripcion",max_length=45, blank=True, null=True)
    d_clave_fecha = models.DateTimeField("Fecha")


    def __str__(self):
        return self.n_clave_num

    class Meta:
        managed = False
        db_table = 'dat_clave'


class DatContrato(models.Model):
    n_contrato_id = models.AutoField(primary_key=True)
    n_proveedor_id = models.ForeignKey(DatProveedor, on_delete=models.PROTECT, db_column='n_proveedor_id')
    n_partida_id = models.ForeignKey(DatPartida, on_delete=models.PROTECT, db_column='n_partida_id')
    c_contrato_monto = models.FloatField("Monto del contrato", null=False)
    d_contrato_fechainicial = models.DateTimeField("Fecha de inicio del contrato", null=False)
    d_contrato_fechafinal = models.DateTimeField("Fecha de fin del contrato",null=False)
    c_contrato_devengo = models.CharField("Devengo",max_length=45, blank=True, null=True)
    c_contrato_imgcontrato = models.CharField("Imagen del contrato",max_length=45, blank=True, null=True)

    def __str__(self):
        return self.n_contrato_id

    class Meta:
        managed = False
        db_table = 'dat_contrato'


class DatPedido(models.Model):
    n_pedido_id = models.AutoField(primary_key=True)
    n_pedido_numero = models.IntegerField("numero de pedido")
    n_pedido_importetotal = models.FloatField("Importe total")
    c_pedido_fuentefinanciera = models.CharField("Fuente financiera",max_length=45)
    n_requisicion_id = models.ForeignKey(DatRequisicion, on_delete=models.PROTECT, db_column='n_requisicion_id')
    n_partida_id = models.ForeignKey(DatPartida, on_delete=models.PROTECT, db_column='n_partida_id')
    n_clave_id = models.ForeignKey(DatClave, on_delete=models.PROTECT, db_column='n_clave_id')
    c_pedido_proceso = models.CharField("Proceso",max_length=45, blank=True, null=True)
    n_proveedor_id = models.IntegerField("Proveedor")
    n_contrato_id = models.ForeignKey(DatContrato, on_delete=models.PROTECT, db_column='n_contrato_id')
    n_proveedor_cantidad = models.IntegerField("Cantidad")
    n_factura_id = models.IntegerField("")
    n_pedido_precio = models.FloatField("Precio")
    n_pedido_totalclaveciva = models.FloatField("Total clave iva")
    d_pedido_fechaelaboracion = models.DateTimeField("Fecha de elaboracion")
    d_pedido_fechaentrega = models.DateTimeField("Fecha de entrega")
    n_estatus_id = models.ForeignKey(CatEstatus, on_delete=models.PROTECT, db_column='n_estatus_id')

    def __str__(self):
        return self.n_pedido_numero

    class Meta:
        managed = False
        db_table = 'dat_pedido'



class DatFactura(models.Model):
    n_factura_id = models.AutoField(primary_key=True)
    n_factura_numero = models.IntegerField("Numero de factura")
    n_proveedor_id = models.IntegerField("proveedor")
    n_factura_penaconvencional = models.IntegerField("Pena convencional",blank=True, null=True)
    n_requisicion_id = models.IntegerField("Requiicion",blank=True, null=True)
    n_factura_importe = models.FloatField("Importe",blank=True, null=True)
    n_factura_total = models.FloatField("Total",blank=True, null=True)
    n_pedido_id = models.IntegerField()
    n_factura_presupuesto = models.FloatField("Presupuesto")
    d_factura_fechaenvio = models.DateTimeField("Fecha de envio")

    def __str__(self):
        return self.n_factura_numero

    class Meta:
        managed = False
        db_table = 'dat_factura'



