from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from jobs.models import *


class RolesForm(ModelForm):

    class Meta:
        model = roles
        fields = ['r_name' , 'r_desc']


class PermissionForm(ModelForm):

    class Meta:
        model = permissions
        fields = ['per_role_id', 'per_name', 'per_module']


class EmployeeForm(ModelForm):

    class Meta:
        model = employee
        fields = ['emp_name', 'emp_username', 'emp_mobile',
        'emp_address','emp_email','emp_password']


class AssignJobForm(ModelForm):

    class Meta:
        model = job
        fields = ['j_emp_id','j_name','j_type','j_desc']


class JobForm(ModelForm):

    class Meta:
        model = Joblist
        fields = ['title', 'type', 'desc','image' ]

class InterviewForm(ModelForm):

    class Meta:
        model = interview
        fields = ['i_job_id', 'i_title', 'i_type','i_date','i_desc']


class searchForm(ModelForm):

    class Meta:
        model = search
        fields = ['s_job_id', 's_title', 's_type', 's_desc']


class CallLetterForm(ModelForm):
   
    class Meta:
        model = call_letter
        fields = ['cl_emp_id', 'cl_job_id', 'cl_title', 'cl_type', 'cl_desc']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
