from .views import NoteList
from django.urls import path
urlpatterns = [
    path("notes/", NoteList.as_view())
]