from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='emp_reg'

urlpatterns = [

    path('list/', views.employee_list, name='emp_list'),
    path('<int:id>/', views.employee_form, name='emp_update'),
    path('delete/<int:id>/', views.employee_delete, name='emp_delete'),
    path('', views.employee_form, name='emp_insert'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)