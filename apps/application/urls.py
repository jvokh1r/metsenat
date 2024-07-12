from django.urls import path
from .views import ApplyCreateView

urlpatterns = [
    path('', ApplyCreateView.as_view(), name="home"),
]