from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field
from import_export import resources
from .models import UserProfile, Staff


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'telegram_id', 'surname', 'name', 'middle_name', 'username',
        'email', 'classroom')


@admin.register(Staff)
class StaffAdmin(ImportExportActionModelAdmin):
    
    class Meta:
        model = Staff
