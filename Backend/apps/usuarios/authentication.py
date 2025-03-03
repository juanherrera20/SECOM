from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from rest_framework.response import Response

class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Intentamos obtener el token de acceso (access token) desde las cookies
        token = request.COOKIES.get('token')
        
        print(f"Este es el token: {token}\n")

        if not token:
            return None  # Si no hay token de acceso, no autenticamos al usuario

        try:
            # Validamos el token de acceso
            validated_token = self.get_validated_token(token)
            
        except Exception as e:
            # Si el token de acceso ha expirado o no es válido, intentamos refrescarlo
            print(f"Token expired or invalid: {str(e)}")
            return self.refresh_token(request)

        user = self.get_user(validated_token)
        
        if user is None:
            raise AuthenticationFailed("User not found.")
        
        return (user, validated_token)

    def refresh_token(self, request):
        # Obtenemos el refresh token desde las cookies
        refresh_token = request.COOKIES.get('refresh_token')
        print(f"Se obtiene el refresh token: {refresh_token}\n")
        
        if not refresh_token:
            raise AuthenticationFailed("Refresh token is missing.")

        #Revisar si guardar de nuevo el access token
        try:
            print("creamos un nuevo access token\n")
            # Validamos el refresh token
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)
            
            
            # Creamos un nuevo token de acceso y lo enviamos al cliente
            user = self.get_user(refresh)
            if not user:
                raise AuthenticationFailed("Invalid refresh token.")
            
            validated_token = self.get_validated_token(new_access_token)
            
            # Añadir el nuevo token de acceso a las cookies
            #validated_token.set_cookie(key="token", value=new_access_token, httponly=True, secure=True, samesite="None", path="/")

            print("Token refrescado y cookies configuradas")
            # Retornar el usuario y el nuevo token
            return (user, validated_token)
        
        except Exception as e:
            raise AuthenticationFailed(f"Error refreshing token: {str(e)}")

