from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django import forms
from .forms import RegisterForm, LoginForm
# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        
        return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'user_form': form,
    }
    return render(request, 'register.html', context)

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                raise forms.ValidationError('user not found')
    
    else:
        form = LoginForm()
    context = {
        'login_form': form,
    }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')