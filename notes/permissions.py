"""notes/permissions.py"""

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Clase para crear un permiso para que solo
    el dueño pueda trabajar con una nota.
    """

    def has_object_permission(self, request, view, obj):
        """
        Método que solo trabaja con métodos que involucran
        objetos en específico. Valida que el usuario que
        viene en el request (logueado) este trabajando con
        objetos creados por él mismo.
        """
        return obj.user == request.user
