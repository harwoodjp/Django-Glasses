import datetime
from django.db import models
from django.forms import ModelForm

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

