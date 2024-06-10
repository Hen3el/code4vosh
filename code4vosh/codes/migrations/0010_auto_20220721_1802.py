# Generated by Django 3.0 on 2022-07-21 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20220721_1802'),
        ('codes', '0009_auto_20220720_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='code',
            options={'ordering': ['date_start'], 'verbose_name': 'Код', 'verbose_name_plural': 'Коды'},
        ),
        migrations.AlterField(
            model_name='code',
            name='subj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subj_code', to='main_site.SchoolSubject'),
        ),
    ]