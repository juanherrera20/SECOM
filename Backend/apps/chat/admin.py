from django.contrib import admin
from .models import Room, Message, MessageType

# Admin para los tipos de mensaje
@admin.register(MessageType)
class MessageTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Inline para mostrar los mensajes directamente en la sala
class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('send_date',)
    fields = ('user', 'content', 'message_type', 'url', 'send_date')
    show_change_link = True

# Admin para las salas (rooms)
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'chat_type', 'state', 'create_date', 'get_users')
    list_filter = ('chat_type', 'state', 'create_date')
    search_fields = ('product__name', 'users__username')
    date_hierarchy = 'create_date'
    inlines = [MessageInline]
    filter_horizontal = ('users',)

    def get_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    get_users.short_description = 'Usuarios'

# Admin para los mensajes
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'message_type', 'short_content', 'send_date')
    list_filter = ('message_type', 'send_date')
    search_fields = ('content', 'user__username', 'room__id')
    date_hierarchy = 'send_date'
    readonly_fields = ('send_date',)

    def short_content(self, obj):
        return obj.content[:40] + '...' if obj.content and len(obj.content) > 40 else obj.content
    short_content.short_description = 'Contenido'
