from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["completed"]


# class MyModel(models.Model):
#     title = models.CharField(max_length=155)
#     description = models.TextField(null=True, blank=True)
#     completed = models.BooleanField(default=False)
