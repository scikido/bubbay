from django.shortcuts import redirect, render
from home.models import Submissons
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.


def index(request):
    return render(request, "index.html")


@login_required(login_url='login')
def community(request):
    submissions = Submissons.objects.all()

    return render(request, "community.html", {'submissions': submissions})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('community')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('community')

            else:
                messages.info(request, 'Username or Password is incorrect')

        return render(request, 'login.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('community')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,
                                 "Succesfully Created Account For " + user)
                return redirect('login')
        context = {'form': form}

        return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        name_author = request.POST.get('name')
        email_author = request.POST.get('email')
        credit_author = request.POST.get('link')
        content = request.POST.get('desc')
        content_title = request.POST.get("title")
        contact = Submissons(name_author=name_author,
                             email_author=email_author,
                             credit_author=credit_author,
                             content=content,
                             content_title=content_title,
                             date=datetime.today())
        contact.save()
        messages.success(request, 'Your Content has succesfully submitted!')
    return render(request, "contact.html")
