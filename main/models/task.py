from django.db import models
from .task_list import TaskList

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    task_list = models.ForeignKey(TaskList, on_delete=models.PROTECT)


    class Meta:
        ordering = ['name']
    

    def __str__(self):
        return self.name