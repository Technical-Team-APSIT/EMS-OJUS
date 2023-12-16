from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    moodle_id = models.CharField(unique=True, primary_key=True)
    dept = models.CharField(max_length=6, null=True)
    year = models.CharField(max_length=6, null=True)
    fname = models.CharField(blank=True)
    lname = models.CharField(blank= True)

    def __str__(self):
        return str(f""+self.moodle_id+"_"+self.fname+"_"+self.lname+"")

    USERNAME_FIELD = 'moodle_id'

    REQUIRED_FIELDS = ['username']

    

class Event(models.Model):
    name = models.CharField(null=True)
    desc = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.name)

class Regis(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
# Create your models here.
