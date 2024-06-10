# Generated by Django 3.0 on 2022-07-17 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220715_1512'),
        ('codes', '0005_auto_20220717_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedcodes',
            name='pupil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issued_code', to='users.Pupil'),
        ),
    ]
