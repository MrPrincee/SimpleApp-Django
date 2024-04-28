from django.urls import path,include
from .views.views import employees


urlpatterns = [
    path('test',employees,name='employees')
]