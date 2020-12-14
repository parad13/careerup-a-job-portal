from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    searchForm,UserRegisterForm, UserUpdateForm, ProfileUpdateForm,
)    
from jobs.models import job


def about(request):
    return render(request, 'jobs/about.html', {'title': 'About'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

    
def search(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'call letter successfully created')
           
    else:
        form = searchForm()
    return render(request, 'user/search.html', {'form': form})    
    

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
            return redirect('user-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)

