from django.shortcuts import render
from .models import *

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{'projects':projects})

def testimonies(request):
    testimonies = Testimonie.objects.all()
    return render(request, 'testimonies.html', {'testimonies':testimonies})
def contact(request):
    return render(request, 'contact.html')