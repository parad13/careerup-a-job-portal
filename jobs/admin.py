from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(registration)

admin.site.register(roles)
admin.site.register(permissions)
admin.site.register(employee)
admin.site.register(job)

admin.site.register(interview)
admin.site.register(search)
admin.site.register(call_letter)
