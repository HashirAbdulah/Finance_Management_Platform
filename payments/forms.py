from django import forms
from .models import Salary, PaymentHistory

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['employee', 'project', 'payment_type', 'amount', 'commission']

class PaymentHistoryForm(forms.ModelForm):
    class Meta:
        model = PaymentHistory
        fields = ['employee', 'project', 'payment_type', 'amount_paid', 'status']
