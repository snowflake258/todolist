from django.db import models
from .organization import Organization

class TaskList(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)


    class Meta:
        ordering = ['datetime']
    

    def __str__(self):
        return '%s %s' % (self.datetime, self.title)