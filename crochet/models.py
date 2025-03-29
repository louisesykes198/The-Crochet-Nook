from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    skill_level = models.CharField(max_length=100)
    materials_needed = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name