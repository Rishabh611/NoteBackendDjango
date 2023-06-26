from django.urls import path
from user import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
]