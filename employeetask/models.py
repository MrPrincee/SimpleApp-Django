from django.db import models


class EmployeeTask(models.Model):
    header = models.CharField(max_length=100, null=False)
    task = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, default="Active")
    worker = models.IntegerField(default=0)

    def __str__(self):
        return self.header
