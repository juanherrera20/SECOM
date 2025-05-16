from django.db import models
from django.utils import timezone

from apps.chat.models import Room
from apps.usuarios.models import CustomUser

# Create your models here.
class Exchange(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name="exchange")
    seller_confirmed = models.BooleanField(default=False, verbose_name="Vendedor confirmó")
    buyer_confirmed = models.BooleanField(default=False, verbose_name="Comprador confirmó")
    create_date = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Intercambio"
        verbose_name_plural = "Intercambios"

    def __str__(self):
        return f"Intercambio - {self.room.product.name}"

    def is_completed(self):
        return self.seller_confirmed and self.buyer_confirmed

    def save(self, *args, **kwargs):
        if self.is_completed() and not self.confirmed_at:
            self.confirmed_at = timezone.now()
        super().save(*args, **kwargs)
        
        

class Review(models.Model):
    exchange = models.OneToOneField(Exchange, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reviews")

    rating = models.PositiveSmallIntegerField(verbose_name="Calificación (1-5)")
    comment = models.TextField(max_length=1000, blank=True, verbose_name="Comentario")
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('exchange', 'user')
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f"{self.create_date} → {self.user.username} ({self.rating})"
