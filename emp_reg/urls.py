from django.urls import path
from . import views

app_name='emp_reg'

urlpatterns = [

    path('list/', views.employee_list, name='emp_list'),
    path('<int:id>/', views.employee_form, name='emp_update'),
    path('delete/<int:id>/', views.employee_delete, name='emp_delete'),
    path('', views.employee_form, name='emp_insert'),
    
]