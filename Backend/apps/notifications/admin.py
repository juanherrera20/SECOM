from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_content', 'is_read', 'create_date')
    list_filter = ('is_read', 'create_date')
    search_fields = ('content', 'user__username')
    ordering = ['-create_date']
    date_hierarchy = 'create_date'

    # Muestra contenido recortado para que no se alargue en la lista
    def short_content(self, obj):
        return obj.content[:40] + ('...' if len(obj.content) > 40 else '')
    short_content.short_description = 'Contenido'