from django.shortcuts import render
from .forms import EmployeeForm

def employee_list(request):

    context = {}
    return render(request, 'emp_reg/employee_list.html', context)

def employee_form(request):
    form = EmployeeForm()
    context = {'form': form}
    return render(request, 'emp_reg/employee_form.html', context)

def employee_delete(request):
    return