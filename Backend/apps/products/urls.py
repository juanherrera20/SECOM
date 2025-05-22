from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  * # Import the all views from the views.py file

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'offers', OfferViewSet, basename='offers')



urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('tags/', TagView.as_view(), name='tags'),
    path('images/<int:pk>/', ImageView.as_view(), name='images'), # Ruta para las imagenes, necesita ID del evento
    path('states/', StateView.as_view(), name='states'),
    path('conditions/', ConditionView.as_view(), name='conditions'),
]