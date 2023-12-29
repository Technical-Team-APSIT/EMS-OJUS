from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    moodle_id = models.CharField(unique=True, primary_key=True, max_length=100)
    dept = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=50, null=True)
    fname = models.CharField(max_length= 200, blank=True)
    lname = models.CharField(max_length= 200, blank= True)

    def __str__(self):
        return str(f""+self.moodle_id+"_"+self.fname+"_"+self.lname+"")

    USERNAME_FIELD = 'moodle_id'

    REQUIRED_FIELDS = ['username']

    

class Event(models.Model):
    name = models.CharField(null=True, max_length=200)
    desc = models.TextField(null=True, max_length= 200)
    venue = models.CharField(null=True, max_length= 200)
    date = models.DateField()
    time = models.TimeField()
    is_doubles = models.BooleanField(default = False)
    img = models.ImageField(upload_to='images', null=True, blank=True, default='logo.png')
    slug = models.SlugField(default="", null=False)


    def __str__(self):
        return str(self.name)

class Rule(models.Model):
    name = models.CharField(null=True, max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class eventHead(models.Model):
    name = models.CharField(null=True, max_length= 200)
    contact = models.BigIntegerField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Signed(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='p1')
    participant2 = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name = 'p2')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    dept = models.CharField(max_length=6, null=True)
    year = models.CharField(max_length=6, null=True)
    pname1 = models.CharField(max_length= 200, blank=True)
    pname2 = models.CharField(max_length= 200, blank= True)
    ename = models.CharField(null=True, max_length= 200)
# Create your models here.
