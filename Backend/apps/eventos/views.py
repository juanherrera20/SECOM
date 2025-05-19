from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Evento, Image, Donation, EventPost
from .serializers import EventoSerializer, EventoListSerializer, ImageSerializer, DonationSerializer, EventPostSerializer

# ViewSet para manejar CRUD de eventos
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().select_related('ubicacion', 'type_donation', 'organizador')
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return EventoListSerializer
        return EventoSerializer
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def subscribe(self, request, pk=None):
        try:
            evento = self.get_object()
            user = request.user

            # Verificar si el usuario ya está suscrito
            if evento.subscriptions.filter(user=user).exists():
                return Response({"detail": "Ya estás suscrito a este evento."}, status=status.HTTP_400_BAD_REQUEST)

            # Crear la suscripción
            Subscription.objects.create(user=user, evento=evento)
            return Response({"detail": "Suscripción exitosa."}, status=status.HTTP_201_CREATED)

        except Evento.DoesNotExist:
            return Response({"detail": "Evento no encontrado."}, status=status.HTTP_404_NOT_FOUND)


class EventPostViewSet(viewsets.ModelViewSet):
    queryset = EventPost.objects.all().prefetch_related('evento')
    serializer_class = EventPostSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento']
    ordering = ['-create_date']
    
    
# Vista para listar tipos de donación
class DonationView(generics.ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
def get_donacion_por_evento(request, evento_id):
    try:
        donacion = Donation.objects.get(evento__id=evento_id)
        serializer = DonationSerializer(donacion)
        return Response(serializer.data)
    except Donation.DoesNotExist:
        return Response({'detail': 'No se encontró donación para este evento.'}, status=404)


# Vista para manejar imágenes del evento (GET y POST)
class ImageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            images = Image.objects.filter(evento_id=pk).order_by("order")
            serializer = ImageSerializer(images, many=True, context={'request': request})
            return Response(serializer.data)
        except Evento.DoesNotExist:
            return Response({"error": "Evento no encontrado"}, status=404)

    def post(self, request, pk, format=None):
        new_images = request.FILES.getlist("new_images", [])
        deleted_images = request.data.getlist("deleted_images", [])

        try:
            evento = Evento.objects.prefetch_related('images').get(id=pk)
        except Evento.DoesNotExist:
            return Response({"error": "Evento no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        images = evento.images.all()

        # Eliminar imágenes marcadas
        for image_id in deleted_images:
            try:
                obj = images.get(id=image_id)
                obj.delete()
                images = images.exclude(id=image_id)
            except Image.DoesNotExist:
                continue

        # Reordenar existentes
        for index, image in enumerate(images.order_by("order"), start=1):
            image.order = index
            image.save(update_fields=["order"])

        # Agregar nuevas
        next_order = images.count() + 1
        for img in new_images:
            Image.objects.create(url=img, evento=evento, order=next_order)
            next_order += 1

        return Response(status=status.HTTP_204_NO_CONTENT)
