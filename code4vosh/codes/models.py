from django.db import models
import datetime as dt
from main_site.models import Parallel, SchoolSubject
from users.models import UserProfile


class Code(models.Model):
    code = models.CharField(
        primary_key=True,
        max_length=30,
        unique=True,
        verbose_name='Код олимпиады'
    )
    subj = models.ForeignKey(
        SchoolSubject,
        related_name='subj_code',
        null=True,
        on_delete=models.SET_NULL
    )
    parallel = models.ForeignKey(
        Parallel,
        related_name='for_class',
        null=True,
        on_delete=models.SET_NULL
    )
    date_start = models.DateField(
        verbose_name='Дата начала',
    )
    date_end = models.DateField(
        verbose_name='Дата окончания',
    )
    issued_to = models.ForeignKey(
        UserProfile,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        verbose_name='Выдан',
        related_name='issued_code'
    )
    issue_date = models.DateField(
        null=True,
        verbose_name='Время выдачи',
    )
    result = models.CharField(
        max_length=100,
        null=True,
        verbose_name='Результат'
    )
    max_result = models.CharField(
        max_length=4,
        null=True,
        verbose_name='Максимум баллов'
    )

    def __str__(self):
        return self.code

    def set_issue_date(self):
        self.issue_date = dt.datetime.now()

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'
        ordering = ['date_start']


class CodeTable(models.Model):
    table = models.FileField(upload_to='CodeTables')



class IssuedCodes(models.Model):
    code = models.OneToOneField(
        Code,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Выданный код',
        related_name='issued_code',
    )

    #subject = models.CharField(
    #    max_length=100,
    #    verbose_name='Предмет'
    #)
    
    pupil = models.CharField(
        max_length=100,
        verbose_name='Кому выдан'
    )

    issue_date = models.DateField(
        auto_now_add=True,
        verbose_name='Время выдачи',
    )

    #result_date = models.DateField(
    #    blank=True, null=True,
    #    verbose_name='Оглашение результатов',
    #)

    result = models.CharField(
        max_length=100,
        verbose_name='Результат'
    )

    max_result = models.CharField(
        max_length=4,
        null=True,
        verbose_name='Максимум баллов'
    )

    class Meta:
        verbose_name = 'Выданный код'
        verbose_name_plural = 'Выданные коды'