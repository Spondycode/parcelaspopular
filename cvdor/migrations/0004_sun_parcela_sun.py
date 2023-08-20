# Generated by Django 4.1.7 on 2023-08-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvdor', '0003_parcela_campsite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_sun', models.CharField(max_length=25, verbose_name='Full Sun')),
                ('mostly_sun', models.CharField(max_length=25, verbose_name='Mostly Sun')),
                ('sun_shadow', models.CharField(max_length=25, verbose_name='Sun and Shadow')),
                ('mostly_shadow', models.CharField(max_length=25, verbose_name='Mostly Shadow')),
                ('full_shadow', models.CharField(max_length=25, verbose_name='Full Shadow')),
            ],
        ),
        migrations.AddField(
            model_name='parcela',
            name='sun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvdor.sun'),
        ),
    ]