from django.db import models
from Medico.models import Medico
# Create your models here.
class DiagnosticoMedico(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    tipo = models.CharField(max_length=255)
    descripcion = models.TextField()
    recomendaciones = models.TextField()
    medico =models.ForeignKey(Medico, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.id)
