"""notes/urls.py"""

from django.urls import path

from .views import NoteListCreateView, NoteRetrieveUpdateDeleteView

urlpatterns = [
    path("notes/", view=NoteListCreateView.as_view(), name="list-notes"),
    path(
        "notes/<int:pk>/",
        view=NoteRetrieveUpdateDeleteView.as_view(),
        name="detail-notes",
    ),
]
