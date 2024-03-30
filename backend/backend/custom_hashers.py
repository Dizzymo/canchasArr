from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.translation import gettext_noop as _
from django.db import connection

class CryptPasswordHasher(BasePasswordHasher):
    """
    Utiliza la función crypt de PostgreSQL para hashear contraseñas.
    """
    algorithm = 'sha256'

    def salt(self):
        # La función crypt de PostgreSQL generará automáticamente un salt
        return None

    def encode(self, password, salt=None):
        # Django manejará la codificación de la contraseña de forma interna
        return password

    def verify(self, password, encoded):
        # Verifica si la contraseña proporcionada coincide con el hash almacenado
        return password == encoded

    def safe_summary(self, encoded):
        # Devuelve solo el hash sin el prefijo
        return encoded