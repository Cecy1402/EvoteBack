from django.db import models
from ..utils import UtilModel
from django.contrib.auth import get_user_model

User = get_user_model()
class VoteStudent(UtilModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'estudiante')
    period = models.ForeignKey("Evote.Period", on_delete=models.CASCADE, verbose_name = 'periodo')

    def __str__(self):
        return self.student.username

    class Meta:
        verbose_name = 'Voto estudiante'
        verbose_name_plural = 'Votos estudiantes'