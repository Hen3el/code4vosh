from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Group, SchoolSubject


class UserProfile(AbstractUser):
    """Модель пользователя"""
    telegram_id = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='ID пользователя телеграмм',
    )
    name = models.CharField(
        max_length=20,
        verbose_name='Имя'
    )
    middle_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Отчество'
    )
    surname = models.CharField(
        max_length=20,
        verbose_name='Фамилия'
    )
    username = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Логин'
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
    )
    classroom = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='classroom',
        verbose_name='Класс',
    )
    school_subj = models.ManyToManyField(
        SchoolSubject,
        blank=True,
        related_name='school_subjects',
        verbose_name='Предметы',
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        unique_together = ('name', 'middle_name', 'surname')


class Staff(models.Model):
    '''Модель сотрудника или ученика школы'''

    bio = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    '''
    middle_name = models.CharField(
        default='1',
        name='Отчество',
        max_length=20,
        verbose_name='Отчество'
    )
    surname = models.CharField(
        default='1',
        name='Фамилия',
        max_length=20,
        verbose_name='Фамилия'
    )
    '''
    '''
    is_staff = models.BooleanField(
        verbose_name='Учитель'
    )
    '''
    def __str__(self):
        return self.bio
        return f'Ученик {self.name} {self.middle_name} {self.surname}'

    class Meta:
        verbose_name = 'Член коллектива'
        verbose_name_plural = 'Члены коллектива'
