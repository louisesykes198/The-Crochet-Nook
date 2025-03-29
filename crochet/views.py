#from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
#def index(request):
    #return HttpResponse("Welcome to my Crochet Nook")
#from django.shortcuts import render
#from .models import Project  # Ensure your Project model is imported

#def home(request):
    #projects = Project.objects.all()  # Get all projects from the database
    #return render(request, 'crochet/project_list.html', {'projects': projects})
# crochet/views.py
#from django.shortcuts import render, redirect
#from .models import Project  # Assuming you have a Project model
#from .forms import ProjectForm  # Assuming you have a ProjectForm (optional if using forms)

#def home(request):
    # A simple view for the home page, displaying all projects
    #projects = Project.objects.all()  # Query all projects from the database
    #return render(request, 'project_list.html', {'projects': projects})

#def add_project(request):
    #if request.method == 'POST':
        #form = ProjectForm(request.POST)
        #if form.is_valid():
            #form.save()  # Save the new project to the database
            #return redirect('home')  # Redirect to the home page after saving
    #else:
        #form = ProjectForm()  # Display an empty form for GET requests

    #return render(request, 'add_project.html', {'form': form})

# Optionally, you can have other views such as project details, edit, delete, etc.
# views.py

#from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
#from .models import Project

# Other views go here...

#def edit_project(request, item_id):
    # Fetch the project to edit, or return a 404 if it doesn't exist
    #project = get_object_or_404(Project, pk=item_id)

    #if request.method == 'POST':
        # Get the updated data from the form
        #name = request.POST.get('name')
        #description = request.POST.get('description')

        #if name and description:
            # Update the project fields
            #project.name = name
            #project.description = description
            #project.save()

            #return redirect('home')  # Redirect to the home page after saving the changes
        #else:
            #return HttpResponse('Invalid data, please fill all fields', status=400)

    # For GET requests, pre-fill the form with the current project data
    #return render(request, 'edit_project.html', {'project': project})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm  # assuming you have a ProjectForm

# Home view - Displays the list of projects
def home(request):
    projects = Project.objects.all()  # Fetch all the projects
    return render(request, 'project_list.html', {'projects': projects})

# Add Project - Displays a form to add a new project
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new project
            return redirect('home')  # Redirect to home page after adding the project
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})

# Edit Project - Displays a form to edit an existing project
def edit_project(request, item_id):
    project = get_object_or_404(Project, pk=item_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()  # Save the edited project
            return redirect('home')  # Redirect to home page after editing the project
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

# Delete Project - Deletes an existing project
def delete_project(request, item_id):
    project = get_object_or_404(Project, pk=item_id)

    if request.method == 'POST':
        project.delete()  # Delete the project
        return redirect('home')  # Redirect to home page after deleting the project

    return render(request, 'delete_project.html', {'project': project})

def project_list(request):
    # Fetch all projects from the database
    projects = Project.objects.all()

    if request.method == 'POST':
        item_id = request.POST.get('delete')  # Get the ID of the project to delete
        if item_id:
            project = get_object_or_404(Project, pk=item_id)
            project.delete()  # Delete the project
            return redirect('home')  # Redirect back to the home page after deleting

    # Render the project list template and pass the 'projects' to it
    return render(request, 'project_list.html', {'projects': projects})




