from django import forms


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
    rank = forms.ChoiceField(choices=CHOICES, label="Rank",required=True)
    balance = forms.FloatField(label="Balance", required=False)
