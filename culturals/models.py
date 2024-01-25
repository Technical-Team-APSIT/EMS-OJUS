from django.db import models
from core.views import User

class GSigned(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    moodle_id = models.CharField(unique=True, primary_key=True, max_length=100)
    pname = models.CharField(max_length= 200, blank=True)
    contact = models.BigIntegerField(null=True)
    dept = models.CharField(max_length=6, null=True)
    year = models.CharField(max_length=6, null=True)
    scanned = models.BooleanField(default=False)



# Create your models here.
