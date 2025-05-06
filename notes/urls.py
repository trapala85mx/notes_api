"""notes/urls.py"""

from django.urls import path

from .views import notes

urlpatterns = [
    path("notes/", view=notes, name="list-notes"),
]
