from django.db import models

# Create your models here.
class Pago(models.Model):
    banco = models.CharField(max_length=50)
    monto = models.IntegerField()
    
    def __str__(self):
        return f"Pago de {self.monto} | ({self.banco})"
