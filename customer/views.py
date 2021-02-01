from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, CustomUserCreationForm
from django.http import HttpResponse
from .models import CustomUser


def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for "+ username)
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, "customer/register.html", context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(username, password, user, end="\n") 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Email or Password are incorrect!")
    context = {'form': form}
    return render(request, "customer/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, "customer/home.html")