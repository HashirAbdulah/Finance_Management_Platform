from django import forms

from employees.models import CustomUser
from expenses.models import Expense
from projects.models import Project
from .models import Report

class ReportForm(forms.ModelForm):
     class Meta:
        model = Report
        fields = ['title', 'content', 'project', 'employee', 'expense']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['project'].queryset = Project.objects.all()
            self.fields['employee'].queryset = CustomUser.objects.filter(role='employee')
            self.fields['expense'].queryset = Expense.objects.all()