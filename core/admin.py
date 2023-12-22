from django.contrib import admin
from . import models
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields
from django import forms

admin.site.register(models.Event)
admin.site.register(models.eventHead)
admin.site.register(models.Rule)

class SignedAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('event_name', 'fname', 'lname', 'id', 'dept', 'year')
    list_filter = ('event__name',)

    
    def event_name(self, obj):
        return obj.event.name

    def fname(self, obj):
        return obj.participant.fname

    def lname(self, obj):
        return obj.participant.lname

    def id(self, obj):
        return obj.participant.id

    def dept(self, obj):
        return obj.participant.dept

    def year(self, obj):
        return obj.participant.year

class UserResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    fname = fields.Field(column_name='fname')
    lname = fields.Field(column_name='lname')
    password = fields.Field(column_name='password')
    dept = fields.Field(column_name='dept')
    year = fields.Field(column_name='year')

    class Meta:
        model = models.User



        fields = ('id', 'fname', 'lname', 'password', 'dept', 'year')





class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ('id', 'dept', 'year', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'fname', 'lname')
    search_fields = ['id', 'username', 'email', 'fname', 'lname']
    ordering = ('id',)



admin.site.register(models.Signed, SignedAdmin)
admin.site.register(models.User, UserAdmin)





# Register your models here.
