from django.db import models
from apps.usuarios.models import CustomUser

from apps.ubicacion.models import Ubicacion
# Creamos nuestros modelos aquí

#Modelo de Categoria
class Categoria (models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    
    #Metadatos
    class Meta: 
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"
    #Definir como se mostrara el objeto en string
    def __str__(self):
        return self.nombre


#Modelo de Articulo
class Articulo (models.Model):
    estados = {
        "1": "Disponible",
        "2": "Vendido",
        "3": "En proceso",
    }
    
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="articulo")
    estado = models.CharField(max_length=1, default="1", choices=estados, verbose_name="Estado del articulo")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="articulo")
    ubicacion = models.OneToOneField(Ubicacion, on_delete=models.CASCADE, related_name="articulo")
    
    class Meta:
        verbose_name_plural = "Articulos"
        verbose_name = "Articulo"
        
    def __str__(self):
        return self.nombre + " - " + self.usuario.username
    

#Modelo para las etiquetas
class Etiqueta (models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Etiquetas"
        verbose_name = "Etiqueta"
        
    def __str__(self):
        return self.nombre


#Modelo para la relacion muchos a muchos entre articulos y etiquetas
class ArticuloEtiqueta (models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="etiquetas")
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, related_name="articulos")
    
    class Meta:
        verbose_name_plural = "Articulos Etiquetas"
        verbose_name = "Articulo Etiqueta"
        
    def __str__(self):
        return self.articulo.nombre + " - " + self.etiqueta.nombre