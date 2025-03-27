# crochet/forms.py
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'skill_level', 'materials_needed', 'notes']  # List the fields you want in the form