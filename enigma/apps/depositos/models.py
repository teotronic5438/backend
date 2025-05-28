from django.db import models

class Deposito(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class StockProducto(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    cantidad_total = models.IntegerField()

    def __str__(self):
        return f"{self.producto} - {self.cantidad_total} en {self.deposito}"
