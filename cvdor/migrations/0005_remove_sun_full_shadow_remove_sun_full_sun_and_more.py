# Generated by Django 4.1.7 on 2023-08-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvdor', '0004_sun_parcela_sun'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sun',
            name='full_shadow',
        ),
        migrations.RemoveField(
            model_name='sun',
            name='full_sun',
        ),
        migrations.RemoveField(
            model_name='sun',
            name='mostly_shadow',
        ),
        migrations.RemoveField(
            model_name='sun',
            name='mostly_sun',
        ),
        migrations.RemoveField(
            model_name='sun',
            name='sun_shadow',
        ),
        migrations.AddField(
            model_name='sun',
            name='sun',
            field=models.CharField(default='sun', max_length=25, verbose_name='SunOrShadow'),
            preserve_default=False,
        ),
    ]
