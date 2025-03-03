from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .serializers import CustomUserSerializer
from rest_framework import status, generics
from .models import CustomUser
from django.contrib.auth import get_user_model

#Obtener el modelo de usuario dinamicamente
User = get_user_model()

#Modificar la vista por defecto que viene para obtener el token Simple-JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            # Llamar a la vista base para obtener el token
            response = super().post(request, *args, **kwargs)
            
            print("Se intenta obtener el token")
            token = response.data.get("access")
            refresh_token = response.data.get("refresh")
            
            # Añadir las cookies HTTPOnly al objeto de respuesta original
            response.set_cookie(key="token", value=token, httponly=True, secure=True, samesite="None", path="/")
            response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=True, samesite="None", path="/")
            
            print("Token obtenido y cookies configuradas")
            return response
        except Exception as e:
            print(f"Error al obtener el token: {str(e)}")
            return Response({"success": False}, status=400)

#Mofiicar la vista por defecto que viene para refrescar el token Simple-JWT
class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            print("Se intenta refrescar el token Vista")
            
            # Recuperar el refresh token de las cookies
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({"Refreshed": False, "message": "No se encontró el refresh token"}, status=400)
            
            # Insertar el token en el cuerpo de la solicitud
            request.data["refresh"] = refresh_token
            
            # Llamar a la vista base para refrescar el token
            response = super().post(request, *args, **kwargs)
            
            # Obtener el nuevo access token
            token = response.data.get("access")
            
            # Añadir las cookies HTTPOnly al objeto de respuesta original
            response.set_cookie(key="token", value=token, httponly=True, secure=False, samesite="None", path="/")
            
            print("Token refrescado y cookies configuradas")
            return response
        except Exception as e:
            print(f"Error al refrescar el token: {str(e)}")
            return Response({"Refreshed": False}, status=400)

#Cerrar sesion   
@api_view(['POST'])
def logout(request):
    try: 
        print("Se esta cerrando sesion")
        res = Response()
        res.data = {"succes": True}
        res.delete_cookie("token")
        res. delete_cookie("refresh_token")
        return res
    except:
        return Response({"succes": False})

#Crear un usuario
@permission_classes([AllowAny])
class register(APIView):
    def post(self, request):
        print("Se intenta registrar un usuario")
        serializer = CustomUserSerializer(data = request.data)
        print(f"Datos recibidos: {request.data}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Vista para comprobar el funcionamiento del token de acceso
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def restringedView(request):
    return Response({"message": "Acceso Exitoso!", "success": True})


#Vista para obtener y eliminar un usuario
class CustomUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    
    def get_object(self):
        return self.request.user