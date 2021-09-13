from django.db import models

from ..utils import UtilModel


class VoteInfo(UtilModel):
    period = models.ForeignKey("Evote.Period", on_delete=models.CASCADE, verbose_name = 'periodo')
    whiteVotes = models.IntegerField(verbose_name = 'votos blancos')
    nullVotes = models.IntegerField(verbose_name = 'votos nulos')

    def __str__(self):
        return "id: {0}".format(self.id)


    class Meta:
        verbose_name = 'escrutinio'
        verbose_name_plural = 'escrutinios'