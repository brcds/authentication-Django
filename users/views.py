from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import RegistrationForm
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form_user = RegistrationForm(request.POST)
        if form_user.is_valid():
            form_user.save();
            return redirect('login_user')
    else:
        form_user = RegistrationForm()
    return render (request,'register.html', {'form_user' : form_user})

def login_user(request):
    if request.method == "POST":
        username    = request.POST["username"]
        password    = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'username or password not correct')
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@login_required(login_url='/login_user')
def change_password(request):
    if request.method == "POST":
        form_password = PasswordChangeForm(request.user, request.POST)
        if form_password.is_valid():
            user = form_password.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_password = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form_password': form_password})

@login_required(login_url='/login_user')
def logout_user(request):
    logout(request)
    return redirect('index')

@login_required(login_url ='/login_user')
def index(request):
    return render(request, 'index.html')