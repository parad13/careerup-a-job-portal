from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user,employee





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

class EmployeeForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = employee
        fields = ['emp_name''emp_email','emp_address','emp_mobile']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['image']
