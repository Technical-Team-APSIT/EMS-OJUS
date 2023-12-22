from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    id = models.CharField(unique=True, primary_key=True)
    dept = models.CharField(max_length=6, null=True)
    year = models.CharField(max_length=6, null=True)
    fname = models.CharField(blank=True)
    lname = models.CharField(blank= True)

    def __str__(self):
        return str(f""+self.id+"_"+self.fname+"_"+self.lname+"")

    USERNAME_FIELD = 'id'

    REQUIRED_FIELDS = ['username']

    

class Event(models.Model):
    name = models.CharField(null=True)
    desc = models.TextField(null=True)
    venue = models.CharField(null=True)
    date = models.DateField()
    time = models.TimeField()
    img = models.ImageField(upload_to='images', null=True, blank=True, default='logo.png')

    def __str__(self):
        return str(self.name)

class Rule(models.Model):
    name = models.CharField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class eventHead(models.Model):
    name = models.CharField(null=True)
    contact = models.BigIntegerField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Signed(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
# Create your models here.
