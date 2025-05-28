from django.db import models

class Destino(models.Model):
    nombre_destino = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_destino

class Pallet(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.PROTECT)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_despacho = models.DateTimeField(null=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    remito = models.ForeignKey('remitos.Remito', on_delete=models.PROTECT)

class OrdenDestino(models.Model):
    orden = models.ForeignKey('ordenes.Orden', on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.PROTECT)
    equipo = models.ForeignKey('productos.Equipo', on_delete=models.PROTECT)
    pallet = models.ForeignKey(Pallet, on_delete=models.SET_NULL, null=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
