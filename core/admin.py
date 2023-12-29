from django.contrib import admin
from . import models
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('moodle_id', 'username', 'password1', 'password2', 'fname', 'lname', 'dept', 'year')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.User
        fields = ('moodle_id', 'username', 'fname', 'lname', 'dept', 'year', 'is_active', 'is_staff')

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('moodle_id', 'username', 'fname', 'lname', 'dept', 'year', 'is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('moodle_id', 'username', 'fname', 'lname', 'dept', 'year')
    ordering = ('moodle_id',)

    fieldsets = (
        (None, {'fields': ('moodle_id', 'password')}),
        ('Personal Info', {'fields': ('username', 'fname', 'lname', 'dept', 'year', 'is_active', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('moodle_id', 'username', 'password1', 'password2'),
        }),
    )

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

class UserAdmin(ImportExportModelAdmin, CustomUserAdmin):
    resource_class = UserResource
    prepopulated_fields = {"username": ("moodle_id",)}

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

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.eventHead)
admin.site.register(models.Rule)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Signed, SignedAdmin)
admin.site.register(models.User, UserAdmin)
