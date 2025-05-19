from django.db import models

from apps.usuarios.models import CustomUser
from apps.products.models import Product

# ----------------------------- MODELS ---------------------------------s
#Model to handle the rooms(Chats), a instance is created when user clicks (Adquirir) on the product
class Room(models.Model):
    class State(models.TextChoices):
        AVAILABLE = '1', "Disponible"
        SOLD = '2',  "Vendido"
        IN_PROGRESS = '3', "En Proceso"
        CANCELED = '4', "Cancelado"
    
    class Type(models.TextChoices):
        GROUP = '1', "Grupal"
        PRIVATE = '2', "Privado"
        
    state = models.CharField(max_length=1, default=State.AVAILABLE, choices=State.choices, verbose_name="Estado del producto")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    chat_type = models.CharField(max_length=1, default=Type.PRIVATE, choices=Type.choices, verbose_name="Tipo de chat")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="rooms")
    # ManyToManyField simplifies the code; there's no need to create an extra table to manage the relation between Rooms and Users
    users = models.ManyToManyField(CustomUser, related_name="rooms")
    
    class Meta:
        verbose_name_plural = "Salas de Chat"
        verbose_name = "Sala de Chat"
        
    def __str__(self):
        return f"{self.product.name} - {self.get_state_display()}"
    
    
# Handle type of message such as Text, Image, audio, Video
class MessageType(models.Model):
    name = models.CharField(max_length=60)
    
    class Meta: 
        verbose_name_plural = "Tipos de Mensaje"
        verbose_name = "Tipo de Mensaje"
        
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    content = models.TextField(blank=True)
    send_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="messages")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    message_type = models.ForeignKey(MessageType, on_delete=models.CASCADE, related_name="messages")
    url = models.FileField(upload_to="attachmentsChat/", null=True) # file will be uploaded to MEDIA_ROOT/imagesChat/
    
    class Meta: 
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['-send_date']
        # improve database searches
        indexes = [
            models.Index(fields=["room", "send_date"]),
        ]
        
    def __str__(self):
        return f"Room: {self.room.id} - {self.user.username} - {self.send_date}"