from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    # Predefined category choices
    CATEGORY_CHOICES = [
        ('Blankets', 'Blankets'),
        ('Cardigans', 'Cardigans'),
        ('Amigurumi', 'Amigurumi'),
        ('Scarves', 'Scarves'),
        ('Hats', 'Hats'),
        ('Dishcloths', 'Dishcloths'),
    ]

    # Skill levels for projects
    SKILL_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    # Project details
    name = models.CharField(max_length=200)
    description = models.TextField()
    skill_level = models.CharField(max_length=50, choices=SKILL_LEVEL_CHOICES, default='Beginner')
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True, default='')  # Optional notes field
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='projects/images/', blank=True)  # Optional image field
    pattern = models.FileField(upload_to='projects/patterns/', blank=True)  # Optional pattern field
    #updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Projects"  # Clean display in Django Admin

    def __str__(self):
        return self.name


# Comment model to store user comments on projects
class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    
    

    def __str__(self):
        return f"Comment by {self.user.username} on {self.project.name}"


# Like model to track project likes
class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user')  # Prevents duplicate likes

    def __str__(self):
        return f"Like by {self.user.username} on {self.project.name}"


class Pattern(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def short_description(self):
        return self.description[:50] + "..." if len(self.description) > 50 else self.description








