from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from .models import Parallel, Group, SchoolSubject


@admin.register(Parallel)
class ParallelAdmin(admin.ModelAdmin):
    list_display = ('number',)


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        import_id_fields = ('clsroom',)
        skip_unchanged = True
        report_skipped = True
        fields = ('clsroom',)


@admin.register(Group)
class GroupAdmin(ImportExportActionModelAdmin):
    resource_class = GroupResource


class SchoolSubjectResource(resources.ModelResource):
    class Meta:
        model = SchoolSubject
        import_id_fields = ('subject',)
        skip_unchanged = True
        report_skipped = True
        fields = ('subject', 'result_date', 'start_parallel')


@admin.register(SchoolSubject)
class SchoolSubjectAdmin(ImportExportActionModelAdmin):
    resource_class = SchoolSubjectResource
    list_display = ['subject', 'result_date']