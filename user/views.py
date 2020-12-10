from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    RolesForm,PermissionForm,EmployeeForm,
    AssignJobForm,JobForm,InterviewForm,searchForm,CallLetterForm, 
    UserRegisterForm, UserUpdateForm, ProfileUpdateForm ,
)    


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

    
def roles(request):
    if request.method == 'POST':
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = RolesForm()
    return render(request, 'user/roles.html', {'form': form})    


def permissions(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = PermissionForm()
    return render(request, 'user/permissions.html', {'form': form})


def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = EmployeeForm()
    return render(request, 'user/employee.html', {'form': form})


def assignjob(request):
    if request.method == 'POST':
        form = AssignJobForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = AssignJobForm()
    return render(request, 'jobs/jobs.html', {'form': form})

def job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = JobForm()
    return render(request, 'jobs/add_jobs.html', {'form': form})    

def interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = InterviewForm()
    return render(request, 'user/interview.html', {'form': form})   

def search(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = searchForm()
    return render(request, 'user/search.html', {'form': form})    
    
             
def call_letter(request):
    if request.method == 'POST':
        form = CallLetterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           #return redirect('login')
    else:
        form = CallLetterForm()
    return render(request, 'user/call_letter.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)

