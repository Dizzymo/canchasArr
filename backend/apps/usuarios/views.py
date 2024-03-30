from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import schemas
from rest_framework_simplejwt.tokens import RefreshToken

import json
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import coreapi
import coreschema

from django.views.generic import TemplateView 
# 
class LoginView(TemplateView):
    template_name = "users/login.html"

class LoginAPIView(APIView):
    """
    API View para el inicio de sesión de usuarios.
    """
    

    schema = schemas.ManualSchema(
        fields=[
            coreapi.Field(
                "email", 
                required=True, 
                location='form', 
                # schema={'type': 'string'}, 
                schema=coreschema.String(), 
                description='Correo electrónico del usuario'
                ),
            coreapi.Field(
                name='password', 
                required=True, 
                location='form', 
                schema=coreschema.String(), 
                description='Contraseña del usuario'),
        ],
        
        description="Inicio de sesión de usuarios"
    )
    
    
    @csrf_exempt
    def post(self, request):
        """
        Iniciar sesión de usuario.
        """
        data = request.data
        email = data.get('email')
        password = data.get('password')

        # Validar que se proporcionaron credenciales de inicio de sesión
        if not email or not password:
            return Response({'error': 'Se requieren email y contraseña'}, status=status.HTTP_400_BAD_REQUEST)

        # Llamar al procedimiento almacenado para verificar las credenciales del usuario
        with connection.cursor() as cursor:
            cursor.execute("SELECT public.user_loginv2(%s, %s)", [email, password])
            result = cursor.fetchone()
        print("re: "+result)
        # Verificar el resultado del procedimiento almacenado
        if result[0] == True:
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        elif result[0] == False:
            return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Error en el servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


 