# projects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Assignment
from .forms import ProjectForm, AssignmentForm
from expenses.models import Expense

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    expenses = Expense.objects.filter(project=project)  # Fetch related expenses

    context = {
        'project': project,
        'expenses': expenses,  # Add expenses to context
    }
    return render(request, 'projects/project_detail.html', context)

# View to list all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

# View to create a new project
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

# View to update an existing project
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

# View to delete a project
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

# View to list all assignments
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'projects/assignment_list.html', {'assignments': assignments})

# View to create a new assignment
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'projects/assignment_form.html', {'form': form})

# View to update an assignment
def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'projects/assignment_form.html', {'form': form})

# View to delete an assignment
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'projects/assignment_confirm_delete.html', {'assignment': assignment})
