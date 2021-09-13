"""Django models utilities."""

# Django
from django.db import models


class UtilModel(models.Model):
    """
    added fields:
        company - state -
        Created - Modified
    """

    created = models.DateTimeField(
        'fecha creacion',
        
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'fecha modificacion',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )
    
    status = models.CharField(verbose_name = 'estado', max_length=100, blank=True, null=True, default="1")

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
