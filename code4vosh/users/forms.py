from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import NON_FIELD_ERRORS
from .models import UserProfile


class UserCreation(UserCreationForm):
    '''Форма регистрации пользователя'''

    class Meta:
        model = UserProfile
        fields = [
            'surname', 'name', 'middle_name', 'username',
            'email'
        ]
        labels = {
            'name': 'Имя',
            'middle_name': 'Отчество',
            'surname': 'Фамилия',
            'username': 'Логин',
            'email': 'Адрес электронной почты',
        }
        help_texts = {
            'middle_name': 'Пожалуйста, укажите отчество, если вы учитель',
            'username': 'В качестве логина можно использовать логин от ЭЖД или любой другой, который вы запомните',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Пользователь с такими ФИО уже зарегистрирован. Если вы забыли пароль, воспользуйтесь восстановлением пароля на странице входа",
            }
        }



'''
    school_subj = forms.ModelMultipleChoiceField(
            queryset=SchoolSubject.objects.all(),
            widget=forms.CheckboxSelectMultiple,
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

    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = (
            'telegram_id', 'surname', 'name', 'middle_name', 'username',
            'email', 'self_class', 'school_subj'
        )
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
            # 'school_subj': SchoolSubjWidget,
        }
'''
