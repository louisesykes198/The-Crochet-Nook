from django.db import models
from django.contrib.auth.models import User

class CrochetProject(models.Model):
    # Define possible difficulty levels
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'
    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]
    
    # Project fields
    name = models.CharField(max_length=200)  # Name of the project
    yarn_type = models.CharField(max_length=100)  # Type of yarn used
    difficulty_level = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default=MEDIUM,
    )
    estimated_time = models.CharField(max_length=100, blank=True)  # Estimated time to finish (optional)
    notes = models.TextField(blank=True)  # Notes or description of the project
    date_started = models.DateField()  # When the project started
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # Upload project image (optional)
    pattern_file = models.FileField(upload_to='patterns/', blank=True, null=True)  # File for the pattern (optional)
    status = models.CharField(
        max_length=20,
        default='In Progress',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link project to the user who created it

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_started']










