from django.urls import path
from .views import frontend

urlpatterns = [
    path('', frontend, name='frontend'),
]