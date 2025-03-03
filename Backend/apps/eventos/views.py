#Importamos Dependencias
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny


#Importamos los modelos y serializadores necesarios
from .models import Evento, Imagen, Donacion
from .serializers import EventoSerializer, EventoListSerializer, ImagenSerializer, DonacionSerializer

#ViewSets Permite manejar todas las peticiones CRUD de una vista en una sola clase
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().select_related('ubicacion', 'donacion', 'organizador') #Obtener las instancias de la base de datos
    permission_classes = [AllowAny,]# IsAuthenticated] #Solo los usuarios autenticados pueden acceder
    #parser_classes = [MultiPartParser, FormParser] #Puede ser util
    
    #SobreEscribirmos el metodo get_serializer_class para que use el serializador correcto Dependiendo la situación
    def get_serializer_class(self):
        if self.action == 'list':
            return EventoListSerializer
        return EventoSerializer
    
#Generics Permite manejar las peticiones CRUD de una vista en una sola clase
class DonacionView(generics.ListAPIView):
    queryset = Donacion.objects.all() #Obtener las instancias de la base de datos
    serializer_class = DonacionSerializer 
    permission_classes = [AllowAny] #Cualquier usuario puede acceder
    
    
#Vista para subir las imagenes, APIView es lo mas parecido a vistas de Django
class ImagenView(APIView):
    permission_classes = [AllowAny] #permissions.IsAdminUser
    
    def get(self, request, pk, format = None):
        evento_id = pk # si se envia el id del propietario mediante al url
        
        if not evento_id:
            return Response({"error": "El parámetro 'id' es obligatorio."}, status=400)
            
        print(f"ID evento {evento_id}")
        imagenes = Imagen.objects.filter(evento = evento_id).order_by("orden")
        serializer = ImagenSerializer(imagenes, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        """
        Agregar Imagenes y eliminar se manejan en una misma vista, de esta manera se envian 
        dos arrays uno con las nuevas imagenes y otro con las imagenes a eliminar
        """
        
        new_images = request.data.getlist("new_images", None)
        print(f"new: {new_images}")
        deleted_images = request.data.getlist("deleted_images", None)
        print(f"deleted: {deleted_images}")

        print(f"ID evento: {pk}")
      
        try:
            evento = Evento.objects.prefetch_related('imagenes').get(id=pk)
        except evento.DoesNotExist:
            return Response({"error": "Evento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        imagenes = evento.imagenes.all() # Obtener todas las imágenes del evento mediante relación inversa
        print(f"Imagenes obj antes: {imagenes}")
        
        # Eliminar Imagenes
        for images_id in deleted_images:
            try:
                obj = imagenes.get(id=images_id)
                obj.delete()  # Eliminamos el archivo
                imagenes = imagenes.exclude(id=images_id)
            except Imagen.DoesNotExist:
                print(f"Imagen con ID {images_id} no encontrado")

        print(f"Imagenes obj despues: {imagenes}")
        
        
        #Modificar logica para manejar prioridades -----------------
        
        # Reordenar imágenes después de eliminación
        for index, image in enumerate(imagenes.order_by("orden"), start=1):
            image.orden = index
            image.save(update_fields=["orden"]) 

        # btener último orden actual
        orden = imagenes.count() + 1
        print(f"Orden: {orden}")

        # Agregar nuevas imágenes con orden ascendente
        for image in new_images:
            Imagen.objects.create(url_imagen=image, evento = evento, orden=orden)
            orden += 1
        
        return Response(status=status.HTTP_204_NO_CONTENT) #Mejor manejo de errores