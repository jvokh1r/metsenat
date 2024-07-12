# Generated by Django 5.0.7 on 2024-07-11 12:35

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'Bakalavr'), (1, 'Magistr')])),
                ('contract', models.DecimalField(decimal_places=1.0, default=Decimal('0.0'), max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('sponsored_amount', models.DecimalField(decimal_places=1.0, default=Decimal('0.0'), max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=1, default=Decimal('0.0'), max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sponsor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.university'),
        ),
    ]
