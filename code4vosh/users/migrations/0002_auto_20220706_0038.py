# Generated by Django 3.0 on 2022-07-05 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_remove_group_parallel'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom_lead', to='main_site.Group', verbose_name='Классное руководство'),
        ),
    ]