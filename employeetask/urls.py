from django.urls import path,include
from .views.views import add_task,all_task,take_task,finish_task


urlpatterns = [
    path('add_task',add_task,name='add_task'),
    path('all_task',all_task,name='all_task'),
    path('take_task/<int:task_id>',take_task,name='take_task'),
    path('finish_task/<int:task_id>',finish_task,name='finish_task')
]