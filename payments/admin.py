from django.contrib import admin
from .models import PaymentType, Salary

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('payment_frequency', 'description')
    search_fields = ('payment_frequency',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'payment_type', 'amount', 'commission')
    search_fields = ('employee__username', 'project__name', 'payment_type__payment_frequency')
