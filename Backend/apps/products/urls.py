from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  *# Import the all views from the views.py file

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryView.as_view(), name='categories'),
    
]