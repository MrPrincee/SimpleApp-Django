from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    salary = models.FloatField()
    rank = models.IntegerField()
    balance = models.FloatField(default=0)
