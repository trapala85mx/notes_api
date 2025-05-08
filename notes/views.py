"""notes/views.py"""

from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    """Obtiene todas las notas o crea una nota en específico.

    Args:
        generics (ListApiView): Clase que contiene la funcionalidad para
                                obtención de información.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Obtiene, Actualiza o Elimina una nota en especñifico.
    Args:
        generics (RetrieveUpdateDestroyAPIView): Clase que contiene la funcionalidad para
                                                    todas acciones.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
