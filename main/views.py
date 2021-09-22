from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Task, TaskBar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

def index(response):
    return render(response, "main/base.html")

def login(response):
    return render(response, "main/login.html", {})

def taskbar(response, id = None):
    if id == None:
        id = TaskBar.objects.first().id
    selected_taskBar = TaskBar.objects.get(id = id)
    notes_list = Task.objects.get_tasks_for_taskBar(selected_taskBar)
    page = response.GET.get('page', 1)
    paginator = Paginator(notes_list, 3)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    context = {
        "taskBars" : TaskBar.objects.all(),
        "selected_taskbar_name": selected_taskBar.name,
        "notes" : notes,
    }
    print(context)
    return render(response, "main/taskBar.html", context)