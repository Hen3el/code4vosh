# Generated by Django 3.0 on 2022-06-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220619_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=10, verbose_name='ID пользователя телеграмм'),
        ),
    ]