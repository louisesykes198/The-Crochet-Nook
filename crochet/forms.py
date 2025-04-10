from django import forms
from .models import CrochetProject

class CrochetProjectForm(forms.ModelForm):
    class Meta:
        model = CrochetProject
        fields = ['name', 'yarn_type', 'difficulty_level', 'estimated_time', 'notes', 'date_started', 'image', 'pattern_file', 'status']
        widgets = {
            'date_started': forms.SelectDateWidget(years=range(2020, 2031)),  # Customizing date input widget
        }









        
