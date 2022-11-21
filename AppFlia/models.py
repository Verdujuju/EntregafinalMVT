from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacim = models.DateField()
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre_completo