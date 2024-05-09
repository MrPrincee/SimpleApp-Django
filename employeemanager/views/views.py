from django.shortcuts import render, redirect
from .forms import AddEmployee, ChooseEmployeeStat,ChooseEmployee,UpdateEmployee
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


def choose_employee_stat(request):
    form = ChooseEmployeeStat(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            stat = form.cleaned_data['stat']
            request.session['employee_stat_index'] = stat
            return redirect('update_employee')

    return render(request,'all_employees/choose_employee_stat.html',{'form': form})


def choose_employee(request):
    form =ChooseEmployee(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            employee = form.cleaned_data['employee']
            request.session['chosen_employee'] = employee.id
            return redirect('choose_employee_stat')

    return render(request,'all_employees/choose_employee.html',{'form': form})


def update_employee(request):
    form = UpdateEmployee(request.POST)
    stat = int(request.session.get('employee_stat_index',1))
    employee_id = request.session.get('chosen_employee','')
    employee = Employee.objects.get(id = employee_id)
    if request.method == 'POST':
        if form.is_valid():
            if stat == 1:
                name = form.cleaned_data['update']
                employee.name = name
                employee.save()
                return redirect('home')

            if stat == 2:
                surname = form.cleaned_data['update']
                employee.surname = surname
                employee.save()
                return redirect('home')

            if stat == 3:
                salary = float(form.cleaned_data['update'])
                employee.salary = salary
                employee.save()
                return redirect('home')

            if stat == 4:
                rank = int(form.cleaned_data['update'])
                employee.rank = rank
                employee.save()
                return redirect('home')

            if stat == 5:
                balance = float(form.cleaned_data['update'])
                employee.balance = balance
                employee.save()
                return redirect('home')

    return render(request, 'all_employees/update_employee.html',{'form': form, 'stat': stat})