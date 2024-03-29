"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from projects import views

urlpatterns = [
    path('projects/',views.all_projects, name = 'all_projects'),
    path('classprojects/',views.classroom_projects, name = 'classprojects'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('', views.dashboard, name = 'dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('project_<int:pk>', views.project_detail, name = 'project_detail'),
    path('class_<int:pk>', views.class_project_detail, name = 'class_project_detail'),
    path('register/', views.register, name = 'register'),

]
