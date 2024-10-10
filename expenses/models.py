from django.db import models
from employees.models import CustomUser
from projects.models import Project

class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = [
        ('travel', 'Travel'),
        ('utilities', 'Utilities'),
        ('supplies', 'Supplies'),
        ('miscellaneous', 'Miscellaneous'),
    ]

    expense_type = models.CharField(max_length=20, choices=EXPENSE_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.expense_type.capitalize()} - ${self.amount} on {self.date}"