from django.urls import path
from . import views

urlpatterns = [
    path('class_list/<int:assignment_list_id>/', views.assignment_list, name='assignment_list'),
    path('', views.class_list, name='class_list'),
    path('download/<int:assignment_id>/', views.download_assignment, name='download_assignment'),
]