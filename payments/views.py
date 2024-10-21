from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import PaymentType, Salary, CustomUser, Project, PaymentHistory
from .forms import SalaryForm, PaymentHistoryForm
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

def salary_edit(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    payment_types = PaymentType.objects.all()

    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm(instance=salary)
    
    # Pass 'editing' as True and omit the 'employees' context since the dropdown should be hidden
    return render(request, 'payments/salary_form.html', {
        'form': form,
        'payment_types': payment_types,
        'editing': True,  # Indicate that this is an edit operation
        'selected_payment_type': salary.payment_type.id
    })

# View to edit payment history inline
def payment_edit(request, pk):
    payment = get_object_or_404(PaymentHistory, pk=pk)
    if request.method == 'POST':
        form = PaymentHistoryForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        data = {
            'amount_paid': payment.amount_paid,
            'status': payment.status,
        }
        return JsonResponse(data)

# View to delete payment history
def payment_delete(request, pk):
    payment = get_object_or_404(PaymentHistory, pk=pk)
    
    if request.method == 'POST':
        # Delete the payment if the request is a POST
        payment.delete()
        # Redirect to the payment overview or any other appropriate page
        return redirect('payment_overview')
    
    # If the request is a GET, render the confirmation template
    return render(request, 'payments/payment_confirm_delete.html', {'payment': payment})

# View to list all salaries
def salary_list(request):
    salaries = Salary.objects.all()
    for salary in salaries:
        # Calculate the total salary (amount + commission)
        salary.total_with_commission = salary.amount + (salary.amount * salary.commission / 100)
    return render(request, 'payments/salary_list.html', {'salaries': salaries})


# View to add a new salary
def salary_create(request):
    employees = CustomUser.objects.filter(role='employee')
    payment_types = PaymentType.objects.all()
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_overview')
    else:
        form = SalaryForm()
    return render(request, 'payments/salary_form.html', {
        'form': form,
        'employees': employees,
        'payment_types': payment_types,
        'editing': False  # Indicate that this is not an edit operation
    })


# View to update a salary
def salary_update(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    payment_types = PaymentType.objects.all()

    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm(instance=salary)
    
    # Pass the context indicating that this is an edit form
    context = {
        'form': form,
        'payment_types': payment_types,
        'editing': True,  # Indicate that this is the edit form
        'form_title': 'Edit Salary',
    }
    return render(request, 'payments/salary_form.html', context)


# View to delete a salary

@csrf_exempt
def salary_delete(request, pk):
    salary = get_object_or_404(Salary, pk=pk)

    if request.method == 'POST':
        salary.delete()
        # Redirect to the salary list page after deletion
        return redirect('payment_overview')

    # Render the delete confirmation template if the request is a GET
    return render(request, 'payments/salary_confirm_delete.html', {'salary': salary})

def give_pay(request, salary_id):
    # Get the salary record
    salary = get_object_or_404(Salary, id=salary_id)
    
    # Calculate the total amount (salary + commission)
    total_amount = salary.amount + (salary.amount * salary.commission / 100)
    
    # Create a new payment history entry with the updated total amount
    PaymentHistory.objects.create(
        employee=salary.employee,
        amount_paid=total_amount,  # Use the calculated total amount
        payment_date=timezone.now(),
        payment_type='monthly',
        status='Paid',
        project=None 
    )
    
    # Redirect back to the payment overview page
    return redirect('payment_overview')



# View to list all payment history records
def payment_history_list(request):
    payment_histories = PaymentHistory.objects.all()
    return render(request, 'payments/payment_history_list.html', {'payment_histories': payment_histories})


# View to create a new payment history record
def payment_history_create(request):
    if request.method == 'POST':
        form = PaymentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_history_list')
    else:
        form = PaymentHistoryForm()
    return render(request, 'payments/payment_history_form.html', {'form': form})


# View for the payment overview
def payment_overview(request):
    salaries = Salary.objects.all()  # Ensure all salary records are fetched
    for salary in salaries:
        salary.total_amount = salary.amount + (salary.amount * salary.commission / 100)
    payment_history = PaymentHistory.objects.all()  # Ensure all payment history records are fetched

    return render(request, 'payments/payment_overview.html', {
        'salaries': salaries,
        'payment_history': payment_history,  # Pass payment history to the template
    })

# View to handle payment history form (both create and edit)
def payment_history_form(request, pk=None):
    if pk:
        payment_history = get_object_or_404(PaymentHistory, pk=pk)
    else:
        payment_history = PaymentHistory()

    if request.method == 'POST':
        form = PaymentHistoryForm(request.POST, instance=payment_history)
        if form.is_valid():
            form.save()
            return redirect('payment_history_list')
    else:
        form = PaymentHistoryForm(instance=payment_history)
    
    employees = CustomUser.objects.filter(role='employee')
    projects = Project.objects.all()

    return render(request, 'payments/payment_history_form.html', {'form': form, 'employees': employees, 'projects': projects})


