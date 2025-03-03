from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Base API endpoints
BASE_API = 'api/v1/'

#Definimos las rutas de los distintos Endpoitns de la API y sus aplicaciones
urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_API + 'usuarios/', include('apps.usuarios.urls')),
    path(BASE_API + 'eventos/', include('apps.eventos.urls')),
]

# 🔥 IMPORTANTE: Esto permite acceder a archivos en /media/ en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)