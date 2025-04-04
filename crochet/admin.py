from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Comment, Like, Pattern

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Pattern)