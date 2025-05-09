"""notes/serializers.py"""

from rest_framework.serializers import ModelSerializer

from .models import Note


class NoteSerializer(ModelSerializer):
    """Serializer para lectura del modelo Note"""

    class Meta:
        """Metadatos del serializer"""

        model = Note
        exclude = ["user"]
        extra_kwargs = {
            "title": {"required": False},
            "content": {"required": False},
        }
