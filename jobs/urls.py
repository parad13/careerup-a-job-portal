from django.urls import path
#from .views import (JobDetailView, JobUpdateView, JobDeleteView, JobPostListView)
from user.views import profile
from .views import *

app_name = "jobs"

urlpatterns = [
    
    path("", JobListView.as_view(), name="home"),
    path('job/<int:pk>', JobDetailView.as_view(), name='detail'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='delete'),
    path('search/', profile, name='search'),
    
    # path("favorite/", favorite, name="favorite"),
    # path("search/", SearchView.as_view(), name="search"),
    # path('job/<str:j_emp_id>', JobPostListView.as_view(), name='job-posts'),
]

#user_posts --> employee profile
