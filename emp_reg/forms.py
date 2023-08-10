from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  
        fields = ('fullname','mobile', 'emp_code', 'position')
        labels = {

            'fullname': 'Full name',
            'emp_code': 'EMP. Code'
        }







