# admin.py
from django.contrib import admin
from .models import Departamento, Municipio, Ubicacion


class MunicipioInline(admin.TabularInline):
    model = Municipio
    extra = (
        1  # Número de formularios vacíos que se muestran para agregar nuevos municipios
    )


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    inlines = [MunicipioInline]


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "departamento")
    list_filter = ("departamento",)
    search_fields = ("nombre", "departamento__nombre")

"""
class UbicacionAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "municipio",
        "direccion",
        "latitud",
        "longitud",
        "pais",
        "ciudad",
    )
    list_filter = ("municipio__departamento", "municipio")
    search_fields = (
        "nombre",
        "direccion",
        "municipio__nombre",
        "municipio__departamento__nombre",
    )
    fieldsets = [
        ("Información Básica", {"fields": ("nombre", "municipio", "direccion")}),
        ("Geolocalización", {"fields": ("latitud", "longitud", "pais", "ciudad")}),
    ]
"""

class UbicacionAdmin(admin.ModelAdmin):
    list_display = (
        "pais",
        "ciudad_o_municipio",
    )

# Registrar los modelos
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
