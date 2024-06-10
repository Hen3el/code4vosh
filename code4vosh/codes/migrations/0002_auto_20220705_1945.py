# Generated by Django 3.0 on 2022-07-05 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('codes', '0001_initial'),
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='pupil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Pupil', verbose_name='Ученик'),
        ),
        migrations.AddField(
            model_name='code',
            name='subj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_subj', to='main_site.SchoolSubject'),
        ),
    ]