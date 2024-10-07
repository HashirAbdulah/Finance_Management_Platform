# projects/admin.py
from django.contrib import admin
from .models import Project, Assignment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'start_date', 'end_date')
    search_fields = ('name', 'client_name')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'role', 'assigned_date', 'end_date', 'status')
    search_fields = ('employee__username', 'project__name', 'role')
