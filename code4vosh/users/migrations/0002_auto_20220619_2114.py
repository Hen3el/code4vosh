# Generated by Django 3.0 on 2022-06-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='ID пользователя телеграмм'),
        ),
    ]
