from django.urls import path,include
from .views.views import employees,choose_employee_stat,choose_employee,update_employee


urlpatterns = [
    path('test',employees,name='employees'),
    path('choose_employee_stat',choose_employee_stat,name='choose_employee_stat'),
    path('choose_employee',choose_employee,name='choose_employee'),
    path("update_employee",update_employee,name="update_employee")
]