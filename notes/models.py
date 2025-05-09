"""notes/models.py"""

from django.conf import settings  # Para usar AUTH_USER_MODEL
from django.db import models


# Create your models here.
class Note(models.Model):
    """Modelo para una Nota."""

    title = models.CharField(max_length=255, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última actualización"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="notes",
    )

    def __str__(self):
        return f"{self.title}"
