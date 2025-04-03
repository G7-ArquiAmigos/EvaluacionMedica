from django.db import models

# Create your models here.
class JuntaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    participantes = models.CharField(max_length=255)
    conclusiones= models.CharField(max_length=255)
    notasAdicionales = models.TextField()
   

    def __str__(self):
        return '{}'.format(self.id)