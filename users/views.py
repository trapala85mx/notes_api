"""users/views.py"""

from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView, generics.ListAPIView):
    """
    Vista para Registrar Usuarios a través
    de un Serializador.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
