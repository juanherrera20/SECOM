from django.contrib import admin
from .models import Departamento, City, Ubicacion


class CityInline(admin.TabularInline):
    model = City
    extra = 1  # Número de formularios vacíos que se muestran para agregar nuevas ciudades


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [CityInline]


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "departamento", "latitude", "longitude")
    list_filter = ("departamento",)
    search_fields = ("name", "departamento__name")


class UbicacionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",  # Muestra el nombre de la ciudad
        "address",
        "latitude",
        "longitude",
        "pais",
    )
    list_filter = ("city__departamento", "city")
    search_fields = (
        "name",
        "address",
        "city__name",
        "city__departamento__name",
    )
    fieldsets = [
        ("Información Básica", {"fields": ("name", "city", "address")}),
        ("Geolocalización", {"fields": ("latitude", "longitude", "pais")}),
    ]
    blankspace_fields = ('city', "latitude", "longitude")  # Campos que se pueden dejar en blanco
    



# Registrar los modelos
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
