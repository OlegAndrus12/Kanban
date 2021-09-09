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
    return render(response, "main/taskBar.html", {"taskBars": taskBars})