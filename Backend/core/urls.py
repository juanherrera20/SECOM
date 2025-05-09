from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.usuarios.views import GoogleLogin, GoogleAuthCallback

# Base API endpoints
BASE_API = 'api/v1/'

#Definimos las rutas de los distintos Endpoitns de la API y sus aplicaciones
urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_API + 'usuarios/', include('apps.usuarios.urls')),
    path(BASE_API + 'eventos/', include('apps.eventos.urls')),
    path(BASE_API + 'ubicacion/', include('apps.ubicacion.urls')),
    path(BASE_API + 'products/', include('apps.products.urls')),
    
    # Autenticación Google
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/', include('social_django.urls', namespace='social')),
    path(BASE_API + 'auth/google/callback/', GoogleAuthCallback.as_view(), name='google_callback'),  
]

# 🔥 IMPORTANTE: Esto permite acceder a archivos en /media/ en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)