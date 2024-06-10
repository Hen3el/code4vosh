# Generated by Django 3.0 on 2022-07-15 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_remove_group_parallel'),
        ('users', '0005_pupil_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('bio', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='ФИО')),
                ('department', models.CharField(blank=True, choices=[(1, 'ALFA'), (2, 'BETA'), (3, 'GAMMA'), (4, 'DELTA'), (5, 'EVRIKA'), (6, 'OMEGA')], max_length=10, null=True)),
                ('registered', models.BooleanField(blank=True, default=False, null=True)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_class', to='main_site.Group')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.AddField(
            model_name='pupil',
            name='department',
            field=models.CharField(blank=True, choices=[(1, 'ALFA'), (2, 'BETA'), (3, 'GAMMA'), (4, 'DELTA'), (5, 'EVRIKA'), (6, 'OMEGA')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pupil_class', to='main_site.Group'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='registered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
