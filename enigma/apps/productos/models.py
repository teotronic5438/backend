from django.db import models

class Producto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    deposito = models.ForeignKey('depositos.Deposito', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Equipo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    numero_serie = models.CharField(max_length=20, unique=True)
    fecha_alta = models.DateTimeField()
    observaciones = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.numero_serie
