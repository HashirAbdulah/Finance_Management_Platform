from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm, EmployeeForm
from django.db.models import Q

# View to list all employees
def employee_list(request):
    query = request.GET.get('q', '')
    if query:
        employees = CustomUser.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
        )
    else:
        employees = CustomUser.objects.all()

    context = {'employees': employees, 'query': query}
    return render(request, 'employees/employee_list.html', context)


# View to create a new employee
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list after saving
    else:
        form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {'form': form})


# View to update an employee
def employee_update(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list after updating
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/employee_form.html', {'form': form})
# View to delete an employee
def employee_delete(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
