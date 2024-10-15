# projects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Assignment
from .forms import ProjectForm, AssignmentForm
from expenses.models import Expense


def project_create_or_update(request, pk=None):
    # Fetch project if pk is provided, else create a new one
    project = get_object_or_404(Project, pk=pk) if pk else None

    if request.method == 'POST':
        # Initialize both forms with POST data
        form = ProjectForm(request.POST, instance=project)
        assignment_form = AssignmentForm(request.POST)

        # Check if both forms are valid
        if form.is_valid() and assignment_form.is_valid():
            # Save the project first
            new_project = form.save()

            # Save the assignment but don't commit yet
            new_assignment = assignment_form.save(commit=False)
            new_assignment.project = new_project  # Attach the project to the assignment
            new_assignment.save()  # Save the assignment

            # Redirect to project list after successful submission (auto-close the form)
            return redirect('project_list')
        else:
            print(form.errors, assignment_form.errors)  # Debugging: Check for validation errors
    else:
        # GET request: empty forms for new project or pre-filled forms for update
        form = ProjectForm(instance=project)
        assignment_form = AssignmentForm()

    return render(request, 'projects/project_form.html', {
        'form': form,
        'assignment_form': assignment_form,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    expenses = Expense.objects.filter(project=project)
    assignments = Assignment.objects.filter(project=project)

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'expenses': expenses,
        'assignments': assignments,
    })

# View to list all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

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
