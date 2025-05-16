from django.db import models

from apps.usuarios.models import CustomUser

# --------------------------- MODELS --------------------------- S

class Notification(models.Model):
    content = models.CharField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    is_read = models.BooleanField(default=False, verbose_name="Leída")
    
    class Meta:
        verbose_name_plural = "Notificaciones"
        verbose_name = "Notificación"
        
    def __str__(self):
        return f"{self.user.username} - {self.create_date.strftime('%Y-%m-%d %H:%M')}"