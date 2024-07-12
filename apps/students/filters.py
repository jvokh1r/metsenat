import django_filters

from apps.application.models import Sponsor


class SponsorFilter(django_filters.FilterSet):
    class Meta:
        model = Sponsor
        fields = ["status", "amount", "created_at"]


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Sponsor
        fields = ["university", "level"]

