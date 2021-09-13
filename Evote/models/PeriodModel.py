from django.db import models
from ..utils import UtilModel
from django.db import transaction


class Period(UtilModel):
    startYear = models.DateField(max_length=150, verbose_name = 'fecha inicio')
    endYear = models.DateField(max_length=150, verbose_name = 'fecha fin')
    periodPresent = models.BooleanField(max_length=150, null=True, blank=True, verbose_name = 'actual')
    #status = models.CharField(max_length=1)

    def save(self, *args, **kwargs):
        if not self.periodPresent:
            return super(Period, self).save(*args, **kwargs)
        with transaction.atomic():
            Period.objects.filter(
                periodPresent=True).update(periodPresent=False)
            return super(Period, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} / {1}".format(self.startYear, self.endYear)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'