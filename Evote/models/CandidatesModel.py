from django.db import models

from ..utils import UtilModel
from django.contrib.auth import get_user_model


User = get_user_model()


class Candidate(UtilModel):
    student = models.ForeignKey(User, verbose_name="Estudiante", on_delete=models.CASCADE)
    position = models.CharField(verbose_name="Posición", max_length=150)
    listInfo = models.ForeignKey("Evote.ListInfo", verbose_name="Lista", on_delete=models.CASCADE)
    foto = models.TextField(blank=True, null=True)
    #status = models.CharField(max_length=1)

    def __str__(self):
        return self.student.username
    
    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['created']