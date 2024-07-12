from django.contrib import admin
from apps.students.models import University, Student, SponsorStudent


@admin.register(University)
class University(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'sponsored_amount')


@admin.register(SponsorStudent)
class SponsorStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor', 'student')

