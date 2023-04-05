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


from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes 
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.db.models.query_utils import Q



# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "registration/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					"user": user,
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'memmedlinurlan2020@gmail.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="registration/password_reset_form.html", context={"password_reset_form":password_reset_form})
