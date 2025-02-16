from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets
from .serializers import CustomUserSerializer

class UsuarioViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
