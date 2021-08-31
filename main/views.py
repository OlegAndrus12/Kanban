from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Task, TaskBar

def index(response):
    tasks = list(Task.objects.all())
    print(tasks)
    return render(response, "main/taskBar.html", {"tasks": tasks})

def login(response):
    return render(response, "main/login.html", {})
