from django.shortcuts import render
from projects.models import Project
from employees.models import CustomUser
from expenses.models import Expense
import json

def dashboard_overview(request):
    # Fetch data for the dashboard
    total_projects = Project.objects.count()
    total_employees = CustomUser.objects.count()
    total_expenses = Expense.objects.all()
    expense_total = sum(expense.amount for expense in total_expenses)

    # Prepare data for JavaScript
    projects = Project.objects.all()
    project_names = [project.name for project in projects]
    project_expenses = [getattr(project, 'expenses_amount', 0) for project in projects]

    # Pass data to the template
    context = {
        'total_projects': total_projects,
        'total_employees': total_employees,
        'expense_total': expense_total,
        'projects_data': json.dumps({
            'labels': project_names,
            'expenses': project_expenses,
        }),
    }
    return render(request, 'dashboard/dashboard_overview.html', context)



def dashboard_view(request):
    projects = Project.objects.all()
    
    # Prepare the data in a JSON format
    project_data = {
        'labels': [project.name for project in projects],
        'expenses': [project.expenses_amount if project.expenses_amount else 0 for project in projects],
    }
    project_data_json = json.dumps(project_data)

    return render(request, 'dashboard/dashboard.html', {'project_data_json': project_data_json})