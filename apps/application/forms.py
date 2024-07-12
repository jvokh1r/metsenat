from django import forms
from apps.application.models import Sponsor


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        exclude = ('spend_amount', 'status',)


class SponsorUpdateForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        exclude = ()
