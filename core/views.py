from django.shortcuts import render
from .models import Advertisement, Setting, Contact

# Create your views here.


def contact(request):
    contact = Contact.objects.first()
    context = {
        'contact': contact
    }
    return render(request, 'contact.html', context)

def index(request):
    setting = Setting.objects.first()
    context = {
        'settings': setting
    }
    return render(request, 'index.html', context)

def home(request):
    advars = Advertisement.objects.all()
    context = {
        'advars': advars
    }
    return render(request, 'index.html', context)