from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_type', 'amount', 'description', 'employee', 'project']
