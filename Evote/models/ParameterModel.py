from django.db import models
from ..utils import UtilModel

class Parameter(UtilModel):
    code = models.CharField(max_length=150, verbose_name = 'codigo')
    value = models.CharField(max_length=150, verbose_name = 'valor')
    description = models.CharField(max_length=150, verbose_name = 'descripcion')
    #status = models.CharField(max_length=1)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Parametro'
        verbose_name_plural = 'Parametros'
