from django.db import models

class Remito(models.Model):
    numero_remito = models.CharField(max_length=20)
    numero_viaje = models.IntegerField()
    detalle_transporte = models.CharField(max_length=30)
    deposito = models.ForeignKey('depositos.Deposito', on_delete=models.PROTECT)
    fecha_ingreso = models.DateTimeField()
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)

    def __str__(self):
        return self.numero_remito

class RemitoProducto(models.Model):
    remito = models.ForeignKey(Remito, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    actualizado = models.DateTimeField()

class RemitoDespacho(models.Model):
    remito_despacho = models.OneToOneField(Remito, on_delete=models.CASCADE)
