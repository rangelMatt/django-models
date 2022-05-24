from ast import Delete
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
  name = models.CharField(max_length=64)
  rating = models.IntegerField(default=0)
  purchaser = models.ForeignKey(get_user_model(), models.CASCADE)
  # description = models.
  
  def __str__(self):
    return self.name