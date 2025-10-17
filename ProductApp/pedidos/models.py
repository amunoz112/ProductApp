from django.db import models
from pagos.models import Pago
# Create your models here.
class Pedido(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE,default=None)
    cliente = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Pedido {self.id} de {self.cliente}"
