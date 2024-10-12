from django.shortcuts import render, get_object_or_404, redirect
from .models import Salary
from .models import PaymentHistory
from .forms import SalaryForm, PaymentHistoryForm

# View to list all salaries
def salary_list(request):
    salaries = Salary.objects.all()
    return render(request, 'payments/salary_list.html', {'salaries': salaries})

# View to add a new salary
def salary_create(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm()
    return render(request, 'payments/salary_form.html', {'form': form})

# View to update a salary
def salary_update(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm(instance=salary)
    return render(request, 'payments/salary_form.html', {'form': form})

# View to delete a salary
def salary_delete(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary_list')
    return render(request, 'payments/salary_confirm_delete.html', {'salary': salary})


def payment_history_list(request):
    payment_histories = PaymentHistory.objects.all()
    return render(request, 'payments/payment_history_list.html', {'payment_histories': payment_histories})

def payment_history_list(request):
    payment_histories = PaymentHistory.objects.all()
    return render(request, 'payments/payment_history_list.html', {'payment_histories': payment_histories})


def payment_history_create(request):
    if request.method == 'POST':
        form = PaymentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_history_list')
    else:
        form = PaymentHistoryForm()
    return render(request, 'payments/payment_history_form.html', {'form': form})

def payment_overview(request):
    salaries = Salary.objects.all()
    payment_histories = PaymentHistory.objects.all()
    context = {
        'salaries': salaries,
        'payment_histories': payment_histories,
    }
    return render(request, 'payments/payment_overview.html', context)
