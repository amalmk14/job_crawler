from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.get_profiles, name='get_profiles'),
    path('jobs/', views.get_jobs, name='get_jobs'),
]