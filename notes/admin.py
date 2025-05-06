"""notes/admin.py"""

from django.contrib import admin

from .models import Note


# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    """Configuración para el modelo Note en el Admin."""

    list_display = (
        "title",
        "content",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
    ordering = (
        "title",
        "created_at",
    )


# Le decimos a Django que registe el modelo Note
# con la configuración de NoteAdmin
admin.site.register(Note, NoteAdmin)
