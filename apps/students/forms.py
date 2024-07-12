from django import forms

from apps.students.models import Student, SponsorStudent, University


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class SponsorStudentAddForm(forms.ModelForm):
    class Meta:
        model = SponsorStudent
        exclude = ('student',)

    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        sponsor = cleaned_data.get('sponsor')
        amount = cleaned_data.get('amount')

        if sponsor and amount:
            if sponsor.amount < amount:
                raise forms.ValidationError({
                    'amount': f'Sponsorning puli yetmaydi, uning puli {sponsor.amount} UZS',
                })

        return cleaned_data


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = "__all__"
