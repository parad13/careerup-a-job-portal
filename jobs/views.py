from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import job,employee

#Function Based Views

def about(request):
    return render(request, 'jobs/about.html', {'title': 'About'})

def home(request):
    context = {
        'jobs': job.objects.all()
    }
    return render(request, 'jobs/home.html', context)


# def emp(request):
#     context = {
#         'emps': employee.objects.all()
#     }
#     return render(request, 'jobs/all_emp.html', context)

class JobListView(ListView):
    model = job
    template_name = 'jobs/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'jobs'
    #ordering = ['-i_date']

class JobDetailView(DetailView):
    model = job


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = job
    fields = ['j_name', 'j_type','j_desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = job
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


posts = [
    {
        'j_emp_id': 'Paras',
        'j_name': 'Python Dev',
        'j_type': 'Temporary',
        'j_desc': 'Lorem ipsum'
    },
    {'j_emp_id': 'Shreya',
        'j_name': 'Java Dev',
        'j_type': 'Temporary',
        'j_desc': 'Lorem ipsum'
     }
]
