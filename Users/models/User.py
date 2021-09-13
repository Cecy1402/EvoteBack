"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """
    identificacion = models.CharField(max_length=100, primary_key=True)

    email = models.EmailField(blank=True, null=True, verbose_name = 'correo electronico')
    
    nombres = models.CharField(max_length=250, blank=True)
    apellidos = models.CharField( max_length=250, blank=True)
    carrera = models.CharField(max_length=250, blank=True, null=True)
    ciclo = models.CharField(max_length=250, blank=True, null=True)
    paralelo = models.CharField(max_length=250, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['identificacion','nombres', 'apellidos']

    def __str__(self):
        """Return username."""
        return '{}'.format(self.username)

    def get_short_name(self):
        """Return username."""
        return '{}'.format(self.username)

    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

