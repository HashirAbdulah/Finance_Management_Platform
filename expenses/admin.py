from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'amount', 'date', 'employee', 'project')
    search_fields = ('expense_type', 'description')
    list_filter = ('expense_type', 'date')
