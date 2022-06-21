from django.db import models


class Group(models.Model):
    class_number = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        verbose_name='Параллель'
    )
    class_litera = models.TextField(
        verbose_name='Литера'
    )

    def __str__(self):
        return str(self.class_number) + self.class_litera


class SchoolSubject(models.Model):
    subject = models.CharField(
        max_length=50,
        verbose_name='Предмет'
    )

    def __str__(self):
        return self.subject
