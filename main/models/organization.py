from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['name']

    
    def __str__(self):
        return self.name