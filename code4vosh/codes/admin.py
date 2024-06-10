from django.contrib import admin
from .models import CodeTable, Code, IssuedCodes
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from django.shortcuts import render
from django.utils.html import format_html
from django.conf.urls import url
from django.urls import reverse, path
from main_site.results import TokenResult
from django.template.response import TemplateResponse


@admin.register(CodeTable)
class CodeTableAdmin(admin.ModelAdmin):
    list_display = ('table',)



'''
class SubjWidget(Widget):
    def __init__(self, subject, *args, **kwargs):
        self.subj = SchoolSubject.objects.get()
        self.revert_choices = dict((v, k) for k, v in self.choices.items())

    def clean(self, value, row=None, *args, **kwargs):
        """Returns the db value given the display value"""
        return self.revert_choices.get(value, value) if value else None

    def render(self, value, obj=None):
        """Returns the display value given the db value"""
        return self.choices.get(value, '')
'''


class CodeResource(resources.ModelResource):
    class Meta:
        model = Code
        import_id_fields = ('code',)
        skip_unchanged = True
        report_skipped = True
        fields = ('code', 'subj',  'parallel', 'date_start', 'date_end',)


@admin.register(Code)
class CodeAdmin(ImportExportActionModelAdmin):
    resource_class = CodeResource
    list_display = ['code', 'subj',  'parallel', 'date_start', 'date_end', 'issued_to', 'issue_date']
    search_fields = ['pupil__bio']
    list_filter = ['issued_to']


@admin.register(IssuedCodes)
class IssuedCodesAdmin(admin.ModelAdmin):
    list_display = ('code', 'pupil', 'issue_date', 'result', 'max_result')
    actions = [TokenResult]
'''
    def get_urls(self):
        urls = super(IssuedCodesAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^result/$', self.admin_site.admin_view(self.process_get_result),
                name='get_result',
            )
        ]
        return custom_urls + urls

    def issued_codes_action(self, obj):
        return format_html(
            '<a class="button" href="{}">Обновить результаты</a> ',
            reverse('admin:get_result', args=[obj.pk]),
        )
    issued_codes_action.short_description = 'Обновление результатов'
    issued_codes_action.allow_tags = True

    def process_get_result(self, request, *args, **kwargs):
        tokens = IssuedCodes.objects.filter(result=None)
        get_result(tokens)
        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        return render(
            request,
            'admin/change_list.html',
            context
        )
        '''