# admin.py
from django.contrib import admin
from .models import Departamento, Municipio, Ubicacion

class MunicipioInline(admin.TabularInline):
    model = Municipio
    extra = 1  # Número de formularios vacíos que se muestran para agregar nuevos municipios

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    inlines = [MunicipioInline]

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento')
    list_filter = ('departamento',)
    search_fields = ('nombre', 'departamento__nombre')

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'municipio_id', 'direccion', 'latitud', 'longitud')
    list_filter = ('municipio_id__departamento', 'municipio_id')
    search_fields = ('nombre', 'direccion', 'municipio_id__nombre', 'municipio_id__departamento__nombre')
    fieldsets = [
        ('Información Básica', {
            'fields': ('nombre', 'municipio_id', 'direccion')
        }),
        ('Geolocalización', {
            'fields': ('latitud', 'longitud')
        }),
    ]

# Registrar los modelos
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)