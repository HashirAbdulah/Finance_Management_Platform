import csv
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from employees.models import CustomUser
from payments.models import PaymentHistory
from expenses.models import Expense
from django.utils import timezone
from django.db.models import Sum
from projects.models import Project
from reports.models import Report
from .forms import ReportForm
from django.views.decorators.csrf import csrf_exempt

def income_expense_report(request):
    # Fetch the start and end date from the query parameters (GET request)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Initialize variables for income and expenses
    total_income = 0
    total_expenses = 0

    # Check if both dates are provided, then filter based on date range
    if start_date and end_date:
        total_income = PaymentHistory.objects.filter(payment_date__range=[start_date, end_date]).aggregate(total=Sum('amount_paid'))['total'] or 0
        total_expenses = Expense.objects.filter(date__range=[start_date, end_date]).aggregate(total=Sum('amount'))['total'] or 0
    else:
        # No date filtering; return all data
        total_income = PaymentHistory.objects.aggregate(total=Sum('amount_paid'))['total'] or 0
        total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0

    # Calculate the net balance
    net_balance = total_income - total_expenses

    # Prepare the context to pass to the template
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_balance': net_balance,
        'report_generated_at': timezone.now(),
    }

    return render(request, 'reports/income_expense_report.html', context)

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()

    employees = CustomUser.objects.filter(role='employee')
    projects = Project.objects.all()
    expenses = Expense.objects.all()

    return render(request, 'reports/report_form.html', {
        'form': form,
        'employees': employees,
        'projects': projects,
        'expenses': expenses,
    })

def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm(instance=report)

    employees = CustomUser.objects.filter(role='employee')
    projects = Project.objects.all()
    expenses = Expense.objects.all()

    return render(request, 'reports/report_form.html', {
        'form': form,
        'employees': employees,
        'projects': projects,
        'expenses': expenses,
        'report': report
    })

@csrf_exempt
def report_update(request, pk):
    if request.method == 'POST':
        report = get_object_or_404(Report, pk=pk)
        data = json.loads(request.body)
        title = data.get('title', '')

        if title:
            report.title = title
            report.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid title'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

# Delete an existing report
def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})


def report_list(request):
    reports = Report.objects.all()  # Fetch all reports from the database
    return render(request, 'reports/report_list.html', {'reports': reports})


def export_reports_csv(request):
    reports = Report.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reports.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Created By', 'Date Created', 'Content'])

    for report in reports:
        writer.writerow([report.title, report.created_by, report.date_created, report.content])

    return response

