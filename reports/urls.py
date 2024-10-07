from django.urls import path
from . import views

urlpatterns = [
    path('income-expense/', views.income_expense_report, name='income_expense_report'),
    path('', views.reports_overview, name='reports_overview'),  # New URL pattern for /reports/

]

