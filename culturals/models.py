from django.db import models
from core.views import User

class GSigned(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    moodle_id = models.CharField(unique=True, primary_key=True, max_length=100)
    pname = models.CharField(max_length= 200, blank=True)
    contact = models.BigIntegerField(null=True)
    dept = models.CharField(max_length=6, null=True)
    year = models.CharField(max_length=6, null=True)
    scanned = models.IntegerField(default=2)


class Event(models.Model):
    name = models.CharField(null=True, max_length=200)
    desc = models.TextField(null=True, max_length= 200)
    venue = models.CharField(null=True, max_length= 200)
    date = models.DateField()
    time = models.TimeField()
    fill = models.BooleanField(default=True)


    

    img = models.ImageField(upload_to='images', null=True, blank=True, default='logo.png')
    slug = models.SlugField(default="", null=False)


    def __str__(self):
        return str(self.name)
    

class eventHead(models.Model):
    name = models.CharField(null=True, max_length= 200)
    contact = models.BigIntegerField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(f""+self.event.name+"_"+self.name+"")    
    
class Signed(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.BigIntegerField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    dept = models.CharField(max_length=6, null=True)
    year = models.CharField(max_length=6, null=True)
    pname = models.CharField(max_length= 200, blank=True)
    ename = models.CharField(null=True, max_length= 200)








# Create your models here.
