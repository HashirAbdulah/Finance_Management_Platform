from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from employees.models import CustomUser
from projects.models import Project

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    # Fetch all employees and projects to pass to the form
    employees = CustomUser.objects.all()
    projects = Project.objects.all()

    return render(request, 'expenses/expense_form.html', {
        'form': form,
        'employees': employees,
        'projects': projects,
    })

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)

    employees = CustomUser.objects.all()
    projects = Project.objects.all()

    return render(request, 'expenses/expense_form.html', {
        'form': form,
        'employees': employees,
        'projects': projects,
    })


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})