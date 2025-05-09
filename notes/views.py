"""notes/views.py"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Note
from .permissions import IsOwner
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    """
    Vista que maneja todos los métodos HTTP para un
    CRUD de las Notas. Verificando que esté logueado
    y que este trabajando sobre notas creadas por
    el mismo usuario.
    """

    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
