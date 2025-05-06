"""notes/urls.py"""

from django.urls import path

from .views import notes, notes_detail

urlpatterns = [
    path("notes/", view=notes, name="list-notes"),
    path("notes/<int:pk>/", view=notes_detail, name="detail-notes"),
]
