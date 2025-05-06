"""notes/models.py"""

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

    def __str__(self):
        return f"{self.title}"
