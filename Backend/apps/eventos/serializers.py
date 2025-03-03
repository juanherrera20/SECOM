#Importamos las dependencias necesarias
from rest_framework import serializers
from django.db import transaction
from django.conf import settings

#Importaciones de otras apps
from apps.ubicacion.serializers import UbicacionSerializer
from apps.ubicacion.models import Municipio, Ubicacion
from apps.usuarios.models import CustomUser
from .models import Evento, Imagen, Donacion

#Serializador para una vista mas detallada del evento
class EventoSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    donacion = serializers.StringRelatedField()
    organizador = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=False)
    donacion_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Evento
        fields = '__all__'
    #Sobreescribimos el metodo Create del serializador, permite añadir logica extra atravez de el
    def create(self, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        donacion_id = validated_data.pop('donacion_id', None)
        
        print(f"Donación {donacion_id}")
        
        try:
            with transaction.atomic(): #Transaction Permite revertir cualquier proceso que se haya hecho en BD si algo sale mal, util para crear varias tablas con relaciones
                
                if ubicacion_data:
                    municipio_id = ubicacion_data.pop("municipio_id")
                    municipio = Municipio.objects.get(id=municipio_id)
                    
                    ubicacion = Ubicacion.objects.create(municipio = municipio, **ubicacion_data)
                    
                    print(f"Municipio: {municipio}")
                    print(f"Ubicación: {ubicacion}")
                
                if donacion_id:
                    donacion = Donacion.objects.get(id=donacion_id)
                else: 
                    print("No Funciono Establecemos default")
                    donacion = Donacion.objects.get(nombre="Cualquiera")
                
                evento = Evento.objects.create(ubicacion=ubicacion, donacion=donacion, **validated_data) 
            
            return evento
        
        except Exception as e:
            print(f"Error durante la creación de un Evento: {str(e)}")
            raise serializers.ValidationError(f"Ocurrió un error al crear el inmueble: {str(e)}")
    
    #Muy similar, el metodo Update actualiza la instancia atravez del serializador   
    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop("ubicacion", None)
        donacion_id = validated_data.pop('donacion_id', None)

        print(f"Donación {donacion_id}")

        try:
            with transaction.atomic():  # Transaction permite revertir cualquier proceso que se haya hecho en BD si algo sale mal
                # Actualizar la ubicación si se proporciona
                if ubicacion_data:
                    municipio_id = ubicacion_data.pop("municipio_id", None)

                    # Verificar si el municipio ha cambiado
                    if municipio_id and municipio_id != instance.ubicacion.municipio.id:
                        print("Es Diferente el Municipio")
                        municipio = Municipio.objects.get(id=municipio_id)
                        instance.ubicacion.municipio = municipio

                    # Actualizar otros campos de la ubicación
                    for attr, value in ubicacion_data.items():
                        setattr(instance.ubicacion, attr, value)

                    # Guardar la ubicación
                    instance.ubicacion.save()

                # Actualizar la donación si se proporciona
                if donacion_id and donacion_id != instance.donacion.id:
                    donacion = Donacion.objects.get(id=donacion_id)
                    instance.donacion = donacion

                # Actualizar otros campos del evento
                for attr, value in validated_data.items():
                    setattr(instance, attr, value)

                # Guardar el evento
                instance.save()

            return instance

        except Exception as e:
            print(f"Error durante la Actualización del Evento: {str(e)}")
            raise serializers.ValidationError(f"Ocurrió un error al actualizar el evento: {str(e)}")
    
    
#Serializador para listar los eventos
class EventoListSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    imagen = serializers.SerializerMethodField()
    
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha', 'causa', 'ubicacion', 'imagen']

    def get_imagen(self, obj):
        request = self.context.get('request')  # Obtener el request si está disponible
        imagen = obj.imagenes.order_by('orden').first()  # Obtener la imagen con el menor orden
        
        if imagen:
            # Construir la URL absoluta de la imagen
            if request:
                return request.build_absolute_uri(imagen.url_imagen.url)
            else:
                return f"{settings.MEDIA_URL}{imagen.url_imagen}"
        
        return None  # Si no hay imagen, devolver None

    
    
class ImagenSerializer(serializers.ModelSerializer):
    url_imagen = serializers.SerializerMethodField()

    class Meta:
        model = Imagen
        fields = ['url_imagen', 'orden', 'id']

    def get_url_imagen(self, obj):
        request = self.context.get('request')  # Obtener el request del contexto
        if obj.url_imagen:  # Verificar si la imagen existe
            if request:  # Si hay un request, construir la URL absoluta
                return request.build_absolute_uri(obj.url_imagen.url)
            else:  # Si no hay request, usar la URL relativa (MEDIA_URL)
                return f"{settings.MEDIA_URL}{obj.url_imagen}"
        return None  # Si no hay imagen, devolver None

   

#Serializador para las donaciones Util para los desplegables de opciones
class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = ['id', 'nombre']
