from django.contrib import admin
from django.utils.html import format_html
from .models import Evento, Image, Donation

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('url', 'order', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.url:
            return format_html('<img src="{}" width="100" height="100" />', obj.url.url)
        return "No hay imagen"

    image_preview.short_description = 'Vista Previa'


class EventoAdmin(admin.ModelAdmin):
    list_display = ('name', 'meet_date', 'ubicacion', 'organizador', 'main_image_preview')
    list_filter = ('meet_date', 'organizador')
    search_fields = ('name', 'description', 'ubicacion__name', 'organizador__email')
    inlines = [ImageInline]

    def main_image_preview(self, obj):
        primera_imagen = obj.images.first()
        if primera_imagen and primera_imagen.url:
            return format_html('<img src="{}" width="50" height="50" />', primera_imagen.url.url)
        return "No hay imagen"

    main_image_preview.short_description = 'Imagen Principal'


class DonationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Registro de modelos
admin.site.register(Evento, EventoAdmin)
admin.site.register(Image)
admin.site.register(Donation, DonationAdmin)
