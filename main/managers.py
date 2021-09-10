from django.db import models
from django.apps import apps

class TaskManager(models.Manager):
    def get_task_by_title(self, id):
        return self.get_queryset().filter(title = id)
    def get_tasks_for_taskBar(self, taskBar):
        return self.get_queryset().filter(taskBar = taskBar)
    
class TaskBarManager(models.Manager):
    def get_notes_for_taskbar(self, taskbar):
        return apps.get_model(__package__, "Task").objects.get_tasks_for_taskBar(taskbar)
    
    def get_taskbar_by_name(self, taskbar_name):
        return self.get_queryset().filter(name = taskbar_name)

    def get_taskbar_names(self):
        return [i.name for i in self.get_queryset().all()]
        