from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='tasks-home'),
    path('status/', views.status, name='tasks-status'),
]
