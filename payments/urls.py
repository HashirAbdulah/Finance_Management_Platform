from django.urls import path
from . import views

urlpatterns = [
    # Payment Overview
    path('', views.payment_overview, name='payment_overview'),
    
    # Salary Management
    path('salaries/', views.salary_list, name='salary_list'),
    path('salaries/<int:pk>/edit/', views.salary_edit, name='salary_edit'),  # Consolidated to salary_edit
    path('salaries/<int:pk>/edit/', views.salary_update, name='salary_update'),
    path('salaries/<int:pk>/delete/', views.salary_delete, name='salary_delete'),
    path('salaries/add/', views.salary_create, name='salary_create'),

    # Payment Management
    path('payments/<int:pk>/edit/', views.payment_edit, name='payment_edit'),
    path('payments/delete/<int:pk>/', views.payment_delete, name='payment_delete'),
    
    # Give Pay functionality
    path('give-pay/<int:salary_id>/', views.give_pay, name='give_pay'), 

    # Payment History
    path('payment-history/', views.payment_history_list, name='payment_history_list'),
    path('payment-history/add/', views.payment_history_create, name='payment_history_create'),
]

