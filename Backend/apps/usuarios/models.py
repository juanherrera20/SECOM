from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Creación de modelos para el manejo de usuarios, autenticaciones

class CustomUser(AbstractUser):
    puntos = models.IntegerField(default=0,  verbose_name="Puntos Descuentos")
    reputacion = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Calificacion")
    
    