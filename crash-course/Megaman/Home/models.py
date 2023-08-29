from django.db import models

# Create your models here.


class Data(models.Model):
    text = models.TextField(max_length=255)
    name = models.CharField(max_length=155)
    age = models.IntegerField(max_length=3)

    def __str__(self) -> str:
        return self.name
