# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de usuarios
    list_display = ('email', 'username', 'telefono', 'puntos', 'reputacion', 'is_staff', 'is_active')
    
    # Campos por los que se puede filtrar
    list_filter = ('is_staff', 'is_active', 'reputacion')
    
    # Campos que se pueden buscar
    search_fields = ('email', 'username', 'telefono')
    
    # Ordenamiento por defecto
    ordering = ('email',)
    
    # Campos que se mostrarán en el formulario de edición
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Información Personal', {'fields': ('telefono', 'img_profile', 'first_name', 'last_name')}),
        ('Puntos y Reputación', {'fields': ('puntos', 'reputacion')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Campos que se mostrarán en el formulario de creación
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'telefono', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

# Registrar el modelo CustomUser con la clase CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)