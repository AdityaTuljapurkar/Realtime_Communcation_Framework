from django.db import models
from datetime import datetime
# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)

class Room(models.Model):
    name = models.CharField(max_length=10000)
    room = models.CharField(max_length=1000)
    message = models.CharField(max_length=500000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    
