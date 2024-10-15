from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('add/', views.report_create, name='report_create'),
    path('export/', views.export_reports_csv, name='export_reports_csv'),
    path('income-expense/', views.income_expense_report, name='income_expense_report'),
    path('add/', views.report_create, name='report_create'),
    path('edit/<int:pk>/', views.report_edit, name='report_edit'),
    path('delete/<int:pk>/', views.report_delete, name='report_delete'),
]

