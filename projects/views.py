from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project, User
# Create your views here.


def project_list(request):

     return render(request, 'projects/index.html')

def all_projects(request):

     # query the database to return all project objects
     projects = Project.objects.all()
     return render(request, 'projects/all_projects.html', {'projects' : projects})


def project_detail(request, pk):
     
     project = Project.objects.get(pk=pk)
     return render(request,'projects/detail.html', {'project' : project} )

def dashboard(request):
    
    return render(request, 'projects/dashboard.html', {'User' : User})