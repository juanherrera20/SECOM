from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Aquí se registran los modelos para usuarios


# Extendemos mediante AbstracBaseUser los metodos y atributos del modelo User
class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True, verbose_name="Correo Electronico"
    )
    telefono = models.CharField(max_length=20)
    puntos = models.IntegerField(default=0, verbose_name="Puntos Descuentos")
    reputacion = models.FloatField(
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Calificacion",
    )
    img_profile = models.ImageField(upload_to="ImagenesPerfil", null=True, blank=True)
    username = models.CharField(max_length=150, unique=True, blank=True)

    # Especificamos cual va a ser el reemplazo de username y cuales son los requeridos
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["telefono", "username"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
