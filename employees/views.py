from django.shortcuts import render
from .models import CustomUser

def employee_list(request):
    employees = CustomUser.objects.filter(role='employee')
    return render(request, 'employees/employee_list.html', {'employees': employees})
