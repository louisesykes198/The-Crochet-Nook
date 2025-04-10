from django.contrib import admin
from .models import CrochetProject

@admin.register(CrochetProject)
class CrochetProjectAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = ('id', 'name', 'user', 'difficulty_level', 'status', 'date_started', 'image')
    
    # Make the 'name' and 'user' fields clickable, linking to their detailed page
    list_display_links = ('name', 'user')

    # Search functionality: search by project name, yarn type, and user
    search_fields = ['name', 'yarn_type', 'user__username']
    
    # Filter functionality: filter by difficulty level, status, and user
    list_filter = ['difficulty_level', 'status', 'user']
    
    # Add ordering to the list view (e.g., by the date started in descending order)
    ordering = ['-date_started']

    # Additional options for form fields or the way data is displayed in the admin panel
    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'difficulty_level', 'yarn_type', 'estimated_time', 'notes')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('image', 'pattern_file', 'status', 'date_started')
        }),
    )

    # Optional: You can customize the list of fields and form behavior
    # to suit your needs, including adding validation, etc.




