from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field
from import_export import resources
from .models import UserProfile, Teacher, Pupil


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'telegram_id', 'surname', 'name', 'middle_name', 'username',
        'email', 'is_staff')


class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        import_id_fields = ('bio',)
        skip_unchanged = True
        report_skipped = False
        fields = ('bio', 'classroom')


class PupilResource(resources.ModelResource):
    class Meta:
        model = Pupil
        import_id_fields = ('bio',)
        skip_unchanged = True
        report_skipped = False
        fields = ('bio', 'classroom')


@admin.register(Teacher)
class TeacherAdmin(ImportExportActionModelAdmin):
    resource_class = TeacherResource
    list_display = ('bio', 'classroom', 'registered')


@admin.register(Pupil)
class PupilAdmin(ImportExportActionModelAdmin):
    resource_class = PupilResource
    list_display = ('bio', 'classroom', 'registered')