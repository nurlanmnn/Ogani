from django.shortcuts import render

from core.forms import SubscriberForm
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
    subscribe_form = SubscriberForm()
    context = {
        'settings': setting,
        'subscribe_form': subscribe_form,
    }
    return render(request, 'index.html', context)

def home(request):
    advars = Advertisement.objects.all()
    context = {
        'advars': advars,
    }
    return render(request, 'index.html', context)