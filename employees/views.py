from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm

# View to list all employees
def employee_list(request):
    employees = CustomUser.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# View to create a new employee
def employee_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = CustomUserForm()
    return render(request, 'employees/employee_form.html', {'form': form})

# View to update an employee
def employee_update(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = CustomUserForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

# View to delete an employee
def employee_delete(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
