# Generated by Django 5.1.5 on 2025-01-22 11:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0007_remove_osoba_data_dodania'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
