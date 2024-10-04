from django.db import models
from employees.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'role': 'employee'})
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.role} - {self.project.name}"
