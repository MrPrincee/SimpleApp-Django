from django import forms
from employeemanager.models import Employee

from django import forms


class AddEmployee(forms.Form):
    CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    name = forms.CharField(max_length=100, label='Name')
    surname = forms.CharField(max_length=100, label='Surname')
    salary = forms.FloatField(label="Salary")
    rank = forms.ChoiceField(choices=CHOICES, label="Rank", required=True)
    balance = forms.FloatField(label="Balance", required=False)


class ChooseEmployeeStat(forms.Form):
    CHOICES = (
        (1, 'name'),
        (2, 'surname'),
        (3, 'salary'),
        (4, 'rank'),
        (5, 'balance')
    )

    stat = forms.ChoiceField(choices=CHOICES, label='Stat', required=True)


class ChooseEmployee(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label="Select Employee")


class UpdateEmployee(forms.Form):
    update = forms.CharField(max_length=100,required=True)
