# Generated by Django 3.0 on 2022-07-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='registered',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Регистрация на сайте'),
        ),
    ]