from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('download/<int:assignment_id>/', views.download_assignment, name='download_assignment'),
]