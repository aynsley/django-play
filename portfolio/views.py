from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    # Fetch all the Projects from the db, that is, all the objects of Python class Project
    proj_objs = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': proj_objs})
