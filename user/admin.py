from django.contrib import admin
from .models import Profile
from jobs.models import search
# Register your models here.

admin.site.register(Profile)
admin.site.register(search)
