from django.urls import path
from . import views

app_name='emp_reg'

urlpatterns = [

    path('list/', views.employee_list),
    path('', views.employee_form),
    
]