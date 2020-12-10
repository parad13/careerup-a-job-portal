from django.urls import path
from .views import (JobDetailView,JobListView, JobUpdateView, JobDeleteView)
from . import views

urlpatterns = [

    path('', JobListView.as_view(), name='jobs-home'),
    path('about/', views.about, name='jobs-about'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job-detail'),
    # path('job/allemp', views.emp, name='emp')
    
    #yet to active
    
    # path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    # path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    #path('job/<str:username>', JobPostListView.as_view(), name='job-posts')
    
]
