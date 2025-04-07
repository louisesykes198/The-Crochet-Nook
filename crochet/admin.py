from django.contrib import admin
from .models import Project, Comment, Like, Pattern

# Inline admin options for the Comment and Like models
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
   

class LikeInline(admin.TabularInline):
    model = Like
    extra = 1

# Project model admin configuration
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'skill_level')  # Removed 'created_at'
    list_filter = ('category', 'skill_level')
    search_fields = ('name', 'description')
    ordering = ('name',)  # Changed from '-created_at' to another valid field
    inlines = [CommentInline, LikeInline]
    
# Comment model admin configuration
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('project', 'user')  # Removed 'created_at'
    search_fields = ('comment',)
    
# Like model admin configuration
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('project', 'user')

# Pattern model admin configuration
@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')  # Still good to go


