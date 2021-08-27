from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('status/', views.status, name='tasks-status'),
]
