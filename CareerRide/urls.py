from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("", include("jobs.urls")),
    path("", include("user.urls")),
    path("", include("employer.urls")),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


