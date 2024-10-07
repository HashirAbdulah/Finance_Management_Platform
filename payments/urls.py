from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_overview, name='payment_overview'),
    path('salaries/', views.salary_list, name='salary_list'),
    path('salaries/add/', views.salary_create, name='salary_create'),
    path('salaries/<int:pk>/edit/', views.salary_update, name='salary_update'),
    path('salaries/<int:pk>/delete/', views.salary_delete, name='salary_delete'),
    path('payment-history/', views.payment_history_list, name='payment_history_list'),
    path('payment-history/add/', views.payment_history_create, name='payment_history_create'),
]
