from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .serializers import CustomUserSerializer
from rest_framework import status, generics
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.conf import settings
import secrets, requests
from rest_framework_simplejwt.tokens import RefreshToken

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
    
    
class CustomUserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer
    

class GoogleLogin(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        state = secrets.token_urlsafe(32)

        # Guardar el state en una cookie HTTPOnly
        response = Response({
            "auth_url": (
                f"https://accounts.google.com/o/oauth2/v2/auth?"
                f"response_type=code&"
                f"client_id={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY}&"
                f"redirect_uri={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI}&"
                f"scope=email profile&"
                f"state={state}&"
                f"access_type=offline&"
                f"prompt=consent"
            ),
            "state": state
        })
        response.set_cookie("oauth_state", state, httponly=True, secure=True, samesite="None", path="/")

        return response
    

class GoogleAuthCallback(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("🚀 Callback de Google recibido")

        # Intentamos obtener el código desde el cuerpo de la solicitud
        code = request.data.get("code")  
        received_state = request.data.get("state")
        stored_state = request.COOKIES.get("oauth_state")

        print(f"🔹 Código recibido: {code}")
        print(f"🔹 State recibido: {received_state}, esperado: {stored_state}")

        if not code or received_state != stored_state:
            return Response({"error": "Invalid state or missing code"}, status=400)

        # 🔄 Intercambio del código por el token de acceso en Google
        token_response = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                "client_secret": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                "redirect_uri": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI,
                "grant_type": "authorization_code",
            },
        ).json()

        if "error" in token_response:
            return Response({"error": token_response["error"]}, status=400)

        access_token = token_response.get("access_token")

        # 🔍 Obtener información del usuario desde Google
        user_info_response = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        ).json()

        print(f"🔹 Datos del usuario: {user_info_response}")

        email = user_info_response.get("email")
        name = user_info_response.get("name")
        picture = user_info_response.get("picture")

        if not email:
            return Response({"error": "No se pudo obtener el correo"}, status=400)

        # 🔥 Manejo de username vacío o duplicado
        base_username = email.split("@")[0]  
        username = base_username
        count = 1
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{count}"
            count += 1

        # 🚀 Verificar si el usuario ya existe o crearlo
        user, created = CustomUser.objects.get_or_create(
            email=email,
            defaults={
                "first_name": name.split(" ")[0],  
                "last_name": " ".join(name.split(" ")[1:]),  
                "img_profile": picture,  
                "username": username,  
                "telefono": "",  
                "is_active": True,
            }
        )

        if not user.is_active:
            return Response({"error": "Usuario inactivo"}, status=403)

        # 🔑 Generar tokens JWT
        try:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
        except Exception as e:
            return Response({"error": "Error generando tokens"}, status=500)

        response = Response({"access_token": str(access), "refresh_token": str(refresh)})
        response.set_cookie("token", str(access), httponly=True, secure=False, samesite="None", path="/")
        response.set_cookie("refresh_token", str(refresh), httponly=True, secure=False, samesite="None", path="/")

        return response
