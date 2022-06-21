from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import Textarea, ModelForm
from .models import SchoolSubject


class TeacherCreationForm(ModelForm):
    '''Форма регистрации учителя'''
    school_subj = forms.ModelMultipleChoiceField(
        queryset=SchoolSubject.objects.all(),
        widget=FilteredSelectMultiple("Предметы", is_stacked=False),
        required=True
    )

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

    def clean_subj_choise(self):
        subj_choise = self.cleaned_data['school_subj']
        return subj_choise
    '''
    school_subj = forms.ModelMultipleChoiceField(
            queryset=SchoolSubject.objects.all(),
            # widget=forms.CheckboxSelectMultiple,
            required=True
        )
    CHOICES=(
        ('math', 'geometry'),
        ('algebra', 'alg')
    )
    school_subj = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    '''

    class Meta:
        # model = Teacher
        fields = [
            'telegram_id', 'surname', 'name', 'middle_name', 'username',
            'email', 'self_class', 'school_subj'
        ]
        labels = {
            'name': 'Имя',
            'middle_name': 'Отчество',
            'surname': 'Фамилия',
            'username': 'Логин',
            'email': 'Адрес электронной почты',
            'self_class': 'Классное руководство',
            'school_subj': 'Преподаваемые предметы'
        }
        widgets = {
            'name': Textarea(attrs={'rows': 1, 'cols': 40}),
            'middle_name': Textarea(attrs={'rows': 1, 'cols': 40}),
            'surname': Textarea(attrs={'rows': 1, 'cols': 40}),
            'username': Textarea(attrs={'rows': 1, 'cols': 40}),
            # 'school_subj': forms.CheckboxSelectMultiple,
        }



