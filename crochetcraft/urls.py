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
from django.contrib.auth import views as auth_views  # ✅ Import this
from django.urls import path
from crochet import views  # Imports views from the 'crochet' app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  

    # Home & Project List
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),

    # Project Management
    path('add_project/', views.add_project, name='add_project'),
    path('edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),

    # Project Detail & Update (Fixed parameter consistency)
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/update/', views.update_project, name='update_project'),

    # Category Filtering
    path('category/<str:category_name>/', views.category_view, name='category_view'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
