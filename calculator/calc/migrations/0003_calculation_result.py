# Generated by Django 5.1.5 on 2025-02-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_remove_calculation_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='result',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
