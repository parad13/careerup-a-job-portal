from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
# Create your models here.
        
class roles(models.Model):
    r_name = models.CharField(max_length=100)
    r_desc = models.TextField()
    USERNAME_FIELD = 'r_name'

    def __str__(self):
        return self.r_name


class permissions(models.Model):
    per_role_id = models.ForeignKey(roles, default=None,on_delete=models.CASCADE)
    per_name = models.CharField(max_length=100)
    per_module = models.CharField(max_length=100)

    def __str__(self):
        return self.per_name


class employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_username = models.CharField(max_length=100)  # Same as name varchar(100)
    emp_mobile = models.IntegerField()  # same as price int
    emp_address = models.CharField(max_length=200)
    emp_email = models.EmailField(max_length=254)
    emp_password = models.CharField(max_length=50)
    USERNAME_FIELD = 'emp_username'
    def __str__(self):
        return self.emp_username

class job(models.Model):
    j_emp_id = models.ForeignKey(employee,default=None,on_delete=models.CASCADE)
    j_name = models.CharField(max_length=100)
    j_type = models.CharField(max_length=100)
    j_desc = models.TextField()
    

    def __str__(self):
        return self.j_name
    
    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})

class interview(models.Model):
    i_job_id = models.ForeignKey(job, default=None, on_delete=models.CASCADE)
    i_title = models.CharField(max_length=100)
    i_type = models.CharField(max_length=100)
    i_date = models.DateTimeField(default=timezone.now)
    i_desc = models.TextField()


class search(models.Model):
    s_job_id = models.ForeignKey(job,default=None,on_delete=models.CASCADE)
    s_title = models.CharField(max_length=100)
    s_type = models.CharField(max_length=100)
    s_desc = models.TextField()


class call_letter(models.Model):
    cl_emp_id = models.ForeignKey(
        employee, default=None, on_delete=models.CASCADE)
    cl_job_id = models.ForeignKey(job, default=None,on_delete=models.CASCADE)
    cl_title = models.CharField(max_length=100)
    cl_type = models.CharField(max_length=100)
    cl_desc = models.TextField()
    USERNAME_FIELD = 'cl_emp_id'


class Postjobs(models.Model):
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics')
    title = models.CharField(max_length=45)
    type = models.CharField(max_length=45)  # wfh/part
    date = models.DateTimeField(default=timezone.now)
    desc = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} Postjobs'

    def save(self, *args, **kwargs):
        super(Postjobs, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)









