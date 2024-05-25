from django import forms


class AddTaskForm(forms.Form):
    header = forms.CharField(label="Header",max_length=100)
    task = forms.CharField(label='Task')
