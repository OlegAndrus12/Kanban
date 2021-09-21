from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Task, TaskBar
import math

def index(response):
    return render(response, "main/base.html")

def login(response):
    return render(response, "main/login.html", {})

def taskbar(response, id = None):
    if id == None:
        id = TaskBar.objects.first().id
    selected_taskBar = TaskBar.objects.get(id = id)
    notes = Task.objects.get_tasks_for_taskBar(selected_taskBar)

    context = {
        "taskBars" : TaskBar.objects.all(),
        "selected_taskbar_name": selected_taskBar.name,
        "notes" : notes,
    }
    print(context)
    return render(response, "main/taskBar.html", context)