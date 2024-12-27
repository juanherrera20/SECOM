from django.db import models
from apps.usuarios.models import CustomUser

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)



class Articulo (models.Model):
    estados = {
        "1": "Disponible",
        "2": "Vendido",
        "3": "En proceso",
    }
    
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="articulo")
    estado = models.CharField(max_length=1, default="1", choices=estados)
    fecha_publiacion = models.DateTimeField(auto_now_add=True)
    usuario_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="articulo")
    ubicacion = models.CharField(max_length=40) #Falta configurarla
    
    class Meta:
        verbose_name_plural = "Articulos"
        verbose_name = "Articulo"