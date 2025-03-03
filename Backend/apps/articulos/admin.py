# admin.py
from django.contrib import admin
from .models import Categoria, Articulo, Etiqueta, ArticuloEtiqueta

class ArticuloEtiquetaInline(admin.TabularInline):
    model = ArticuloEtiqueta
    extra = 1  # Número de formularios vacíos que se muestran para agregar nuevas etiquetas

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'usuario', 'fecha_publicacion')
    list_filter = ('categoria', 'estado', 'usuario')
    search_fields = ('nombre', 'descripcion', 'categoria__nombre', 'usuario__username')
    inlines = [ArticuloEtiquetaInline]

    fieldsets = [
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'categoria', 'estado')
        }),
        ('Relaciones', {
            'fields': ('usuario', 'ubicacion')
        })
    ]

class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')

class ArticuloEtiquetaAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'etiqueta')
    list_filter = ('articulo', 'etiqueta')
    search_fields = ('articulo__nombre', 'etiqueta__nombre')

# Registrar los modelos
admin.site.register(Categoria)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(ArticuloEtiqueta, ArticuloEtiquetaAdmin)