from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'sassy':'sarvadnya',
    }
    return render(request,"index.html", context)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")
