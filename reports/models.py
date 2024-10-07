from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from payments.models import PaymentHistory
from expenses.models import Expense

def income_expense_report(request):
    # Calculating total income from PaymentHistory
    total_income = PaymentHistory.objects.all().aggregate(total=Sum('amount_paid'))['total'] or 0

    # Calculating total expenses from Expense model
    total_expenses = Expense.objects.all().aggregate(total=Sum('amount'))['total'] or 0

    # Generating context for the report
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_balance': total_income - total_expenses,
        'report_generated_at': timezone.now()
    }
    return render(request, 'reports/income_expense_report.html', context)
