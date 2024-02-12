from django.contrib import admin
from .models import GSigned, Event, eventHead, Signed
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields



class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SignedAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('event_name', 'fname', 'lname', 'moodle_id', 'dept', 'year')
    list_filter = ('event__name',)

    def event_name(self, obj):
        return obj.event.name

    def fname(self, obj):
        return obj.participant.fname

    def lname(self, obj):
        return obj.participant.lname

    def moodle_id(self, obj):
        return obj.participant.moodle_id

    def dept(self, obj):
        return obj.participant.dept

    def year(self, obj):
        return obj.participant.year

admin.site.register(Signed, SignedAdmin)

admin.site.register(GSigned)
admin.site.register(Event, EventAdmin)
admin.site.register(eventHead)

# Register your models here.
