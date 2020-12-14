from django.shortcuts import render
from django.views.generic import ListView
from .forms import *
from django.contrib import messages
from user.forms import  JobForm 
# Create your views here.

def assign_job(request):
    if request.method == 'POST':
        form = AssignJobForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')

    else:
        form = AssignJobForm()
    return render(request, 'employer/jobs.html', {'form': form})


def post_jobs(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Job successfully added')

    else:
        form = JobForm()
    return render(request, 'employer/post_jobs.html', {'form': form})


def interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Interciew successfully Scheduled')

    else:
        form = InterviewForm()
    return render(request, 'employer/interview.html', {'form': form})


context = {
    'emps': employee.objects.all()
}

def emp(request):
    context = {
        'emps': employee.objects.all()
    }
    return render(request, 'employer/all_emp.html', context)


class EmployeeListView(ListView):
    model = employee
    template_name = 'employer/all_emp.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'emps'



def roles(request):
    if request.method == 'POST':
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')

    else:
        form = RolesForm()
    return render(request, 'employer/roles.html', {'form': form})


def permissions(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')

    else:
        form = PermissionForm()
    return render(request, 'employer/permissions.html', {'form': form})

def call_letter(request):
    if request.method == 'POST':
        form = CallLetterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           
    else:
        form = CallLetterForm()
    return render(request, 'employer/call_letter.html', {'form': form})
    
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Employee successfully added')

    else:
        form = EmployeeForm()
    return render(request, 'employer/employee.html', {'form': form})



