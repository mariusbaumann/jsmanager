from django.db import models

# Create your models here.

class cVideofile(models.Model):
    videoTitle = models.CharField(max_length=200)
    timeCreated = models.DateTimeField('date published')
    length = models.IntegerField(default=0)
    frames = models.IntegerField(default=0)
    framesDone = models.IntegerField(default=0)
    codingString = models.CharField(max_length=500)
