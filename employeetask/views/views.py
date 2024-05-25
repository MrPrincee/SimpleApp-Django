from django.shortcuts import render,redirect
from .forms import AddTaskForm
from employeetask.models import EmployeeTask


def add_task(request):
    form = AddTaskForm(request.POST or None)
    if form.is_valid():
        new_task = EmployeeTask(header=form.cleaned_data['header'],task=form.cleaned_data['task'])
        new_task.save()
        return redirect('home')

    return render(request,'add_task.html',{'form': form})


def all_task(request):
    tasks = EmployeeTask.objects.all()
    current_user = request.user.id
    return render(request,'all_tasks.html',{'tasks':tasks,'current_user':current_user})


def take_task(request,task_id):
    current_user = request.user.id
    current_task = EmployeeTask.objects.get(pk=task_id)
    current_task.status = 'Taken'
    current_task.worker = current_user
    current_task.save()
    return redirect('all_task')


def finish_task(request,task_id):
    current_task = EmployeeTask.objects.get(pk=task_id)
    current_task.status = 'Finished'
    current_task.save()
    return redirect('all_task')



