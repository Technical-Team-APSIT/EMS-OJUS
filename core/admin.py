from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Event)
admin.site.register(models.Signed)
admin.site.register(models.eventHead)



# Register your models here.
