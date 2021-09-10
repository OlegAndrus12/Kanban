from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Task, TaskBar

def index(response):
    return render(response, "main/base.html")

def login(response):
    return render(response, "main/login.html", {})

def notes(response):
    tasks = list(Task.objects.all())
    taskBars = list(TaskBar.objects.all())
    print(TaskBar.objects.get_taskbar_names())
    print(TaskBar.objects.get_notes_for_taskbar(taskBars[2]))
    return render(response, "main/taskBar.html", {"taskBars": taskBars})