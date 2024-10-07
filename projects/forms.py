from django import forms
from .models import Project, Assignment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 
            'description', 
            'start_date', 
            'end_date', 
            'status', 
            'manager', 
            'budget', 
            'client_name'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['employee', 'project', 'role', 'assigned_date', 'end_date', 'status']
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
