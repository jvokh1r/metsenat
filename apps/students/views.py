from apps.application.forms import SponsorUpdateForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from apps.students.models import University
from apps.students.forms import StudentForm, StudentAddForm, SponsorStudentAddForm, UniversityForm
from apps.application.models import Sponsor
from apps.students.models import Student, SponsorStudent


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


class SponsorsView(View):
    def get(self, request):
        sponsors = Sponsor.objects.all().order_by('-pk')
        # filter
        filter_sponsor = request.POST.get("filter_sponsors")
        filter_amount = request.POST.get("filter_amount")
        from_date = request.POST.get("from")
        to_date = request.POST.get("to")
        if filter_sponsor and filter_amount and from_date and to_date:
            print(1111111111111111111111111111111111111111111111111111)
            sponsors = sponsors.filter(status=filter_sponsor, amount=filter_amount,
                                       created_at__range=[from_date, to_date])
        ctx = {
            'sponsors': sponsors
        }
        return render(request, 'dashboard/sponsors.html', ctx)


class SponsorsDeleteView(DeleteView):
    queryset = Sponsor.objects.all()
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('sponsors')


class SponsorDetailView(DetailView):
    model = Sponsor
    context_object_name = 'sponsor'
    template_name = 'dashboard/detail_edit_sponsor.html'


class SponsorUpdateDetailView(UpdateView):
    model = Sponsor
    form_class = SponsorUpdateForm
    template_name = 'dashboard/detail_edit_sponsor.html'
    success_url = reverse_lazy('sponsors')


# students
class StudentsListView(ListView):
    template_name = 'dashboard/students.html'
    queryset = Student.objects.order_by("-pk")


class StudentsUpdateDetailView(UpdateView):
    model = Student
    form_class = StudentForm
    context_object_name = 'student'
    template_name = 'dashboard/detail_edit_student.html'
    success_url = reverse_lazy('students')

    def get_context_data(self, **kwargs):
        context_data = super(StudentsUpdateDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        student = get_object_or_404(Student, pk=pk)

        obj = SponsorStudent.objects.filter(student=student)
        if obj:
            context_data['sponsor_students'] = obj
        return context_data


class StudentsDeleteView(DeleteView):
    queryset = Student.objects.all()
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('students')


class StudentsAddView(CreateView):
    model = Student
    form_class = StudentAddForm
    template_name = 'dashboard/add_student.html'
    success_url = reverse_lazy('students')


# student-sponsor
class StudentSponsorAddView(CreateView):
    model = SponsorStudent
    form_class = SponsorStudentAddForm
    template_name = 'dashboard/add_sponsor.html'
    success_url = reverse_lazy('students')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk = self.kwargs.get('pk')
        student = get_object_or_404(Student, pk=pk)
        kwargs['student'] = student
        return kwargs

    def form_valid(self, form):
        sponsor_student = form.instance
        sponsor = sponsor_student.sponsor
        amount = sponsor_student.amount
        student = form.student

        # Проверка перед сохранением
        if sponsor.amount < amount:
            form.add_error('amount', f'Sponsorning puli yetmaydi, uning puli {sponsor.amount} UZS')
            return self.form_invalid(form)

        sponsor_student.student = student

        response = super().form_valid(form)

        return response


class StudentSponsorUpdateView(UpdateView):
    model = SponsorStudent
    form_class = SponsorStudentAddForm
    template_name = 'dashboard/edit_sponsor.html'
    success_url = reverse_lazy('students')


class SponsorStudentDeleteView(DeleteView):
    model = SponsorStudent
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('students')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        sponsor = self.object.sponsor
        student = self.object.student
        amount = self.object.amount

        response = super().delete(request, *args, **kwargs)

        sponsor.spend_amount -= amount
        sponsor.save()

        student.sponsored_amount -= amount
        student.save()

        return response

# universities


class UniversityListView(ListView):
    queryset = University.objects.order_by("-pk")
    template_name = 'dashboard/universities.html'
    context_object_name = 'universities'


class UniversityAddView(CreateView):
    model = University
    form_class = UniversityForm
    template_name = 'dashboard/add_university.html'
    success_url = reverse_lazy('universities')


class UniversityDeleteView(DeleteView):
    model = University
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('universities')


class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'dashboard/edit_university.html'
    form_class = UniversityForm
    success_url = reverse_lazy('universities')
