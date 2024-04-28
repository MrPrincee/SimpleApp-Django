from django.shortcuts import render, redirect,HttpResponse
from employeemanager.views.forms import AddEmployee
from employeemanager.models import Employee


def employees(request):
    form = AddEmployee(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            salary = form.cleaned_data['salary']
            rank = form.cleaned_data['rank']
            balance = form.cleaned_data['balance']
            new_employee = Employee(name=name,surname=surname,salary=salary,rank=rank,balance=balance)
            new_employee.save()
            return redirect('home')

    return render(request,'all_employees/all_employees.html',{'form':form})
