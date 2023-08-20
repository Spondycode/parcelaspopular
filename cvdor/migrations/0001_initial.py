# Generated by Django 4.1.7 on 2023-08-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Campsite Name')),
                ('address', models.CharField(max_length=320)),
                ('postcode', models.CharField(max_length=10, verbose_name='Postal Code')),
                ('w3words', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=25, verbose_name='Phone')),
                ('web', models.URLField(verbose_name='Website Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('primary_mode', models.CharField(max_length=60, verbose_name='Camper Type')),
            ],
        ),
        migrations.CreateModel(
            name='Parcelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Plot Number')),
                ('group', models.CharField(max_length=20, verbose_name='Group')),
                ('width', models.IntegerField(verbose_name='Size')),
                ('entry', models.IntegerField(verbose_name='Width of Entry')),
                ('length', models.IntegerField(verbose_name='Plot Length')),
                ('description', models.TextField(blank=True)),
                ('plot_users', models.ManyToManyField(blank=True, to='cvdor.users')),
            ],
        ),
    ]