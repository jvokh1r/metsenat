from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.application.models import Sponsor
from django.core.validators import MinValueValidator


class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    class Level(models.IntegerChoices):
        Bakalavr = 0
        Magistr = 1

    full_name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(choices=Level.choices)
    contract = models.DecimalField(max_digits=20, decimal_places=1, validators=[MinValueValidator(0)])
    sponsored_amount = models.DecimalField(max_digits=20, decimal_places=1, validators=[MinValueValidator(0)],
                                           default=Decimal("0.0"))

    def __str__(self):
        return self.full_name


class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=1, validators=[MinValueValidator(0)],
                                 default=Decimal("0.0"))

    def __str__(self):
        return self.sponsor.full_name

    def clean(self):
        if self.sponsor.amount < self.amount:
            raise ValidationError({'amount': f'Sponsorning puli yetmaydi, uning puli {self.sponsor.amount} UZS'})
