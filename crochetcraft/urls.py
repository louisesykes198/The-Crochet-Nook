from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from crochet import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Home & Project List (Login required for project list)
    path('', views.home, name='home'),
    path('projects/', login_required(views.project_list), name='project_list'),  # Login required

    # Project Management
    path('add_project/', login_required(views.add_project), name='add_project'),  # Add project with login
    path('edit/<int:project_id>/', login_required(views.edit_project), name='edit_project'),  # Edit project with login
    path('delete/<int:project_id>/', login_required(views.delete_project), name='delete_project'),  # Delete project with login

    # Project Detail & Update
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('project/<slug:slug>/update/', login_required(views.update_project), name='update_project'),


    # Category Filtering
    path('category/<str:category>/', views.category_view, name='category_view'),
]
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








