# Generated by Django 5.1.4 on 2025-01-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
