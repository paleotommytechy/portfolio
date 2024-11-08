from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import *
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

def homepage(request):
    projects = Project.objects.all()
    testimonies = Testimonie.objects.all()
    return render(request, 'homepage.html',{'projects':projects,'testimonies':testimonies})

def about(request):
    return render(request, 'about.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{'projects':projects})

def testimonies(request):
    testimonies = Testimonie.objects.all()
    return render(request, 'testimonies.html', {'testimonies':testimonies})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"A new message from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject,
                full_message,
                email,
                ['olusegunifetomiwa2000@gmail.com'])
            print("Email succesfully sent")
        return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})