from http.client import HTTPResponse
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from projects.models import Project, User
from django.contrib.auth import login 
from django.urls import reverse 
from projects.forms import CustomUserCreationForm
import markdown
# Create your views here.

md = markdown.Markdown()

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
    users = User.objects.all()
    
    return render(request, 'projects/dashboard.html', {'users' : users})

def register(request):
     if request.method=="GET":
          return render(
               request, "registration/register.html", 
               {"form": CustomUserCreationForm}
          )
     elif request.method == "POST":
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
               user = form.save()
               login(request,user)
               return redirect(reverse("dashboard"))     