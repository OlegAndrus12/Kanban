from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login, name = "login"),
    path("taskbar", views.taskbar, name = "taskbar-list"),
    path("taskbar/<int:id>", views.taskbar, name = "taskbar-list"),
]
