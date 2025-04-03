from django.db import models

# Create your models here.
class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    

    def __str__(self):
        return '{} {}'.format(self.nombre)