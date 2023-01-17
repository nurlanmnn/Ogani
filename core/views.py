from django.shortcuts import render
from .models import Setting

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    setting = Setting.objects.first()
    context = {
        'settings': setting
    }
    return render(request, 'index.html', context)

