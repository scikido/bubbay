from django.shortcuts import render
from home.models import Submissons
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def community(request):
    submissions=Submissons.objects.all()
    return render(request,"community.html",
    {'submissions':submissions})

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method=="POST":
        name_author=request.POST.get('name')
        email_author=request.POST.get('email')
        credit_author=request.POST.get('link')
        content=request.POST.get('desc')
        content_title=request.POST.get("title")
        contact=Submissons(name_author=name_author,email_author=email_author,credit_author=credit_author,content=content,content_title=content_title,date=datetime.today())
        contact.save()
        messages.success(request,'Your Content has succesfully submitted!')
    return render(request,"contact.html")
