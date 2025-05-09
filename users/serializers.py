"""users/serializers.py"""

from typing import Any, Dict

from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    """
    Convertir obtejos del modelo User en JSON y viceversa.
    """

    class Meta:
        """
        Metadatos para el Serializer.
        """

        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: Dict[str, Any]) -> User:
        """
        Crea un nuevo usuario en la Base de Datos. Encriptando la
        contraseña.

        Args:
            validated_data (Dict[str, Any]): Datos recibidos del cliente
                                             y validados.

        Returns:
            User: Usuario creado en la Base de Datos, mostrando solo los
                    datos configurados en el Serializer.
        """

        user = User.objects.create_user(**validated_data)
        return user
