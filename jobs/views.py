from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,UpdateView,DeleteView)
from .models import Postjobs, job,employee

def home(request):
    context1 = {
        'jobs': Postjobs.objects.all()
    }
    return render(request, 'home.html', context1)

class JobListView(ListView):
    model = job
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'jobs'
    #ordering = ['-i_date']

class JobDetailView(DetailView):
    model = job


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = job
    fields = ['j_name', 'j_type','j_desc']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = job
    success_url = '/'

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class JobPostListView(ListView):
    model = job
    template_name = 'jobs/user_jobs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'jobs'
    #paginate_by = 5

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_posted')
