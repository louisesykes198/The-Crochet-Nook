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
from .models import Project, Comment, Like
from .forms import ProjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Home view
def home(request):
    return render(request, 'home.html')

# Project List view
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# Category view (projects based on category)
def category_view(request, category):
    projects = Project.objects.filter(category=category)
    return render(request, 'category.html', {"category": category, "projects": projects})

# Add Project view
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

# Edit Project view
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()  # Save the updated project
            return redirect('project_list')  # Redirect to the project list page
        else:
            # Add an error message if the form is invalid
            print(form.errors)  # Check the form errors in the terminal or log
    else:
        form = ProjectForm(instance=project)  # Initialize the form with the project instance

    return render(request, 'edit_project.html', {'form': form, 'project': project})

# Delete Project view
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})

# User Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# User Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Project Detail view (likes and comments handling)
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Handle the form for adding likes and comments
    if request.method == 'POST':
        if 'like' in request.POST:
            # Prevent user from liking the same project more than once
            if not Like.objects.filter(project=project, user=request.user).exists():
                Like.objects.create(project=project, user=request.user)
            else:
                messages.error(request, "You have already liked this project.")
        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment_text')
            if comment_text:  # Ensure the comment text is not empty
                Comment.objects.create(project=project, user=request.user, comment=comment_text)
            else:
                messages.error(request, "Comment cannot be empty.")

    # Retrieve likes and comments for the project
    comments = Comment.objects.filter(project=project)
    likes = Like.objects.filter(project=project).count()

    return render(request, 'project_detail.html', {
        'project': project,
        'comments': comments,
        'likes': likes
    })

# Update Project view
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'update_project.html', {'form': form, 'project': project})


