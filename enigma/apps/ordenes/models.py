from django.db import models

class Estado(models.Model):
    nombre_estado = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_estado

class Orden(models.Model):
    remito = models.ForeignKey('remitos.Remito', on_delete=models.PROTECT)
    producto = models.ForeignKey('productos.Producto', on_delete=models.PROTECT)
    equipo = models.ForeignKey('productos.Equipo', on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    falla_detectada = models.CharField(max_length=50, blank=True)
    reparacion = models.CharField(max_length=50, blank=True)
    fecha_revision = models.DateTimeField(null=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    orden_activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.ForeignKey('usuarios.Usuario', related_name='modificaciones', on_delete=models.PROTECT)

class HistorialOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    fecha_modificacion = models.DateTimeField(auto_now=True)
