from django.contrib import admin
from .models import GSigned, Event, eventHead



class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(GSigned)
admin.site.register(Event, EventAdmin)
admin.site.register(eventHead)

# Register your models here.
