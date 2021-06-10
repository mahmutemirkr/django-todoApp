from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.utils import tree

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    todotitle = models.CharField(max_length=200, null=False,blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todotitle

    class Meta:
        ordering = ['complete']