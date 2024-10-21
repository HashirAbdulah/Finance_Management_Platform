from django.db import models
from employees.models import CustomUser
from projects.models import Project


class PaymentType(models.Model):
    PAYMENT_CHOICES = [
        ('monthly', 'Monthly'),
        ('hourly', 'Hourly'),
    ]
    payment_frequency = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.payment_frequency.capitalize()} Payment"


class Salary(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'employee'})
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.username} - {self.payment_type} - ${self.amount}"
    

# This will change in add payments history for payment type field
class PaymentHistory(models.Model):
    PAYMENT_CHOICES = [
        ('monthly', 'Monthly'),
        ('hourly', 'Hourly'),
    ]
    
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'employee'})
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    payment_date = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.amount_paid} on {self.payment_date}"
