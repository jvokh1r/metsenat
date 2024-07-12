from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('sponsors/', views.SponsorsView.as_view(), name="sponsors"),
    path('students/', views.StudentsListView.as_view(), name="students"),
    path('sponsors/<int:pk>/delete/', views.SponsorsDeleteView.as_view(), name="delete_sponsors"),
    path('sponsors/<int:pk>/update-detail/', views.SponsorUpdateDetailView.as_view(), name="update_detail_sponsors"),
    path('students/<int:pk>/update-detail/', views.StudentsUpdateDetailView.as_view(), name="update_detail_students"),
    path('students/<int:pk>/delete/', views.StudentsDeleteView.as_view(), name="delete_students"),
    path('students/add/', views.StudentsAddView.as_view(), name="add_students"),
    path('students/<int:pk>/update-detail/add-sponsor/', views.StudentSponsorAddView.as_view(), name="add_sponsors"),
    path('students/<int:pk>/update-detail/delete-sponsor/', views.SponsorStudentDeleteView.as_view(),
         name="delete_sponsor_student"),
    path('students/<int:pk>/update-detail/update-sponsor/', views.StudentSponsorUpdateView.as_view(),
         name="update_sponsor_student"),
    path('universities/', views.UniversityListView.as_view(), name="universities"),
    path('universities/add/', views.UniversityAddView.as_view(), name="add_university"),
    path('universities/<int:pk>/delete/', views.UniversityDeleteView.as_view(), name="delete_university"),
    path('universities/<int:pk>/update/', views.UniversityUpdateView.as_view(), name="update_university"),
]