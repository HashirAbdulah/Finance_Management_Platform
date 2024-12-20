from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'address', 'skills', 'is_staff', 'is_active']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'role', 'email', 'phone_number', 'address']
