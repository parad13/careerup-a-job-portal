from django.contrib import admin
from jobs.models import *
# Register your models here.

admin.site.register(roles)
admin.site.register(permissions)
admin.site.register(employee)
admin.site.register(interview)
admin.site.register(call_letter)
admin.site.register(Postjobs)