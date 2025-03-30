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
from .forms import ProjectForm
from django.contrib.auth.forms import UserCreationForm



# Home view - This will display a welcome message or featured content
def home(request):
    # You can customize the homepage content here (for example, featured projects)
    return render(request, 'home.html')  # Ensure you have a 'home.html' template

# Project List View - This will display all the projects
def project_list(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'project_list.html', {'projects': projects})

# Category View - This will display projects filtered by category
def category_view(request, category_name):
    projects = Project.objects.filter(category=category_name)
    return render(request, 'category.html', {'category': category_name, 'projects': projects})

# Add Project - This will bring up a form to add a new project
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new project
            return redirect('project_list')  # Redirect back to the project list after adding a project
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})

# Edit Project - This will display a form to edit an existing project
def edit_project(request, item_id):
    project = get_object_or_404(Project, pk=item_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()  # Save the project
            return redirect('project_list')  # Redirect back to the project list after editing the project
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

# Delete Project - This will delete an existing project
def delete_project(request, item_id):
    project = get_object_or_404(Project, pk=item_id)

    if request.method == 'POST':
        project.delete()  # Delete the project
        return redirect('project_list')  # Redirect back to the project list after deleting the project
    return render(request, 'delete_project.html', {'project': project})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save new user
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})  # Render the register page




