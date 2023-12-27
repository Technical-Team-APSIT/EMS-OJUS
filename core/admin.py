from django.contrib import admin
from . import models
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields
from django import forms

admin.site.register(models.eventHead)
admin.site.register(models.Rule)

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

class UserResource(resources.ModelResource):
    moodle_id = fields.Field(column_name='moodle_id', attribute='moodle_id')
    fname = fields.Field(column_name='fname', attribute='fname')
    lname = fields.Field(column_name='lname', attribute='lname')
    password = fields.Field(column_name='password', attribute='password')
    dept = fields.Field(column_name='dept', attribute='dept' )
    year = fields.Field(column_name='year', attribute='year')

    class Meta:
        model = models.User



        fields = ('moodle_id', 'fname', 'lname', 'password', 'dept', 'year')





class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ('moodle_id', 'dept', 'year', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'fname', 'lname')
    search_fields = ['moodle_id', 'username', 'email', 'fname', 'lname']
    ordering = ('moodle_id',)
    prepopulated_fields = {"username" : ("moodle_id",)}

class EventAdmin(admin.ModelAdmin):
      prepopulated_fields = {"slug": ("name",)}



admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Signed, SignedAdmin)
admin.site.register(models.User, UserAdmin)





# Register your models here.
