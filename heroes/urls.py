from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ API routes
    path('api/', include('members.api_urls')),

    # ✅ Frontend
    path('', include('members.urls')),
]

