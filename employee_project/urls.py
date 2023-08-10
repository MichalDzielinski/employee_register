from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('emp_reg.urls', namespace='emp_reg')),
]
