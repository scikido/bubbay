from os import name
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("services/", views.services,name="services"),
    path("community/",views.community,name="community"),
    path("login/",views.loginPage, name="login"),
    path("register/",views.registerPage, name="register"),
    path("logout/",views.logoutUser, name="logout"),
    path("decoder/",views.decode, name="decoder")
]
