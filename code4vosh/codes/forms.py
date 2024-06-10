from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from .models import IssuedCodes, Code
from main_site.views import SchoolSubject

class SubjForm(forms.Form):

    subject = forms.MultipleChoiceField(
            choices=(),
            widget=FilteredSelectMultiple('Предметы', is_stacked=False),
            required=True
            )
    
    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css', 'admin/css/overrides.css'),
        }
        js = ('/admin/jquery.js', '/admin/jsi18n')

    #class Meta:

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super(SubjForm, self).__init__(*args, **kwargs)
        self.fields['subject'].choices=choices


class IssueCodeForm(forms.Form):
    subject = forms.ModelChoiceField(
            queryset=SchoolSubject.objects.all(),
            required=True
            )
    
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super(IssueCodeForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset=choices
