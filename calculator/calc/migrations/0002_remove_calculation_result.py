# Generated by Django 5.1.5 on 2025-02-04 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculation',
            name='result',
        ),
    ]
