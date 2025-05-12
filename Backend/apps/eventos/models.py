from django.db import models
from apps.usuarios.models import CustomUser
from apps.ubicacion.models import Ubicacion
from django.utils.text import slugify
import os


#-------------------Función para subir las imagenes de los eventos-------------------
def get_image_upload_path(instance, filename):
    # Obtener el nombre del evento y limpiarlo para usarlo como carpeta
    eventos_name = slugify(instance.evento.nombre)
    
    # Construir la ruta
    return os.path.join('Eventos', eventos_name, 'Imagenes', filename)
#-----------------------------------------------------------------------------------------

# Modelos Aquí

class Evento (models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField()
    causa = models.CharField(max_length=50)
    #Los campos OneToOneField se usan para establecer una relación uno a uno 
    ubicacion = models.OneToOneField(Ubicacion, related_name="evento", on_delete=models.CASCADE)
    organizador = models.ForeignKey(CustomUser, related_name="evento", on_delete=models.CASCADE)
    donacion = models.ForeignKey('Donacion', related_name="evento", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        
    def __str__(self): 
        return f"{self.nombre} - {self.fecha}"
    
    
class Imagen(models.Model):
    evento = models.ForeignKey(Evento, related_name="imagenes", on_delete=models.CASCADE)
    url_imagen = models.ImageField(upload_to=get_image_upload_path, max_length=250)
    orden = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.evento.nombre} - {self.url_imagen}"
    
    #Función para eliminar los archivos cuando se eliminan de la base de datos
    def delete(self, *args, **kwargs): #Llamamos al metodo delete que tiene la clase
        if os.path.isfile(self.url_imagen.path):
            os.remove(self.url_imagen.path)
        super().delete(*args, **kwargs)
        

#Definir los distintos tipos de donaciones
class Donacion(models.Model):
    nombre = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'
        
    def __str__(self):
        return self.name