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
from django.contrib import admin
from django.contrib.auth import views as auth_views  # Import for login/logout
from django.urls import path
from crochet import views  # Import views from the 'crochet' app
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', views.register, name='register'),  # Ensure 'register' is in views
    path('login/', views.user_login, name='login'),  # Custom login view here
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout view
    
    # Login URL for Django's default view
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    # Home & Project List (Login required for project list)
    path('', views.home, name='home'),  # Home page
    path('projects/', login_required(views.project_list), name='project_list'),  # Apply login_required

    # Project Management
    path('add_project/', login_required(views.add_project), name='add_project'),  # Add project with login
    path('edit/<int:project_id>/', login_required(views.edit_project), name='edit_project'),  # Edit project with login
    path('delete/<int:project_id>/', login_required(views.delete_project), name='delete_project'),  # Delete project with login

    # Project Detail & Update
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/update/', views.update_project, name='update_project'),

    # Category Filtering
    path('category/<str:category>/', views.category_view, name='category_view'),

    # Landing Page (or any default home)
    path('landing/', views.landing_page, name='landing'),  # You can make landing page specific
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




