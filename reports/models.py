from django.db import models
from django.contrib.auth.models import User
from employees.models import CustomUser
from expenses.models import Expense
from projects.models import Project

class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    expense = models.ForeignKey(Expense, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title
