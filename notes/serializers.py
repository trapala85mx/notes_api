"""notes/serializers.py"""

from rest_framework.serializers import ModelSerializer

from .models import Note


class NoteReadSerializer(ModelSerializer):
    """Serializer para lectura del modelo Note"""

    class Meta:
        """Metadatos del serializer"""

        model = Note
        fields = "__all__"


class NoteWriteSerializer(ModelSerializer):
    """Serializer para lectura del modelo Note"""

    class Meta:
        """Metadatos del serializer"""

        model = Note
        fields = ["title", "content"]
