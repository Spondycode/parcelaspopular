# Generated by Django 4.1.7 on 2023-08-19 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvdor', '0009_alter_parcela_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcela',
            name='group',
        ),
    ]