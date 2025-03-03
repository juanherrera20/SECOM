# admin.py
from django.contrib import admin
from .models import Evento, Imagen
from django.utils.html import format_html

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1  # Número de formularios vacíos que se muestran para agregar nuevas imágenes
    fields = ('url_imagen', 'orden', 'imagen_preview')
    readonly_fields = ('imagen_preview',)

    def imagen_preview(self, obj):
        if obj.url_imagen:
            return format_html('<img src="{}" width="100" height="100" />', obj.url_imagen.url)
        return "No hay imagen"
    
    imagen_preview.short_description = 'Vista Previa'

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'ubicacion', 'organizador', 'imagen_preview')
    list_filter = ('fecha', 'organizador')
    search_fields = ('nombre', 'descripcion', 'ubicacion__nombre', 'organizador__email')
    inlines = [ImagenInline]

    def imagen_preview(self, obj):
        primera_imagen = obj.imagenes.first()
        if primera_imagen and primera_imagen.url_imagen:
            return format_html('<img src="{}" width="50" height="50" />', primera_imagen.url_imagen.url)
        return "No hay imagen"
    
    imagen_preview.short_description = 'Imagen Principal'

# Registrar los modelos
admin.site.register(Evento, EventoAdmin)
admin.site.register(Imagen)