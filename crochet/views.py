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
        print("FILES:", request.FILES)  # 👈 Add this
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            print("Image saved to:", project.image.url)  # 👈 Add this
            messages.success(request, "Project added successfully!")
            return redirect('project_list')
        else:
            print("Form errors:", form.errors)  # 👈 Add this
            messages.error(request, "There was an error with your form submission.")
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

# Edit Project view
def edit_project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")  # Add success message
            return redirect('project_list')
        else:
            messages.error(request, "There was an error with your form submission.")  # Add error message
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

# Delete Project view
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully!")  # Add success message
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})

# User Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")  # Add success message
            return redirect('home')
        else:
            messages.error(request, "There was an error with your registration.")  # Add error message
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# User Login view
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

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
                next_url = request.GET.get('next', 'home')  # Get the next parameter or default to 'home'
                messages.success(request, "Logged in successfully!")  # Add success message
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})  # Render login page with form

# Project Detail view (likes and comments handling)
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    # Handle likes and comments
    if request.method == 'POST':
        if 'like' in request.POST:
            if not Like.objects.filter(project=project, user=request.user).exists():
                Like.objects.create(project=project, user=request.user)
                messages.success(request, "You liked this project!")
            else:
                messages.error(request, "You have already liked this project.")
        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment_text')
            if comment_text:
                Comment.objects.create(project=project, user=request.user, comment=comment_text)
                messages.success(request, "Your comment was posted!")
            else:
                messages.error(request, "Comment cannot be empty.")

        return redirect('project_detail', slug=project.slug)

    context = {
        'project': project,
        'comments': project.comments.all(),
        'likes': project.likes.count(),
    }

    return render(request, 'project_detail.html', context)

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
            messages.success(request, "Project updated successfully!")  # Add success message
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'update_project.html', {'form': form, 'project': project})



