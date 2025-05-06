"""notes/views.py"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteReadSerializer, NoteWriteSerializer


# Create your views here.
@api_view(["GET", "POST"])
def notes(request):
    """Vista basada en función para listar todas las notas y
    crear una nota"""
    method = request.method

    if method == "GET":
        # Listamos todas las notas
        notes = Note.objects.all()
        serializer = NoteReadSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if method == "POST":
        # Crear una nota
        serializer = NoteWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
