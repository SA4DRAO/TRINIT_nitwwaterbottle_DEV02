from django.shortcuts import redirect, render
from django.http import HttpResponse
from django import forms


from projects.forms import ProjectCreationForm

from projects.models import Project
from django.contrib.auth.models import User

# Create your views here.
def index_view(request):
    project_list = Project.objects.all()

    context = {
        'projects' : project_list
    }
    
    return render(request, 'projects/home.html', context)


def add_project(request):
        
    form = ProjectCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.team_leader = request.user
            instance.save()

            return redirect('projects:home')
    
    context = {
        'form':form
    }

    return render(request, 'projects/add_project.html', context)