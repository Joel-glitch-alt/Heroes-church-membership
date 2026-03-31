# heroes/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('members.urls')),  # API
    path('', include('members.urls')),      # Frontend
]