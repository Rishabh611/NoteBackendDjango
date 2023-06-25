from .views import note_list
from django.urls import path
urlpatterns = [
    path("notes/", note_list)
]