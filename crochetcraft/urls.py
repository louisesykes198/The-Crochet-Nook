"""
URL configuration for crochetcraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
#from crochet import views as index_views

#urlpatterns = [
    #path('', index_views.index, name='index'),
    #path('admin/', admin.site.urls),
    #]
#from django.urls import path
#from crochet import views

#urlpatterns = [
    #path('', views.home, name='home'),  # Home page
    #path('add/', views.add_project, name='add_project'),  # Add project page
    #path('edit/<int:project_id>/', views.edit_project, name='edit_project'),  # Edit project page
    #path('delete/<int:project_id>/', views.delete_project, name='delete_project'),  # Delete project page
#]
from django.contrib import admin
from django.urls import path
from crochet import views  # Imports views from the 'crochet' app

# This code will run the urls for all the websites pages so you can add, edit, delete and view the projects
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:item_id>/', views.edit_project, name='edit_project'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('projects/', views.project_list, name='project_list'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
]

