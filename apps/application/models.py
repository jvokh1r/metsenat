from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from apps.application.validators import validate_phone_number


class Sponsor(models.Model):
    class Type(models.IntegerChoices):
        jismoniy_shaxs = 0
        yuridik_shaxs = 1

    class Status(models.IntegerChoices):
        yangi = 0
        moderatsiyada = 1
        tasdiqlangan = 2
        bekor_qilingan = 3

    class PaymentMethod(models.IntegerChoices):
        naqd = 0
        plastik_karta = 1

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=17, validators=[validate_phone_number])

    amount = models.DecimalField(max_digits=20, decimal_places=1, validators=[MinValueValidator(0)],
                                 default=Decimal("0.0"))
    spend_amount = models.DecimalField(max_digits=20, decimal_places=1, validators=[MinValueValidator(0)],
                                       default=Decimal("0.0"), blank=True)

    type = models.PositiveSmallIntegerField(choices=Type.choices)
    company_name = models.CharField(max_length=255, blank=True)

    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.yangi)
    payment_type = models.PositiveSmallIntegerField(choices=PaymentMethod.choices)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.type == 0:
            self.company_name = ''
        super().save(*args, **kwargs)

    def clean(self):
        if self.type == 1 and self.company_name == '':
            raise ValidationError({'company_name': 'Korxona nomini kiriting!'})

    def spend_money(self, amount):
        if amount > self.amount:
            raise ValidationError('Cannot spend more than the available amount.')
        self.amount -= amount
        self.spend_amount += amount
        self.save()


