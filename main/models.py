from django.db import models
from datetime import datetime
from django.utils.timezone import make_aware
from .managers import TaskManager, TaskBarManager

class TaskBar(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateField(auto_now_add=True)
    modifiedAt = models.DateField(auto_now=True)
    headerColor = models.CharField(max_length=10)

    objects = TaskBarManager()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    taskBar = models.ForeignKey(TaskBar, on_delete=models.CASCADE)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateField(auto_now=True)
    isFinished = models.BooleanField(default=False)

    objects = TaskManager()

    def __str__(self):
        return f"Task {self.title} : {self.description}"