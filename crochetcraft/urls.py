from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrochetProjectListView.as_view(), name='project_list'),  # Home or project list page
    path('project/<int:pk>/', views.CrochetProjectDetailView.as_view(), name='project_detail'),  # Detail page for a project
    path('add_project/', views.CrochetProjectCreateView.as_view(), name='add_project'),  # Create a new project
    path('project/<int:pk>/edit/', views.CrochetProjectUpdateView.as_view(), name='project_update'),  # Edit an existing project
    path('project/<int:pk>/delete/', views.CrochetProjectDeleteView.as_view(), name='project_delete'),  # Delete a project
]









