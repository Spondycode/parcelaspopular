# Generated by Django 4.1.7 on 2023-08-18 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvdor', '0002_rename_parcelas_parcela_rename_users_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='campsite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvdor.campsite'),
        ),
    ]
