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
        serializer.is_valid(raise_exception=True)
        note = serializer.save()
        return Response(NoteReadSerializer(note).data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def notes_detail(request, pk: int):
    """Vista basada en función para modificar notas y
    obtener detalles de una nota en específico"""
    # Buscamos la nota con el id enviado
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        # Si no existe arrojamos un 404
        return Response(status=status.HTTP_404_NOT_FOUND)

    method = request.method

    # Si se encuentra la nota vemos qué método se envió

    if method == "GET":
        # un JSON con el serializador, en este caso, para leer
        serializer = NoteReadSerializer(note)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if method == "PUT":
        # Actualizar toda los campos de la nota.
        serializer = NoteWriteSerializer(note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(NoteReadSerializer(note).data, status=status.HTTP_201_CREATED)

    if method == "PATCH":
        # Actualizar solo los campos enviados
        serializer = NoteWriteSerializer(note, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Explicación de esta línea:
        # note es una instancia del modelo Note , obtenida previamente
        # Esto quiere decir que note es un objeto de la base de datos, como si fuera un registro de tu tabla notes.
        # por lo que ya tiene todos los datos
        # Al hacer NoteReadSerializer(note)
        # Estamos diciendo: "Serializa este objeto (note) según las reglas definidas en NoteReadSerializer".
        # En este punto NoteReadSerializer(note), la data actualizada ya la tenemos como no NoteReadSerializer
        # Solo basta retornar el json con ".data"
        return Response(NoteReadSerializer(note).data, status=status.HTTP_201_CREATED)

    if method == "DELETE":
        # Eliminamos la nota
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
