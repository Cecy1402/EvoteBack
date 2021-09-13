from django.db import models
from ..utils import UtilModel


class ListInfo(UtilModel):
    period = models.ForeignKey("Evote.Period", verbose_name = 'Periodo', on_delete=models.CASCADE)
    name = models.CharField(verbose_name = 'Nombre', max_length=150)
    number = models.IntegerField(verbose_name = 'Numero')
    slogan = models.CharField(verbose_name = 'Eslogan', max_length=150, blank=True, null=True)
    votes = models.IntegerField(verbose_name = 'Votos', default=0)
    foto = models.TextField(blank=True, null=True)
    #status = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
