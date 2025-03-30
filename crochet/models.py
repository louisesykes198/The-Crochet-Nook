from django.db import models

# The Project model is to store information about crochet projects

class Project(models.Model):
    # This section gives a list of project categories to provide users with options 
    CATEGORY_CHOICES = [
        ('Blankets', 'Blankets'),
        ('Cardigans', 'Cardigans'),
        ('Amigurumi', 'Amigurumi'),
        ('Scarves', 'Scarves'),
        ('Hats', 'Hats'),
    ]
    # This code provides a list of information that you need to include when adding a project to the site
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    skill_level = models.CharField(max_length=100)
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Blankets')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # Add an image field

    # This string is for the model to retuen the name of the project
    def __str__(self):
        return self.name
