# Generated by Django 3.1.1 on 2020-09-16 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardgames', '0002_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='value',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(13)]),
        ),
    ]