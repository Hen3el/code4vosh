# Generated by Django 3.0 on 2022-07-05 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='Код олимпиады')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(verbose_name='Дата окончания')),
                ('parallel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='for_class', to='main_site.Parallel')),
            ],
            options={
                'verbose_name': 'Код',
                'verbose_name_plural': 'Коды',
            },
        ),
        migrations.CreateModel(
            name='CodeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.FileField(upload_to='CodeTables')),
            ],
        ),
        migrations.CreateModel(
            name='IssuedCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Предмет')),
                ('pupil', models.CharField(max_length=100, verbose_name='Кому выдан')),
                ('issue_date', models.DateField(auto_now_add=True, verbose_name='Время выдачи')),
                ('result_date', models.DateField(blank=True, null=True, verbose_name='Оглашение результатов')),
                ('result', models.CharField(max_length=100, verbose_name='Результат')),
                ('max_result', models.CharField(max_length=4, null=True, verbose_name='Максимум баллов')),
                ('code', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codes.Code', verbose_name='Выданный код')),
            ],
            options={
                'verbose_name': 'Выданный код',
                'verbose_name_plural': 'Выданные коды',
            },
        ),
    ]