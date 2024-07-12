from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.application.urls')),
    path('dashboard/', include('apps.students.urls'))
]
