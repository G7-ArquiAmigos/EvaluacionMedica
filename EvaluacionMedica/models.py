from django.db import models
from JuntaMedica.models import JuntaMedica
# Create your models here.
class EvaluacionMedica(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=255)
    resultados = models.CharField(max_length=255)
    recomendaciones = models.TextField()
    JuntaMedica = models.ForeignKey(JuntaMedica,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return '{}'.format(self.id)