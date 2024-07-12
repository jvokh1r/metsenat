from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .models import Sponsor

from apps.application.forms import SponsorForm


# def home(request):
#     form = SponsorForm()
#     if form.is_valid():
#         form.save()
#     else:
#         messages.error(request, form.errors)
#     ctx = {
#         'form': form,
#     }
#     return render(request, 'application.html', ctx)

class ApplyCreateView(View):
    def get(self, request):
        ctx = {
            'form': SponsorForm(),
        }
        return render(request, 'application.html', ctx)

    def post(self, request):
        data = request.POST
        form = SponsorForm(data=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'arizangiz yuborildi')
        else:
            messages.error(request, form.errors)

        return redirect('home')

# class ApplyCreateView(CreateView):
#     model = Sponsor
#     template_name = 'application.html'
#     form_class = SponsorForm

