from django.contrib import admin
from .models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'amount', 'spend_money')
