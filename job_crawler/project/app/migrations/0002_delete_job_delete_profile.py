# Generated by Django 5.1.4 on 2025-01-06 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]