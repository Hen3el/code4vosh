# Generated by Django 3.0 on 2022-07-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_staff_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='registered',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Регистрация на сайте'),
        ),
    ]
