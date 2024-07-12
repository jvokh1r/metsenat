# Generated by Django 5.0.7 on 2024-07-11 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contract',
            field=models.DecimalField(decimal_places=1, max_digits=20, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]