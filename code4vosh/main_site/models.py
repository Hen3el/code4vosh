from tabnanny import verbose
from django.db import models

# from users.models import UserProfile


class Parallel(models.Model):
    number = models.DecimalField(
        primary_key=True,
        max_digits=2,
        decimal_places=0,
        verbose_name='Параллель'
    )

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Параллель'
        verbose_name_plural = 'Параллели'


class Group(models.Model):
    clsroom = models.CharField(
        primary_key=True,
        max_length=4,
        verbose_name='Класс'
    )

    def get_parallel(self):
        if len(self.clsroom) > 2:
            return self.clsroom[0:2]
        return self.clsroom[0]  

    def __str__(self):
        return self.clsroom
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class SchoolSubject(models.Model):
    subject = models.CharField(
        primary_key=True,
        max_length=100,
        verbose_name='Предмет'
    )
    result_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Результат ожидается'
    )
    start_parallel = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        verbose_name='Доступна с класса'
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['subject']


'''
class Person(models.Model):
    id = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile'
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
    is_pupil = models.BooleanField(
        verbose_name='Ученик'
    )
'''
