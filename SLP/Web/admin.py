from django.contrib import admin

# Register your models here.
from .models import CatEstado, CatEstatus,CatClasificacionPedido, DatClave, DatContrato,DatFactura,DatPartida,DatPedido,DatProveedor,DatRequisicion

admin.site.register(CatEstatus)
admin.site.register(CatEstado)
admin.site.register(CatClasificacionPedido)
admin.site.register(DatRequisicion)
admin.site.register(DatProveedor)
admin.site.register(DatPedido)
admin.site.register(DatPartida)
admin.site.register(DatClave)
admin.site.register(DatContrato)
admin.site.register(DatFactura)
