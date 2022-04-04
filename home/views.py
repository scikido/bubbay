from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, phone=phone,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your Message has succesfully submitted!')
    return render(request,"contact.html")
