from django.db import models
from employees.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on hold', 'On Hold'),
    ], default='active')
    manager = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_projects')
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    assigned_date = models.DateField(null=True, blank=True)  # Setting null=True, blank=True to avoid nullable issues
    end_date = models.DateField(null=True, blank=True)       # Setting null=True, blank=True to avoid nullable issues
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('completed', 'Completed')
    ], default='active')

    def __str__(self):
        return f"{self.employee.username if self.employee else 'Unassigned'} assigned to {self.project.name}"
