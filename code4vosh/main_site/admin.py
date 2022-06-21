from django.contrib import admin

from .models import Group, SchoolSubject


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('class_number', 'class_litera')


@admin.register(SchoolSubject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject',)
