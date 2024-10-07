from django.urls import path
from . import views

urlpatterns = [
    # Project URLs
    path('', views.project_list, name='project_list'),  # List all projects
    path('create/', views.project_create, name='project_create'),  # Create a new project
    path('<int:pk>/update/', views.project_update, name='project_update'),  # Update an existing project
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),  # Delete a project
    
    # Assignment URLs
    path('assignments/', views.assignment_list, name='assignment_list'),  # List all assignments
    path('assignments/create/', views.assignment_create, name='assignment_create'),  # Create a new assignment
    path('assignments/<int:pk>/update/', views.assignment_update, name='assignment_update'),  # Update an assignment
    path('assignments/<int:pk>/delete/', views.assignment_delete, name='assignment_delete'),  # Delete an assignment
]
