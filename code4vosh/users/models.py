from django.db import models
from django.contrib.auth.models import AbstractUser
from code4vosh.settings import DEPARTMENTS

from main_site.models import Group


class SchoolStaff(models.Model):
    ''' Абстрактная модель члена коллектива школы '''
    
    bio = models.CharField(
        primary_key=True,
        max_length=100,
        verbose_name='ФИО'
    )

    department = models.CharField(
        max_length=10,
        null=True, blank=True,
        choices=DEPARTMENTS
    )

    classroom = models.ForeignKey(
        Group,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_class"
    )

    registered = models.BooleanField(
        blank=True, null=True,
        default=False,
    )

    def __str__(self):
        return self.bio

    class Meta:
        abstract = True


class Teacher(SchoolStaff):
    '''Модель сотрудника школы'''

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Pupil(SchoolStaff):
    '''Модель ученика школы'''

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


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
    is_teacher = models.BooleanField(
        verbose_name='Учитель',
        default=False
    )
    classroom = models.ForeignKey(
        Group,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='classroom_member',
        verbose_name='Класс'
    )

    def __str__(self):
        return self.username

    def get_parallel(self):
        if len(str(self.classroom)) > 2:
            return str(self.classroom)[0:2]
        return str(self.classroom)[0]

    def get_bio(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        unique_together = ('name', 'middle_name', 'surname')


