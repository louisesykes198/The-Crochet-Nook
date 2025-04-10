from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CrochetProject
from .forms import CrochetProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin

# List view to show all crochet projects
class CrochetProjectListView(LoginRequiredMixin, ListView):
    model = CrochetProject
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return CrochetProject.objects.filter(user=self.request.user).order_by('-date_started')

# Detail view to show the details of a single project
class CrochetProjectDetailView(LoginRequiredMixin, DetailView):
    model = CrochetProject
    template_name = 'project_detail.html'
    context_object_name = 'project'

# Create view to add a new crochet project
class CrochetProjectCreateView(LoginRequiredMixin, CreateView):
    model = CrochetProject
    template_name = 'project_form.html'
    form_class = CrochetProjectForm
    success_url = reverse_lazy('project_list')  # Redirect to project list after creation

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the project
        return super().form_valid(form)

# Update view to edit an existing project
class CrochetProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = CrochetProject
    template_name = 'project_form.html'
    form_class = CrochetProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})  # Redirect to project detail after edit

# Delete view to delete a project
class CrochetProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = CrochetProject
    template_name = 'project_confirm_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project_list')  # Redirect to project list after deletion




