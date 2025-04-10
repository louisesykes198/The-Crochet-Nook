from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Blankets', 'Blankets'),
        ('Cardigans', 'Cardigans'),
        ('Amigurumi', 'Amigurumi'),
        ('Scarves', 'Scarves'),
        ('Hats', 'Hats'),
        ('Dishcloths', 'Dishcloths'),
    ]

    SKILL_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # 🧵 For clean URLs

    description = models.TextField()
    skill_level = models.CharField(max_length=50, choices=SKILL_LEVEL_CHOICES, default='Beginner')
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True, default='')

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    image = models.ImageField(upload_to='project_images/')  # 🌸 Optional — paste in an image URL
    pattern = models.TextField(blank=True, null=True)  # 🧶 Crochet pattern as text instead of upload

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

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








