from django.forms import ModelForm
from jobs.models import employee,job,interview,roles,permissions,call_letter

class EmployeeForm(ModelForm):

    class Meta:
        model = employee
        fields = ['emp_name', 'emp_username', 'emp_mobile',
                  'emp_address', 'emp_email', 'emp_password']

class AssignJobForm(ModelForm):

    class Meta:
        model = job
        fields = ['j_emp_id', 'j_name', 'j_type', 'j_desc']


class InterviewForm(ModelForm):

    class Meta:
        model = interview
        fields = ['i_job_id', 'i_title', 'i_type', 'i_date', 'i_desc']


class RolesForm(ModelForm):

    class Meta:
        model = roles
        fields = ['r_name', 'r_desc']


class PermissionForm(ModelForm):

    class Meta:
        model = permissions
        fields = ['per_role_id', 'per_name', 'per_module']


class CallLetterForm(ModelForm):

    class Meta:
        model = call_letter
        fields = ['cl_emp_id', 'cl_job_id', 'cl_title', 'cl_type', 'cl_desc']
