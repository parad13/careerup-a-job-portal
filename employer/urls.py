from django.urls import path
from . import views
from .views import (EmployeeListView)

urlpatterns = [

    path('post_jobs/', views.post_jobs, name='post-Jobs'),
    path('jobs/assign', views.assign_job, name='assign-jobs'),
    path('interviews/', views.interview, name='user-interviews'),
    path('call_letter/', views.call_letter, name='call-letter'),
    path('employee/', views.add_employee, name='add_employees'),
    path('roles/', views.roles, name='user-roles'),
    path('permissions/', views.permissions, name='user-permissions'),
    path('all_employees/', EmployeeListView.as_view(), name='all_employees'),
   
]
