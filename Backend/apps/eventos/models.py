from django.db import models
from apps.usuarios.models import CustomUser
from apps.ubicacion.models import Ubicacion
from django.utils.text import slugify
import os


#-------------------Función para subir las imagenes de los eventos-------------------
def get_image_upload_path(instance, filename):
    # Obtener el nombre del evento y limpiarlo para usarlo como carpeta
    eventos_name = slugify(instance.evento.name)
    
    # Construir la ruta
    return os.path.join('Eventos', eventos_name, 'Images', filename)
#-----------------------------------------------------------------------------------------

# Modelos Aquí
class Evento (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    meet_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    #Los campos OneToOneField se usan para establecer una relación uno a uno 
    ubicacion = models.ForeignKey(Ubicacion, related_name="evento", on_delete=models.CASCADE)
    organizador = models.ForeignKey(CustomUser, related_name="eventos", on_delete=models.CASCADE)
    type_donation = models.ForeignKey('Donation', related_name="eventos", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        
    def __str__(self): 
        return f"{self.name} - {self.meet_date}"
    
    
class Image(models.Model):
    evento = models.ForeignKey(Evento, related_name="images", on_delete=models.CASCADE)
    url = models.ImageField(upload_to=get_image_upload_path, max_length=300)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.evento.name} - {self.url}"
    
    #Función para eliminar los archivos cuando se eliminan de la base de datos
    def delete(self, *args, **kwargs): #Llamamos al metodo delete que tiene la clase
        if os.path.isfile(self.url.path):
            os.remove(self.url.path)
        super().delete(*args, **kwargs)
        

#Define model to handle suscriptions to the event
class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, related_name="subscriptions", on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, related_name="subscriptions", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Suscripción'
        verbose_name_plural = 'Suscripciones'
        
    def __str__(self):
        return f"{self.user.email} - {self.evento.name}"

#Definir los distintos tipos de donaciones
class Donation(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'
        
    def __str__(self):
        return self.nombre